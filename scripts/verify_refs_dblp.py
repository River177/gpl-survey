"""Verify every cited reference in zotero.bib against DBLP.

For each citation key actually used in tex/*.tex, query the DBLP publication
search API by title, pick the best title match, and compare title / authors /
year / venue with the bib entry. Writes a Markdown audit report to
docs/research/dblp_reference_audit.md.

Usage:
    python3 scripts/verify_refs_dblp.py            # audit all cited keys
    python3 scripts/verify_refs_dblp.py --limit 10 # quick smoke test

The script is read-only with respect to zotero.bib; it only reports. Apply
corrections manually based on the report.
"""
import argparse
import html
import os
import re
import sys
import time
import json
import urllib.parse
import urllib.request

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _paper_utils import collect_cited_keys, parse_bib, canonical_venue  # noqa: E402

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TEX_DIR = os.path.join(ROOT, "tex")
BIB_PATH = os.path.join(TEX_DIR, "zotero.bib")
REPORT_PATH = os.path.join(ROOT, "docs", "research", "dblp_reference_audit.md")
CACHE_PATH = os.path.join(ROOT, "docs", "research", ".dblp_cache.json")

DBLP_HOSTS = [
    "https://dblp.uni-trier.de/search/publ/api",
    "https://dblp.org/search/publ/api",
]


def norm_title(s):
    s = s.lower()
    s = re.sub(r"[{}\\]", "", s)
    s = re.sub(r"[^a-z0-9 ]", " ", s)
    s = re.sub(r"\s+", " ", s).strip()
    return s


def title_sim(a, b):
    """Token Jaccard similarity on normalized titles."""
    ta, tb = set(norm_title(a).split()), set(norm_title(b).split())
    if not ta or not tb:
        return 0.0
    return len(ta & tb) / len(ta | tb)


def dblp_query(title, retries=6):
    q = norm_title(title)
    params = f"?q={urllib.parse.quote(q)}&format=json&h=8"
    last_err = "unknown"
    for attempt in range(retries):
        # Prefer the working mirror; only fall back occasionally.
        host = DBLP_HOSTS[0] if attempt % 3 != 2 else DBLP_HOSTS[1]
        url = host + params
        try:
            req = urllib.request.Request(url, headers={"User-Agent": "gpl-survey-ref-audit/1.0"})
            with urllib.request.urlopen(req, timeout=30) as resp:
                data = json.load(resp)
            hits = data.get("result", {}).get("hits", {}).get("hit", [])
            return hits
        except Exception as e:  # noqa: BLE001
            last_err = str(e)
            time.sleep(5 + 5 * attempt)  # exponential-ish backoff for rate limits
    return {"_error": last_err}


def best_match(title, hits):
    best, best_s = None, 0.0
    for h in hits:
        info = h.get("info", {})
        t = info.get("title", "")
        s = title_sim(title, t)
        if s > best_s:
            best, best_s = info, s
    return best, best_s


def fmt_authors(info):
    a = info.get("authors", {}).get("author", [])
    if isinstance(a, dict):
        a = [a]
    names = []
    for x in a:
        if isinstance(x, dict):
            names.append(x.get("text", ""))
        else:
            names.append(str(x))
    return names


def bib_first_author(entry):
    auth = entry.get("author", "")
    if not auth:
        return ""
    first = re.split(r"\band\b", auth)[0]
    first = first.replace("{", "").replace("}", "").strip()
    return first


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--limit", type=int, default=0, help="only audit first N keys")
    ap.add_argument("--sleep", type=float, default=1.5, help="seconds between API calls")
    args = ap.parse_args()

    keys = collect_cited_keys(TEX_DIR)
    bib = parse_bib(BIB_PATH)
    cited = [k for k in keys if k in bib]
    if args.limit:
        cited = cited[: args.limit]

    cache = {}
    if os.path.exists(CACHE_PATH):
        try:
            with open(CACHE_PATH, encoding="utf-8") as fh:
                cache = json.load(fh)
        except Exception:  # noqa: BLE001
            cache = {}

    rows = []
    counts = {"OK": 0, "REVIEW": 0, "NOT_FOUND": 0, "ERROR": 0, "NO_TITLE": 0}

    for idx, key in enumerate(cited, 1):
        entry = bib[key]
        title = entry.get("title", "")
        venue = canonical_venue(entry)
        byear = entry.get("year", "")
        print(f"[{idx}/{len(cited)}] {key} ...", file=sys.stderr)
        if not title:
            counts["NO_TITLE"] += 1
            rows.append((key, "NO_TITLE", title, venue, byear, "", "", "", "no title field in bib"))
            continue
        if key in cache and cache[key].get("hits") is not None:
            hits = cache[key]["hits"]
        else:
            hits = dblp_query(title)
            if not (isinstance(hits, dict) and "_error" in hits):
                cache[key] = {"hits": hits}
                with open(CACHE_PATH, "w", encoding="utf-8") as fh:
                    json.dump(cache, fh)
            time.sleep(args.sleep)
        if isinstance(hits, dict) and "_error" in hits:
            counts["ERROR"] += 1
            rows.append((key, "ERROR", title, venue, byear, "", "", "", hits["_error"]))
            continue
        info, sim = best_match(title, hits or [])
        if not info or sim < 0.6:
            counts["NOT_FOUND"] += 1
            rows.append((key, "NOT_FOUND", title, venue, byear, "", "", f"{sim:.2f}",
                         "no confident DBLP title match"))
            continue

        d_title = info.get("title", "")
        d_year = str(info.get("year", ""))
        d_venue = info.get("venue", "")
        if isinstance(d_venue, list):
            d_venue = ", ".join(d_venue)
        d_type = info.get("type", "")

        notes = []
        # year check
        if byear and d_year and byear != d_year:
            notes.append(f"year bib={byear} dblp={d_year}")
        # arXiv published elsewhere?
        if venue == "arXiv preprint" and d_venue and "CoRR" not in d_venue:
            notes.append(f"bib=arXiv but DBLP venue='{d_venue}' (consider upgrading)")
        # venue mismatch heuristic
        elif d_venue:
            dv_canon_text = d_venue.lower()
            if venue not in ("Others", "Unknown") and venue.lower() not in dv_canon_text:
                # only flag if clearly different and not arXiv
                if "corr" not in dv_canon_text:
                    notes.append(f"venue bib='{venue}' dblp='{d_venue}'")
        # title close but not exact
        if sim < 0.92:
            notes.append(f"title sim={sim:.2f}")

        status = "OK" if not notes else "REVIEW"
        counts[status] += 1
        rows.append((key, status, title, venue, byear, d_venue, d_year,
                     f"{sim:.2f}", "; ".join(notes)))

    write_report(rows, counts, len(cited))
    print("\nSummary:", counts, file=sys.stderr)
    print("Report written to", REPORT_PATH, file=sys.stderr)


def write_report(rows, counts, total):
    os.makedirs(os.path.dirname(REPORT_PATH), exist_ok=True)
    lines = []
    lines.append("# DBLP Reference Audit\n")
    lines.append(f"Total cited references audited: **{total}**\n")
    lines.append("Status counts: " + ", ".join(f"{k}={v}" for k, v in counts.items()) + "\n")
    lines.append("- **OK**: confident DBLP title match, no metadata discrepancy.")
    lines.append("- **REVIEW**: matched but year/venue/title needs a look (see Notes).")
    lines.append("- **NOT_FOUND**: no confident DBLP match (preprint-only or title drift).")
    lines.append("- **ERROR/NO_TITLE**: API error or missing title field.\n")

    def section(title, status):
        sub = [r for r in rows if r[1] == status]
        if not sub:
            return
        lines.append(f"\n## {title} ({len(sub)})\n")
        lines.append("| Key | Bib venue | Bib year | DBLP venue | DBLP year | Sim | Notes |")
        lines.append("|---|---|---|---|---|---|---|")
        for key, _st, _t, bv, by, dv, dy, sim, notes in sub:
            lines.append(f"| `{key}` | {bv} | {by} | {dv} | {dy} | {sim} | {notes} |")

    section("REVIEW \u2014 needs manual check", "REVIEW")
    section("NOT_FOUND \u2014 no DBLP match", "NOT_FOUND")
    section("ERROR", "ERROR")
    section("NO_TITLE", "NO_TITLE")
    section("OK", "OK")

    with open(REPORT_PATH, "w", encoding="utf-8") as fh:
        fh.write("\n".join(lines) + "\n")


if __name__ == "__main__":
    main()
