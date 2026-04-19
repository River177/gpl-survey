#!/usr/bin/env python3
from __future__ import annotations

import hashlib
import random
import shutil
import sqlite3
import string
import time
from pathlib import Path

import requests


ZOTERO_DIR = Path(r"C:\Users\River\Zotero")
DB_PATH = ZOTERO_DIR / "zotero.sqlite"
STORAGE_DIR = ZOTERO_DIR / "storage"
COLLECTION_KEY = "5NAFQLF7"  # GPL/GraphPrompt_new
PDF_CACHE_DIR = Path(r"D:\GPL\gpl-survey\papers\zotero\pdfs\graphprompt_new")

AUTHOR_CREATOR_TYPE_ID = 10
ATTACHMENT_ITEM_TYPE_ID = 3
LINK_MODE_IMPORTED_FILE = 0


TARGET_PAPERS = [
    {
        "title": "HGPROMPT: Bridging Homogeneous and Heterogeneous Graphs for Few-shot Prompt Learning",
        "item_type": "conferencePaper",
        "date": "2024",
        "doi": "10.1609/aaai.v38i15.29596",
        "url": "https://doi.org/10.1609/aaai.v38i15.29596",
        "proceedingsTitle": "Proceedings of the AAAI Conference on Artificial Intelligence",
        "publisher": "Association for the Advancement of Artificial Intelligence (AAAI)",
        "pages": "16578-16586",
        "volume": "38",
        "issue": "15",
        "authors": [
            ("Xingtong", "Yu"),
            ("Yuan", "Fang"),
            ("Zemin", "Liu"),
            ("Xinming", "Zhang"),
        ],
        "pdf_urls": [
            "https://ojs.aaai.org/index.php/AAAI/article/download/29596/31004",
            "https://arxiv.org/pdf/2312.01878.pdf",
        ],
        "pdf_filename": "HGPROMPT-AAAI2024.pdf",
    },
    {
        "title": "Self-Pro: A Self-Prompt and Tuning Framework for Graph Neural Networks",
        "item_type": "conferencePaper",
        "date": "2024",
        "doi": "10.1007/978-3-031-70344-7_12",
        "url": "https://doi.org/10.1007/978-3-031-70344-7_12",
        "proceedingsTitle": "Lecture Notes in Computer Science",
        "publisher": "Springer Nature Switzerland",
        "authors": [
            ("Chenghua", "Gong"),
            ("Xiang", "Li"),
            ("Jianxiang", "Yu"),
            ("Yao", "Cheng"),
            ("Jiaqi", "Tan"),
        ],
        "pdf_urls": [
            "https://link.springer.com/content/pdf/10.1007/978-3-031-70344-7_12",
            "https://arxiv.org/pdf/2310.10362.pdf",
        ],
        "pdf_filename": "Self-Pro-ECMLPKDD2024.pdf",
    },
    {
        "title": "PSP: Pre-Training and Structure Prompt Tuning for Graph Neural Networks",
        "item_type": "conferencePaper",
        "date": "2024",
        "doi": "10.1007/978-3-031-70362-1_25",
        "url": "https://doi.org/10.1007/978-3-031-70362-1_25",
        "proceedingsTitle": "Lecture Notes in Computer Science",
        "publisher": "Springer Nature Switzerland",
        "authors": [
            ("Qingqing", "Ge"),
            ("Zeyuan", "Zhao"),
            ("Yiding", "Liu"),
            ("Anfeng", "Cheng"),
            ("Xiang", "Li"),
        ],
        "pdf_urls": [
            "https://link.springer.com/content/pdf/10.1007/978-3-031-70362-1_25",
            "https://arxiv.org/pdf/2310.17394.pdf",
        ],
        "pdf_filename": "PSP-ECMLPKDD2024.pdf",
    },
    {
        "title": "Edge Prompt Tuning for Graph Neural Networks",
        "local_pdf": Path(r"D:\GPL\gpl-survey\papers\section5-candidates\2503.00750v1.pdf"),
    },
    {
        "title": "Non-Homophilic Graph Pre-Training and Prompt Learning",
        "item_type": "conferencePaper",
        "date": "2025",
        "doi": "10.1145/3690624.3709219",
        "url": "https://doi.org/10.1145/3690624.3709219",
        "proceedingsTitle": "Proceedings of the 31st ACM SIGKDD Conference on Knowledge Discovery and Data Mining",
        "publisher": "ACM",
        "authors": [
            ("Xingtong", "Yu"),
            ("Jie", "Zhang"),
            ("Yuan", "Fang"),
            ("Renhe", "Jiang"),
        ],
        "pdf_urls": [
            "https://arxiv.org/pdf/2408.12594.pdf",
        ],
        "pdf_filename": "ProNoG-KDD2025.pdf",
    },
    {
        "title": "HGMP: Heterogeneous Graph Multi-Task Prompt Learning",
        "item_type": "conferencePaper",
        "date": "2025",
        "doi": "10.24963/ijcai.2025/332",
        "url": "https://doi.org/10.24963/ijcai.2025/332",
        "proceedingsTitle": "Proceedings of the Thirty-Fourth International Joint Conference on Artificial Intelligence",
        "publisher": "IJCAI",
        "pages": "2982-2990",
        "authors": [
            ("Pengfei", "Jiao"),
            ("Jialong", "Ni"),
            ("Di", "Jin"),
            ("Xuan", "Guo"),
            ("Huan", "Liu"),
        ],
        "pdf_urls": [
            "https://www.ijcai.org/proceedings/2025/0332.pdf",
            "https://arxiv.org/pdf/2507.07405.pdf",
        ],
        "pdf_filename": "HGMP-IJCAI2025.pdf",
    },
    {
        "title": "HePa: Heterogeneous Graph Prompting for All-Level Classification Tasks",
        "item_type": "conferencePaper",
        "date": "2025",
        "doi": "10.1609/aaai.v39i11.33297",
        "url": "https://doi.org/10.1609/aaai.v39i11.33297",
        "proceedingsTitle": "Proceedings of the AAAI Conference on Artificial Intelligence",
        "publisher": "Association for the Advancement of Artificial Intelligence (AAAI)",
        "authors": [
            ("Jinghong", "Jia"),
            ("Lei", "Song"),
            ("Jiaxing", "Li"),
            ("Youyong", "Kong"),
        ],
        "pdf_urls": [
            "https://ojs.aaai.org/index.php/AAAI/article/download/33297/35452",
        ],
        "pdf_filename": "HePa-AAAI2025.pdf",
    },
    {
        "title": "SGPT: Few-Shot Prompt Tuning for Signed Graphs",
        "local_pdf": Path(r"D:\GPL\gpl-survey\papers\section5-candidates\2412.12155v2.pdf"),
    },
    {
        "title": "Prompt-Based Spatio-Temporal Graph Transfer Learning",
        "local_pdf": Path(r"D:\GPL\gpl-survey\papers\section5-candidates\2405.12452v2.pdf"),
    },
    {
        "title": "MultiHGPT: Multi-task heterogeneous graph prompt tuning",
        "item_type": "journalArticle",
        "date": "2025",
        "doi": "10.1016/j.ipm.2025.104236",
        "url": "https://doi.org/10.1016/j.ipm.2025.104236",
        "publicationTitle": "Information Processing & Management",
        "publisher": "Elsevier BV",
        "volume": "62",
        "issue": "6",
        "pages": "104236",
        "authors": [
            ("Yifan", "Wang"),
            ("Yixin", "Cao"),
            ("Zeping", "Li"),
            ("Bowen", "Dong"),
            ("Guangnan", "Ye"),
            ("Hongfeng", "Chai"),
        ],
    },
    {
        "title": "One Prompt Fits All: Universal Graph Adaptation for Pretrained Models",
        "local_pdf": Path(r"D:\GPL\gpl-survey\papers\section5-candidates\2509.22416v2.pdf"),
    },
    {
        "title": "MAGPrompt: Message-Adaptive Graph Prompt Tuning for Graph Neural Networks",
        "local_pdf": Path(r"D:\GPL\gpl-survey\papers\section5-candidates\2602.05567v1.pdf"),
    },
    {
        "title": "Unsupervised Prompting for Graph Neural Networks",
        "item_type": "preprint",
        "date": "2025",
        "url": "https://arxiv.org/abs/2505.16903",
        "archiveID": "2505.16903",
        "repository": "arXiv",
        "libraryCatalog": "arXiv",
        "extra": "Primary Class: cs.LG\narXiv: 2505.16903",
        "authors": [
            ("Peyman", "Baghershahi"),
            ("Sourav", "Medya"),
        ],
        "pdf_urls": [
            "https://arxiv.org/pdf/2505.16903.pdf",
        ],
        "pdf_filename": "Unsupervised-Prompting-GNNs-2025.pdf",
    },
    {
        "title": "GP2F: Cross-Domain Graph Prompting with Adaptive Fusion of Pre-trained Graph Neural Networks",
        "local_pdf": Path(r"D:\GPL\gpl-survey\papers\section5-candidates\2602.11629v1.pdf"),
    },
    {
        "title": "Subgraph-level Universal Prompt Tuning",
        "item_type": "journalArticle",
        "date": "2026",
        "doi": "10.1016/j.ins.2026.123516",
        "url": "https://doi.org/10.1016/j.ins.2026.123516",
        "publicationTitle": "Information Sciences",
        "publisher": "Elsevier BV",
        "pages": "123516",
        "authors": [
            ("Junhyun", "Lee"),
            ("Wooseong", "Yang"),
            ("Jaewoo", "Kang"),
        ],
        "pdf_urls": [
            "https://arxiv.org/pdf/2402.10380.pdf",
        ],
        "pdf_filename": "SUPT-2026.pdf",
    },
    {
        "title": "MGP: Integrating pre-training and few-shot node classification via meta graph prompt",
        "item_type": "journalArticle",
        "date": "2026",
        "doi": "10.1016/j.knosys.2025.114876",
        "url": "https://doi.org/10.1016/j.knosys.2025.114876",
        "publicationTitle": "Knowledge-Based Systems",
        "publisher": "Elsevier BV",
        "pages": "114876",
        "authors": [
            ("Zhili", "Qin"),
            ("Zihan", "Mei"),
            ("Jingyi", "Zhou"),
            ("Jiang", "You"),
            ("Jingliang", "Gu"),
            ("Junming", "Shao"),
        ],
        "pdf_urls": [
            "https://papers.ssrn.com/sol3/Delivery.cfm/9bbd35f3-4f10-45da-8b96-11d8431c533f-MECA.pdf?abstractid=5351691&mirid=1",
        ],
        "pdf_filename": "MGP-SSRN-2025.pdf",
    },
    {
        "title": "A Unified Graph Selective Prompt Learning for Graph Neural Networks",
        "local_pdf": Path(r"D:\GPL\gpl-survey\papers\section5-candidates\2406.10498v1.pdf"),
    },
    {
        "title": "CLEAR: Cluster-based Prompt Learning on Heterogeneous Graphs",
        "local_pdf": Path(r"D:\GPL\gpl-survey\papers\section5-candidates\2502.08918v1.pdf"),
    },
    {
        "title": "Heterogeneous Graph Prompt Learning via Adaptive Weight Pruning",
        "item_type": "preprint",
        "date": "2025",
        "url": "https://arxiv.org/abs/2507.09132",
        "archiveID": "2507.09132",
        "repository": "arXiv",
        "libraryCatalog": "arXiv",
        "extra": "Primary Class: cs.LG\narXiv: 2507.09132",
        "authors": [
            ("Chu-Yuan", "Wei"),
            ("Shun-Yao", "Liu"),
            ("Sheng-Da", "Zhuo"),
            ("Chang-Dong", "Wang"),
        ],
        "pdf_urls": [
            "https://arxiv.org/pdf/2507.09132.pdf",
        ],
        "pdf_filename": "HGPrompt-Pruning-2025.pdf",
    },
    {
        "title": "Event-Aware Prompt Learning for Dynamic Graphs",
        "local_pdf": Path(r"D:\GPL\gpl-survey\papers\section5-candidates\2510.11339v1.pdf"),
    },
    {
        "title": "Prompt-Driven Continual Graph Learning",
        "local_pdf": Path(r"D:\GPL\gpl-survey\papers\section5-candidates\2502.06327v1.pdf"),
    },
    {
        "title": "Killing Two Birds with One Stone: Cross-modal Reinforced Prompting for Graph and Language Tasks",
        "item_type": "conferencePaper",
        "date": "2024",
        "doi": "10.1145/3637528.3671742",
        "url": "https://doi.org/10.1145/3637528.3671742",
        "proceedingsTitle": "Proceedings of the 30th ACM SIGKDD Conference on Knowledge Discovery and Data Mining",
        "publisher": "ACM",
        "authors": [
            ("Wenyuan", "Jiang"),
            ("Wenwei", "Wu"),
            ("Le", "Zhang"),
            ("Zixuan", "Yuan"),
            ("Jian", "Xiang"),
        ],
        "pdf_urls": [
            "https://zhoujingbo.github.io/paper/2024KillingKDD.pdf",
        ],
        "pdf_filename": "Killing-Two-Birds-KDD2024.pdf",
    },
]


def now_ts() -> str:
    return time.strftime("%Y-%m-%d %H:%M:%S")


def md5sum(path: Path) -> str:
    h = hashlib.md5()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()


def generate_key(existing: set[str]) -> str:
    alphabet = string.ascii_uppercase + string.digits
    while True:
        key = "".join(random.choice(alphabet) for _ in range(8))
        if key not in existing:
            existing.add(key)
            return key


def ensure_value(cur: sqlite3.Cursor, value: str) -> int:
    row = cur.execute("SELECT valueID FROM itemDataValues WHERE value=?", (value,)).fetchone()
    if row:
        return int(row[0])
    cur.execute("INSERT INTO itemDataValues(value) VALUES (?)", (value,))
    return int(cur.lastrowid)


def ensure_creator(cur: sqlite3.Cursor, first: str, last: str, field_mode: int = 0) -> int:
    row = cur.execute(
        "SELECT creatorID FROM creators WHERE firstName=? AND lastName=? AND fieldMode=?",
        (first, last, field_mode),
    ).fetchone()
    if row:
        return int(row[0])
    cur.execute(
        "INSERT INTO creators(firstName, lastName, fieldMode) VALUES (?, ?, ?)",
        (first, last, field_mode),
    )
    return int(cur.lastrowid)


def field_id_map(cur: sqlite3.Cursor) -> dict[str, int]:
    return {name: int(fid) for fid, name in cur.execute("SELECT fieldID, fieldName FROM fields").fetchall()}


def item_type_id_map(cur: sqlite3.Cursor) -> dict[str, int]:
    return {name: int(iid) for iid, name in cur.execute("SELECT itemTypeID, typeName FROM itemTypes").fetchall()}


def choose_best_existing(cur: sqlite3.Cursor, title: str) -> int | None:
    rows = cur.execute(
        """
        SELECT i.itemID
        FROM items i
        JOIN itemData d ON i.itemID=d.itemID
        JOIN fields f ON d.fieldID=f.fieldID
        JOIN itemDataValues v ON d.valueID=v.valueID
        WHERE i.itemTypeID!=3 AND f.fieldName='title' AND lower(v.value)=lower(?)
        """,
        (title,),
    ).fetchall()
    if not rows:
        return None

    best_item_id = None
    best_score = -1
    for (item_id,) in rows:
        fields = {
            name
            for (name,) in cur.execute(
                """
                SELECT f.fieldName
                FROM itemData d
                JOIN fields f ON d.fieldID=f.fieldID
                WHERE d.itemID=?
                """,
                (item_id,),
            ).fetchall()
        }
        att_count = cur.execute(
            "SELECT COUNT(*) FROM itemAttachments WHERE parentItemID=? AND contentType='application/pdf'",
            (item_id,),
        ).fetchone()[0]
        score = len(fields)
        score += 5 if att_count else 0
        score += 3 if "DOI" in fields else 0
        score += 3 if "proceedingsTitle" in fields or "publicationTitle" in fields else 0
        score += 2 if "abstractNote" in fields else 0
        if score > best_score or (score == best_score and (best_item_id is None or item_id > best_item_id)):
            best_score = score
            best_item_id = int(item_id)
    return best_item_id


def ensure_item_fields(
    cur: sqlite3.Cursor,
    item_id: int,
    metadata: dict,
    fields: dict[str, int],
) -> None:
    skip_keys = {"item_type", "authors", "pdf_urls", "pdf_filename", "local_pdf"}
    for key, value in metadata.items():
        if key in skip_keys or value in (None, ""):
            continue
        if key not in fields:
            continue
        field_id = fields[key]
        exists = cur.execute(
            "SELECT 1 FROM itemData WHERE itemID=? AND fieldID=?",
            (item_id, field_id),
        ).fetchone()
        if exists:
            continue
        value_id = ensure_value(cur, value)
        cur.execute(
            "INSERT INTO itemData(itemID, fieldID, valueID) VALUES (?, ?, ?)",
            (item_id, field_id, value_id),
        )


def ensure_authors(cur: sqlite3.Cursor, item_id: int, authors: list[tuple[str, str]]) -> None:
    existing = cur.execute("SELECT COUNT(*) FROM itemCreators WHERE itemID=?", (item_id,)).fetchone()[0]
    if existing:
        return
    for idx, (first, last) in enumerate(authors):
        creator_id = ensure_creator(cur, first, last)
        cur.execute(
            """
            INSERT INTO itemCreators(itemID, creatorID, creatorTypeID, orderIndex)
            VALUES (?, ?, ?, ?)
            """,
            (item_id, creator_id, AUTHOR_CREATOR_TYPE_ID, idx),
        )


def ensure_collection_item(cur: sqlite3.Cursor, collection_id: int, item_id: int) -> None:
    row = cur.execute(
        "SELECT 1 FROM collectionItems WHERE collectionID=? AND itemID=?",
        (collection_id, item_id),
    ).fetchone()
    if row:
        return
    order_index = cur.execute(
        "SELECT COALESCE(MAX(orderIndex), -1) + 1 FROM collectionItems WHERE collectionID=?",
        (collection_id,),
    ).fetchone()[0]
    cur.execute(
        "INSERT INTO collectionItems(collectionID, itemID, orderIndex) VALUES (?, ?, ?)",
        (collection_id, item_id, int(order_index)),
    )


def download_pdf(urls: list[str], filename: str) -> Path | None:
    PDF_CACHE_DIR.mkdir(parents=True, exist_ok=True)
    dest = PDF_CACHE_DIR / filename
    if dest.exists() and dest.read_bytes()[:5] == b"%PDF-":
        return dest
    headers = {"User-Agent": "Mozilla/5.0"}
    for url in urls:
        try:
            r = requests.get(url, headers=headers, timeout=60, allow_redirects=True)
            if r.ok and r.content[:5] == b"%PDF-":
                dest.write_bytes(r.content)
                return dest
        except Exception:
            continue
    return None


def ensure_pdf_attachment(
    cur: sqlite3.Cursor,
    item_id: int,
    pdf_path: Path | None,
    item_keys: set[str],
) -> tuple[bool, str]:
    existing = cur.execute(
        "SELECT itemID FROM itemAttachments WHERE parentItemID=? AND contentType='application/pdf'",
        (item_id,),
    ).fetchone()
    if existing:
        return True, "already attached"
    if pdf_path is None or not pdf_path.exists():
        return False, "missing pdf"

    max_item_id = int(cur.execute("SELECT COALESCE(MAX(itemID),0) FROM items").fetchone()[0]) + 1
    max_version = int(cur.execute("SELECT COALESCE(MAX(version),0) FROM items").fetchone()[0]) + 1
    item_key = generate_key(item_keys)
    target_dir = STORAGE_DIR / item_key
    target_dir.mkdir(parents=True, exist_ok=False)
    target_name = pdf_path.name
    target_path = target_dir / target_name
    shutil.copy2(pdf_path, target_path)
    stat = target_path.stat()
    storage_mod_time = int(stat.st_mtime * 1000)
    last_processed = int(stat.st_mtime)
    hash_value = md5sum(target_path)
    title_value_id = ensure_value(cur, "PDF")
    title_field_id = 1  # title
    ts = now_ts()

    cur.execute(
        """
        INSERT INTO items(itemID, itemTypeID, dateAdded, dateModified, clientDateModified, libraryID, key, version, synced)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
        """,
        (max_item_id, ATTACHMENT_ITEM_TYPE_ID, ts, ts, ts, 1, item_key, max_version, 1),
    )
    cur.execute(
        """
        INSERT INTO itemAttachments(itemID, parentItemID, linkMode, contentType, charsetID, path, syncState, storageModTime, storageHash, lastProcessedModificationTime)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        """,
        (
            max_item_id,
            item_id,
            LINK_MODE_IMPORTED_FILE,
            "application/pdf",
            None,
            f"storage:{target_name}",
            2,
            storage_mod_time,
            hash_value,
            last_processed,
        ),
    )
    cur.execute(
        "INSERT INTO itemData(itemID, fieldID, valueID) VALUES (?, ?, ?)",
        (max_item_id, title_field_id, title_value_id),
    )
    return True, str(target_path)


def create_item(
    cur: sqlite3.Cursor,
    metadata: dict,
    item_type_ids: dict[str, int],
    fields: dict[str, int],
    item_keys: set[str],
) -> int:
    item_id = int(cur.execute("SELECT COALESCE(MAX(itemID),0) FROM items").fetchone()[0]) + 1
    version = int(cur.execute("SELECT COALESCE(MAX(version),0) FROM items").fetchone()[0]) + 1
    item_key = generate_key(item_keys)
    ts = now_ts()
    cur.execute(
        """
        INSERT INTO items(itemID, itemTypeID, dateAdded, dateModified, clientDateModified, libraryID, key, version, synced)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
        """,
        (item_id, item_type_ids[metadata["item_type"]], ts, ts, ts, 1, item_key, version, 1),
    )
    ensure_item_fields(cur, item_id, metadata, fields)
    ensure_authors(cur, item_id, metadata.get("authors", []))
    return item_id


def main() -> int:
    if not DB_PATH.exists():
        raise SystemExit(f"Missing Zotero DB: {DB_PATH}")

    backup = ZOTERO_DIR / f"zotero.sqlite.graphprompt_new-{int(time.time())}.bak"
    shutil.copy2(DB_PATH, backup)

    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()
    fields = field_id_map(cur)
    item_type_ids = item_type_id_map(cur)
    item_keys = {row[0] for row in cur.execute("SELECT key FROM items").fetchall()}
    collection_row = cur.execute(
        "SELECT collectionID FROM collections WHERE key=?",
        (COLLECTION_KEY,),
    ).fetchone()
    if not collection_row:
        raise SystemExit(f"Missing target collection key: {COLLECTION_KEY}")
    collection_id = int(collection_row[0])

    report = []
    for paper in TARGET_PAPERS:
        title = paper["title"]
        item_id = choose_best_existing(cur, title)
        created = False
        if item_id is None:
            item_id = create_item(cur, paper, item_type_ids, fields, item_keys)
            created = True
        ensure_collection_item(cur, collection_id, item_id)

        pdf_path = None
        if "local_pdf" in paper:
            local_pdf = Path(paper["local_pdf"])
            if local_pdf.exists():
                pdf_path = local_pdf
        elif paper.get("pdf_urls") and paper.get("pdf_filename"):
            pdf_path = download_pdf(paper["pdf_urls"], paper["pdf_filename"])

        attached, attach_info = ensure_pdf_attachment(cur, item_id, pdf_path, item_keys)
        report.append((title, item_id, created, attached, attach_info))

    conn.commit()
    conn.close()

    print(f"Backup: {backup}")
    for title, item_id, created, attached, attach_info in report:
        status = "CREATED" if created else "REUSED"
        pdf_status = "PDF" if attached else "NOPDF"
        print(f"[{status}][{pdf_status}] {item_id} :: {title} :: {attach_info}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
