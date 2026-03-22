#!/usr/bin/env python3
"""Download papers referenced in a BibTeX file and report arXiv publication status."""

from __future__ import annotations

import argparse
import csv
import html
import io
import re
import sys
import time
import unicodedata
import xml.etree.ElementTree as ET
from dataclasses import dataclass
from difflib import SequenceMatcher
from pathlib import Path
from urllib.parse import urljoin
from typing import Iterable

import requests


USER_AGENT = "GPLSurveyPaperFetcher/0.1 (Codex)"
OPENALEX_URL = "https://api.openalex.org/works"
CROSSREF_URL = "https://api.crossref.org/works"
ARXIV_API_URL = "https://export.arxiv.org/api/query"
DBLP_SEARCH_URL = "https://dblp.org/search/publ/api"

MANUAL_PDF_OVERRIDES = {
    "ahmed2013distributed": [
        "https://static.googleusercontent.com/media/research.google.com/en/us/pubs/archive/40839.pdf",
    ],
    "pan2010survey": [
        "https://dl.icdst.org/pdfs/files/6125c5c9c719611ca598cd4a7d5396d4.pdf",
    ],
    "jiang2021contrastive": [
        "https://yuanfulu.github.io/publication/CIKM-CPT.pdf",
    ],
    "sun2021mocl": [
        "https://arxiv.org/pdf/2106.04509.pdf",
    ],
    "jiang2021pretraining": [
        "https://smufang.github.io/paper/KDD21_PT-HGNN.pdf",
    ],
    "li2023what": [
        "https://arxiv.org/pdf/2205.10053.pdf",
    ],
    "long2022pretraining": [
        "https://academic.oup.com/bioinformatics/article-pdf/38/8/2254/49009728/btac100.pdf",
    ],
    "ou2016asymmetric": [
        "https://www.kdd.org/kdd2016/papers/files/rfp0184-ouA.pdf",
    ],
    "cao2015grarep": [
        "https://ir.sdu.edu.cn/~zhuminchen/RL/Cao2015.pdf",
    ],
    "yao2023schemaaware": [
        "https://arxiv.org/pdf/2210.10709.pdf",
    ],
    "huan2023tea": [
        "https://madsys.cs.tsinghua.edu.cn/publication/tea-a-general-purpose-temporal-graph-random-walk-engine/eurosys23-huan.pdf",
    ],
    "wang2022common": [
        "https://www.cse.cuhk.edu.hk/~cslui/PUBLICATION/IEEE-TKDE-CNM-23.pdf",
    ],
    "wang2021selfsuperviseda": [
        "https://arxiv.org/pdf/2105.09111.pdf",
    ],
    "wang2017mgae": [
        "https://shiruipan.github.io/publication/wang-mgae-2017/wang-mgae-2017.pdf",
    ],
    "bran2023transformers": [
        "https://arxiv.org/pdf/2310.06083.pdf",
    ],
    "wang2023scientific": [
        "https://ai.stanford.edu/~jure/pubs/discovery-nature23.pdf",
    ],
    "rosenstein2005transfer": [
        "https://people.csail.mit.edu/mtr/papers/RosensteinM05c.pdf",
    ],
    "zhang2023large": [
        "https://arxiv.org/pdf/2308.14522.pdf",
    ],
}


@dataclass
class Entry:
    entry_type: str
    key: str
    fields: dict[str, str]


def read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def clean_title(raw: str) -> str:
    text = raw.replace("\n", " ").replace("\t", " ")
    text = re.sub(r"[{}]", "", text)
    text = re.sub(r"\\[a-zA-Z]+\s*", "", text)
    text = text.replace("\\&", "&")
    text = re.sub(r"\s+", " ", text).strip()
    return text


def normalize_title(title: str) -> str:
    title = clean_title(title)
    title = unicodedata.normalize("NFKD", title).encode("ascii", "ignore").decode("ascii")
    title = title.lower()
    title = re.sub(r"[^a-z0-9]+", " ", title)
    return re.sub(r"\s+", " ", title).strip()


def normalize_author(author: str) -> str:
    author = clean_title(author)
    author = author.split(" and ")[0].strip()
    if "," in author:
        author = author.split(",", 1)[0]
    else:
        author = author.split()[-1] if author.split() else author
    return normalize_title(author)


def parse_bibtex(text: str) -> list[Entry]:
    entries: list[Entry] = []
    idx = 0
    length = len(text)
    while idx < length:
        at = text.find("@", idx)
        if at == -1:
            break
        brace = text.find("{", at)
        if brace == -1:
            break
        entry_type = text[at + 1 : brace].strip()
        depth = 1
        j = brace + 1
        while j < length and depth > 0:
            ch = text[j]
            if ch == "{":
                depth += 1
            elif ch == "}":
                depth -= 1
            j += 1
        body = text[brace + 1 : j - 1].strip()
        idx = j
        comma = body.find(",")
        if comma == -1:
            continue
        key = body[:comma].strip()
        fields_block = body[comma + 1 :]
        fields = parse_fields(fields_block)
        entries.append(Entry(entry_type=entry_type, key=key, fields=fields))
    return entries


def parse_fields(block: str) -> dict[str, str]:
    fields: dict[str, str] = {}
    i = 0
    n = len(block)
    while i < n:
        while i < n and block[i] in " \r\n\t,":
            i += 1
        if i >= n:
            break
        start = i
        while i < n and re.match(r"[A-Za-z0-9_\-]", block[i]):
            i += 1
        name = block[start:i].strip().lower()
        while i < n and block[i].isspace():
            i += 1
        if i >= n or block[i] != "=":
            while i < n and block[i] != ",":
                i += 1
            continue
        i += 1
        while i < n and block[i].isspace():
            i += 1
        if i >= n:
            break
        if block[i] == "{":
            depth = 1
            i += 1
            start = i
            while i < n and depth > 0:
                if block[i] == "{":
                    depth += 1
                elif block[i] == "}":
                    depth -= 1
                i += 1
            value = block[start : i - 1]
        elif block[i] == '"':
            i += 1
            start = i
            escaped = False
            while i < n:
                ch = block[i]
                if ch == '"' and not escaped:
                    break
                escaped = ch == "\\" and not escaped
                if ch != "\\":
                    escaped = False
                i += 1
            value = block[start:i]
            i += 1
        else:
            start = i
            while i < n and block[i] not in ",\r\n":
                i += 1
            value = block[start:i].strip()
        fields[name] = value.strip()
    return fields


def is_arxiv_entry(entry: Entry) -> bool:
    joined = " ".join(
        [
            entry.fields.get("journal", ""),
            entry.fields.get("note", ""),
            entry.fields.get("eprint", ""),
            entry.fields.get("archiveprefix", ""),
        ]
    ).lower()
    return "arxiv" in joined


def extract_arxiv_id(entry: Entry) -> str | None:
    for key in ("eprint", "note", "url"):
        value = entry.fields.get(key, "")
        match = re.search(r"arxiv[:/\s]*([0-9]{4}\.[0-9]{4,5}(?:v\d+)?)", value, re.I)
        if match:
            return match.group(1)
        match = re.search(r"arxiv\.org/(?:abs|pdf)/([^/\s]+)", value, re.I)
        if match:
            return match.group(1).replace(".pdf", "")
    return None


def request_json(session: requests.Session, url: str, params: dict[str, str] | None = None) -> dict | None:
    for attempt in range(3):
        try:
            response = session.get(url, params=params, timeout=30)
            response.raise_for_status()
            return response.json()
        except Exception:
            if attempt == 2:
                return None
            time.sleep(1.5 * (attempt + 1))
    return None


def request_text(session: requests.Session, url: str, params: dict[str, str] | None = None) -> str | None:
    for attempt in range(3):
        try:
            response = session.get(url, params=params, timeout=30)
            response.raise_for_status()
            return response.text
        except Exception:
            if attempt == 2:
                return None
            time.sleep(1.5 * (attempt + 1))
    return None


def title_similarity(a: str, b: str) -> float:
    return SequenceMatcher(None, normalize_title(a), normalize_title(b)).ratio()


def author_matches(entry: Entry, author_names: Iterable[str]) -> bool:
    expected = normalize_author(entry.fields.get("author", ""))
    if not expected:
        return True
    candidates = {normalize_title(name) for name in author_names if name}
    return any(expected and expected in name for name in candidates)


def find_openalex_work(session: requests.Session, entry: Entry) -> dict | None:
    doi = entry.fields.get("doi", "").strip()
    if doi:
        work = request_json(session, f"{OPENALEX_URL}/https://doi.org/{doi}")
        if work and work.get("id"):
            return work
    title = clean_title(entry.fields.get("title", ""))
    if not title:
        return None
    data = request_json(session, OPENALEX_URL, {"search": title, "per-page": "5"})
    if not data:
        return None
    best = None
    best_score = 0.0
    for work in data.get("results", []):
        score = title_similarity(title, work.get("display_name", ""))
        author_names = [a.get("author", {}).get("display_name", "") for a in work.get("authorships", [])]
        if not author_matches(entry, author_names):
            score -= 0.08
        if score > best_score:
            best_score = score
            best = work
    return best if best and best_score >= 0.84 else None


def find_crossref_publication(session: requests.Session, entry: Entry) -> dict | None:
    title = clean_title(entry.fields.get("title", ""))
    if not title:
        return None
    data = request_json(session, CROSSREF_URL, {"query.title": title, "rows": "5"})
    if not data:
        return None
    best = None
    best_score = 0.0
    for item in data.get("message", {}).get("items", []):
        titles = item.get("title") or []
        if not titles:
            continue
        candidate_title = titles[0]
        score = title_similarity(title, candidate_title)
        author_names = [a.get("family", "") for a in item.get("author", [])]
        if not author_matches(entry, author_names):
            score -= 0.08
        if item.get("type") == "posted-content":
            score -= 0.1
        if score > best_score:
            best_score = score
            best = item
    if best and best_score >= 0.90 and best.get("type") != "posted-content":
        return best
    return None


def find_arxiv_id_by_title(session: requests.Session, entry: Entry) -> str | None:
    known = extract_arxiv_id(entry)
    if known:
        return known
    title = clean_title(entry.fields.get("title", ""))
    if not title:
        return None
    xml_text = request_text(session, ARXIV_API_URL, {"search_query": f'ti:"{title}"', "max_results": "5"})
    if not xml_text:
        return None
    try:
        root = ET.fromstring(xml_text)
    except ET.ParseError:
        return None
    ns = {"a": "http://www.w3.org/2005/Atom"}
    best_id = None
    best_score = 0.0
    for node in root.findall("a:entry", ns):
        id_text = node.findtext("a:id", default="", namespaces=ns)
        title_text = html.unescape(node.findtext("a:title", default="", namespaces=ns))
        score = title_similarity(title, title_text)
        if score > best_score:
            best_score = score
            best_id = id_text.rsplit("/", 1)[-1]
    return best_id if best_id and best_score >= 0.90 else None


def find_dblp_urls(session: requests.Session, entry: Entry) -> list[str]:
    title = clean_title(entry.fields.get("title", ""))
    if not title:
        return []
    data = request_json(
        session,
        DBLP_SEARCH_URL,
        {"q": title, "h": "5", "format": "json"},
    )
    if not data:
        return []
    hits = data.get("result", {}).get("hits", {}).get("hit", [])
    if isinstance(hits, dict):
        hits = [hits]
    urls: list[str] = []
    for hit in hits:
        info = hit.get("info", {})
        candidate_title = info.get("title", "")
        if title_similarity(title, candidate_title) < 0.90:
            continue
        ee = info.get("ee")
        if isinstance(ee, list):
            urls.extend(ee)
        elif isinstance(ee, str):
            urls.append(ee)
    deduped: list[str] = []
    seen: set[str] = set()
    for url in urls:
        if not url:
            continue
        if "arxiv.org/abs/" in url:
            url = url.replace("http://", "https://").replace("/abs/", "/pdf/")
            if not url.endswith(".pdf"):
                url += ".pdf"
        if "doi.org/10.48550/arXiv." in url:
            arxiv_id = url.rsplit("arXiv.", 1)[-1]
            url = f"https://arxiv.org/pdf/{arxiv_id}.pdf"
        if url not in seen:
            seen.add(url)
            deduped.append(url)
    return deduped


def pdf_url_candidates(entry: Entry, work: dict | None, arxiv_id: str | None, dblp_urls: list[str]) -> list[str]:
    urls: list[str] = []
    urls.extend(MANUAL_PDF_OVERRIDES.get(entry.key, []))
    if work:
        for location_key in ("best_oa_location", "primary_location"):
            location = work.get(location_key) or {}
            for field in ("pdf_url", "landing_page_url"):
                url = location.get(field)
                if url:
                    urls.append(url)
        for location in work.get("locations", []) or []:
            for field in ("pdf_url", "landing_page_url"):
                url = location.get(field)
                if url:
                    urls.append(url)
        doi = work.get("doi")
        if doi:
            urls.append(doi)
        ids = work.get("ids") or {}
        arxiv_url = ids.get("arxiv")
        if arxiv_url:
            candidate = arxiv_url.rstrip("/").rsplit("/", 1)[-1]
            urls.append(f"https://arxiv.org/pdf/{candidate}.pdf")
    doi = entry.fields.get("doi", "").strip()
    if doi:
        urls.append(f"https://doi.org/{doi}")
    if arxiv_id:
        urls.append(f"https://arxiv.org/pdf/{arxiv_id}.pdf")
    urls.extend(dblp_urls)
    # Preserve order while deduplicating.
    deduped: list[str] = []
    seen: set[str] = set()
    for url in urls:
        if url and url not in seen:
            deduped.append(url)
            seen.add(url)
    return deduped


def extract_pdf_links_from_html(page_url: str, text: str) -> list[str]:
    patterns = [
        r'<meta[^>]+name=["\']citation_pdf_url["\'][^>]+content=["\']([^"\']+)["\']',
        r'<meta[^>]+content=["\']([^"\']+)["\'][^>]+name=["\']citation_pdf_url["\']',
        r'href=["\']([^"\']+\.pdf(?:\?[^"\']*)?)["\']',
    ]
    links: list[str] = []
    for pattern in patterns:
        for match in re.findall(pattern, text, flags=re.I):
            links.append(urljoin(page_url, html.unescape(match)))
    deduped: list[str] = []
    seen: set[str] = set()
    for link in links:
        if link not in seen:
            deduped.append(link)
            seen.add(link)
    return deduped


def download_pdf(session: requests.Session, url: str, dest: Path, depth: int = 0) -> tuple[bool, str]:
    try:
        response = session.get(url, stream=True, timeout=60, allow_redirects=True)
        response.raise_for_status()
        header = response.headers.get("content-type", "").lower()
        chunks: list[bytes] = []
        size = 0
        for chunk in response.iter_content(chunk_size=65536):
            if chunk:
                chunks.append(chunk)
                size += len(chunk)
                if size >= 262144:
                    break
        prefix = b"".join(chunks)
        is_pdf = "pdf" in header or url.lower().endswith(".pdf") or prefix.startswith(b"%PDF")
        if not is_pdf:
            if depth == 0 and ("html" in header or prefix.lstrip().startswith(b"<")):
                text = prefix.decode("utf-8", errors="ignore")
                for link in extract_pdf_links_from_html(response.url, text):
                    ok, note = download_pdf(session, link, dest, depth=1)
                    if ok:
                        return ok, note
            return False, f"not a PDF ({header or 'unknown content-type'})"
        with dest.open("wb") as handle:
            handle.write(prefix)
            for chunk in response.iter_content(chunk_size=65536):
                if chunk:
                    handle.write(chunk)
        return True, "downloaded"
    except Exception as exc:
        return False, str(exc)


def publication_info_from_crossref(item: dict) -> tuple[str, str, str]:
    venue = ""
    container = item.get("container-title") or []
    if container:
        venue = container[0]
    elif item.get("event", {}).get("name"):
        venue = item["event"]["name"]
    elif item.get("publisher"):
        venue = item["publisher"]
    year = ""
    for key in ("published-print", "published-online", "issued"):
        parts = item.get(key, {}).get("date-parts") or []
        if parts and parts[0]:
            year = str(parts[0][0])
            break
    doi = item.get("DOI", "")
    return venue, year, doi


def publication_info_from_openalex(work: dict) -> tuple[str, str, str]:
    primary = work.get("primary_location") or {}
    source = primary.get("source") or {}
    venue = source.get("display_name", "")
    year = str(work.get("publication_year") or "")
    doi = work.get("doi", "")
    return venue, year, doi


def ensure_directory(path: Path) -> None:
    path.mkdir(parents=True, exist_ok=True)


def is_pdf_file(path: Path) -> bool:
    if not path.exists() or path.stat().st_size < 5:
        return False
    with path.open("rb") as handle:
        return handle.read(5) == b"%PDF-"


def write_report(rows: list[dict[str, str]], report_dir: Path) -> None:
    csv_path = report_dir / "download-report.csv"
    with csv_path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(rows[0].keys()) if rows else [])
        if rows:
            writer.writeheader()
            writer.writerows(rows)

    arxiv_rows = [row for row in rows if row["is_arxiv"] == "yes"]
    md_path = report_dir / "arxiv-publication-status.md"
    with md_path.open("w", encoding="utf-8") as handle:
        handle.write("# arXiv Publication Status\n\n")
        handle.write(f"- Total BibTeX entries: {len(rows)}\n")
        handle.write(f"- arXiv-tagged entries: {len(arxiv_rows)}\n")
        handle.write(f"- Successfully downloaded PDFs: {sum(1 for row in rows if row['download_status'] == 'downloaded')}\n")
        handle.write(f"- arXiv entries with formal publication match: {sum(1 for row in arxiv_rows if row['arxiv_publication_status'] == 'published')}\n")
        handle.write("\n| Key | Title | Publication Status | Venue | Year | DOI | PDF |\n")
        handle.write("| --- | --- | --- | --- | --- | --- | --- |\n")
        for row in arxiv_rows:
            pdf_value = row["saved_pdf"] if row["saved_pdf"] else row["download_note"]
            handle.write(
                f"| {row['key']} | {row['title'].replace('|', ' ')} | {row['arxiv_publication_status']} | "
                f"{row['published_venue'].replace('|', ' ')} | {row['published_year']} | "
                f"{row['published_doi']} | {pdf_value.replace('|', ' ')} |\n"
            )


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("bib", type=Path, help="Path to the BibTeX file")
    parser.add_argument(
        "--output-dir",
        type=Path,
        default=Path("papers/zotero"),
        help="Directory to save downloaded PDFs and reports",
    )
    parser.add_argument(
        "--keys",
        nargs="*",
        default=None,
        help="Optional BibTeX keys to process",
    )
    args = parser.parse_args()

    entries = parse_bibtex(read_text(args.bib))
    if args.keys:
        wanted = set(args.keys)
        entries = [entry for entry in entries if entry.key in wanted]
    ensure_directory(args.output_dir)
    ensure_directory(args.output_dir / "pdfs")

    session = requests.Session()
    session.headers.update({"User-Agent": USER_AGENT})

    rows: list[dict[str, str]] = []
    total = len(entries)
    for index, entry in enumerate(entries, start=1):
        title = clean_title(entry.fields.get("title", ""))
        year = entry.fields.get("year", "")
        work = find_openalex_work(session, entry)
        arxiv_id = find_arxiv_id_by_title(session, entry) if is_arxiv_entry(entry) else None
        dblp_urls = find_dblp_urls(session, entry)
        pdf_dest = args.output_dir / "pdfs" / f"{entry.key}.pdf"
        download_status = "missing"
        download_note = ""
        saved_pdf = ""
        if pdf_dest.exists():
            if is_pdf_file(pdf_dest):
                download_status = "downloaded"
                download_note = "already existed"
                saved_pdf = str(pdf_dest)
            else:
                pdf_dest.unlink()
        else:
            for candidate_url in pdf_url_candidates(entry, work, arxiv_id, dblp_urls):
                ok, note = download_pdf(session, candidate_url, pdf_dest)
                if ok:
                    download_status = "downloaded"
                    download_note = candidate_url
                    saved_pdf = str(pdf_dest)
                    break
                if pdf_dest.exists() and not is_pdf_file(pdf_dest):
                    pdf_dest.unlink()
                download_note = note

        arxiv_status = ""
        published_venue = ""
        published_year = ""
        published_doi = ""
        if is_arxiv_entry(entry):
            crossref_item = find_crossref_publication(session, entry)
            if crossref_item:
                arxiv_status = "published"
                published_venue, published_year, published_doi = publication_info_from_crossref(crossref_item)
            elif work:
                venue, pub_year, pub_doi = publication_info_from_openalex(work)
                source_type = ((work.get("primary_location") or {}).get("source") or {}).get("type", "")
                source_name = ((work.get("primary_location") or {}).get("source") or {}).get("display_name", "")
                if venue and source_name.lower() != "arxiv" and source_type != "repository":
                    arxiv_status = "published"
                    published_venue, published_year, published_doi = venue, pub_year, pub_doi
                else:
                    arxiv_status = "preprint_only"
            else:
                arxiv_status = "unknown"

        row = {
            "key": entry.key,
            "entry_type": entry.entry_type,
            "title": title,
            "year": year,
            "is_arxiv": "yes" if is_arxiv_entry(entry) else "no",
            "download_status": download_status,
            "download_note": download_note,
            "saved_pdf": saved_pdf,
            "openalex_id": work.get("id", "") if work else "",
            "matched_openalex_title": work.get("display_name", "") if work else "",
            "arxiv_publication_status": arxiv_status,
            "published_venue": published_venue,
            "published_year": published_year,
            "published_doi": published_doi,
        }
        rows.append(row)
        print(
            f"[{index:03d}/{total:03d}] {entry.key}: {download_status}"
            + (f", arXiv={arxiv_status}" if row["is_arxiv"] == "yes" else "")
        )
        sys.stdout.flush()
        time.sleep(0.15)

    write_report(rows, args.output_dir)
    downloaded = sum(1 for row in rows if row["download_status"] == "downloaded")
    arxiv_published = sum(1 for row in rows if row["arxiv_publication_status"] == "published")
    print(f"Finished. Downloaded {downloaded}/{len(rows)} PDFs.")
    print(f"arXiv entries marked published: {arxiv_published}.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
