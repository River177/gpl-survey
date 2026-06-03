"""Shared helpers for paper figure/reference tooling.

Provides:
- collect_cited_keys: scan tex/*.tex for keys used in \\cite / \\citet / ...
- parse_bib: minimal BibTeX parser returning {key: {field: value}}
- canonical_venue: map raw booktitle/journal strings to canonical short venue
"""
import os
import re
import glob

CITE_RE = re.compile(r"\\[a-zA-Z]*cite[a-zA-Z]*\s*(?:\[[^\]]*\])?\s*\{([^}]*)\}")
COMMENT_RE = re.compile(r"(?<!\\)%.*")


def _strip_comments(text):
    """Remove LaTeX line comments (unescaped % to end of line)."""
    return "\n".join(COMMENT_RE.sub("", line) for line in text.splitlines())


def collect_cited_keys(tex_dir):
    """Return sorted list of distinct citation keys used across tex_dir/*.tex."""
    keys = set()
    for path in glob.glob(os.path.join(tex_dir, "*.tex")):
        with open(path, encoding="utf-8") as fh:
            text = _strip_comments(fh.read())
        for match in CITE_RE.findall(text):
            for raw in match.split(","):
                key = raw.strip()
                if key:
                    keys.add(key)
    return sorted(keys)


def parse_bib(bib_path):
    """Parse BibTeX via bibtexparser. Returns {key: {"_type": str, field: value}}."""
    import bibtexparser
    from bibtexparser.bparser import BibTexParser

    parser = BibTexParser(common_strings=True)
    parser.ignore_nonstandard_types = False
    with open(bib_path, encoding="utf-8") as fh:
        db = bibtexparser.load(fh, parser=parser)

    entries = {}
    for raw in db.entries:
        key = raw.get("ID")
        if not key:
            continue
        fields = {}
        for k, v in raw.items():
            if k in ("ID", "ENTRYTYPE"):
                continue
            fields[k.lower()] = _clean_value(v)
        fields["_type"] = raw.get("ENTRYTYPE", "").lower()
        entries[key] = fields
    return entries


def _clean_value(v):
    v = v.replace("\n", " ").replace("\t", " ")
    v = re.sub(r"\s+", " ", v).strip()
    return v


# --- venue canonicalization -------------------------------------------------
# Order matters: more specific patterns first.
VENUE_PATTERNS = [
    ("arXiv preprint", [r"\barxiv\b", r"\bcorr\b", r"\bpreprint\b"]),
    ("NeurIPS", [r"neurips", r"neural information processing systems", r"\bnips\b"]),
    ("ICLR", [r"\biclr\b", r"international conference on learning representations"]),
    ("ICML", [r"\bicml\b", r"international conference on machine learning"]),
    ("KDD", [r"\bkdd\b", r"knowledge discovery and data mining", r"sigkdd"]),
    ("WWW", [r"web conference", r"\bwww\b", r"world wide web"]),
    ("CIKM", [r"\bcikm\b", r"information and knowledge management"]),
    ("SIGIR", [r"\bsigir\b", r"research and development in information retrieval"]),
    ("IJCAI", [r"\bijcai\b", r"international joint conference on artificial intelligence"]),
    ("AAAI", [r"\baaai\b"]),
    ("EMNLP", [r"\bemnlp\b", r"empirical methods in natural language processing"]),
    ("NAACL", [r"\bnaacl\b"]),
    ("ACL", [r"\bacl\b", r"association for computational linguistics"]),
    ("WSDM", [r"\bwsdm\b", r"web search and data mining"]),
    ("TKDE", [r"\btkde\b", r"transactions on knowledge and data engineering"]),
    ("ICDE", [r"\bicde\b", r"international conference on data engineering"]),
    ("ICCV", [r"\biccv\b", r"international conference on computer vision"]),
    ("CVPR", [r"\bcvpr\b", r"computer vision and pattern recognition"]),
    ("ECCV", [r"\beccv\b"]),
    ("ECML PKDD", [r"ecml", r"pkdd", r"machine learning and knowledge discovery in databases"]),
    ("Nature", [r"\bnature\b"]),
    ("TMLR", [r"transactions on machine learning research", r"\btmlr\b"]),
    ("ACM Computing Surveys", [r"computing surveys", r"\bcsur\b"]),
]


def canonical_venue(entry):
    """Map a bib entry's venue to a canonical short name.

    Looks at booktitle, then journal, then publisher/series. Returns 'Others'
    when nothing matches and the entry is clearly published, or 'arXiv preprint'
    for preprints.
    """
    raw = ""
    for f in ("booktitle", "journal", "series", "publisher"):
        if entry.get(f):
            raw += " " + entry[f]
    text = raw.lower()
    text = text.replace("{", " ").replace("}", " ")
    text = re.sub(r"\s+", " ", text)
    if not text.strip():
        return "Unknown"
    for canon, patterns in VENUE_PATTERNS:
        for pat in patterns:
            if re.search(pat, text):
                return canon
    return "Others"
