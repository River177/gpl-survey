#!/usr/bin/env python3
"""Attach downloaded PDFs to Zotero items by matching BibTeX titles."""

from __future__ import annotations

import argparse
import hashlib
import os
import random
import re
import shutil
import sqlite3
import string
import time
import unicodedata
from pathlib import Path


TITLE_VALUE = "PDF"
ATTACHMENT_ITEM_TYPE_ID = 3
LINK_MODE_IMPORTED_FILE = 0


def clean_title(raw: str) -> str:
    text = raw.replace("\n", " ").replace("\t", " ")
    text = re.sub(r"[{}]", "", text)
    text = re.sub(r"\\[a-zA-Z]+\s*", "", text)
    text = text.replace("\\&", "&")
    return re.sub(r"\s+", " ", text).strip()


def normalize_title(title: str) -> str:
    title = clean_title(title)
    title = unicodedata.normalize("NFKD", title).encode("ascii", "ignore").decode("ascii")
    title = title.lower()
    title = re.sub(r"[^a-z0-9]+", " ", title)
    return re.sub(r"\s+", " ", title).strip()


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


def parse_bib_titles(path: Path) -> list[tuple[str, str]]:
    text = path.read_text(encoding="utf-8")
    entries: list[tuple[str, str]] = []
    idx = 0
    while True:
        at = text.find("@", idx)
        if at == -1:
            break
        brace = text.find("{", at)
        if brace == -1:
            break
        depth = 1
        end = brace + 1
        while end < len(text) and depth > 0:
            if text[end] == "{":
                depth += 1
            elif text[end] == "}":
                depth -= 1
            end += 1
        body = text[brace + 1 : end - 1].strip()
        idx = end
        comma = body.find(",")
        if comma == -1:
            continue
        key = body[:comma].strip()
        fields = parse_fields(body[comma + 1 :])
        title = fields.get("title")
        if title:
            entries.append((key, title))
    return entries


def generate_key(existing: set[str]) -> str:
    alphabet = string.ascii_uppercase + string.digits
    while True:
        key = "".join(random.choice(alphabet) for _ in range(8))
        if key not in existing:
            existing.add(key)
            return key


def is_pdf(path: Path) -> bool:
    return path.exists() and path.read_bytes()[:5] == b"%PDF-"


def md5sum(path: Path) -> str:
    digest = hashlib.md5()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def get_title_field_id(cur: sqlite3.Cursor) -> int:
    row = cur.execute("SELECT fieldID FROM fields WHERE fieldName='title'").fetchone()
    if not row:
        raise RuntimeError("Could not find Zotero title field")
    return int(row[0])


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--bib", type=Path, required=True)
    parser.add_argument("--pdf-dir", type=Path, required=True)
    parser.add_argument("--zotero-dir", type=Path, required=True)
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args()

    db_path = args.zotero_dir / "zotero.sqlite"
    storage_dir = args.zotero_dir / "storage"
    if not db_path.exists():
        raise SystemExit(f"Missing Zotero DB: {db_path}")

    bib_titles = parse_bib_titles(args.bib)
    pdfs = {path.stem: path for path in args.pdf_dir.glob("*.pdf") if is_pdf(path)}

    conn = sqlite3.connect(db_path)
    conn.row_factory = sqlite3.Row
    cur = conn.cursor()

    title_field_id = get_title_field_id(cur)
    title_value_row = cur.execute("SELECT valueID FROM itemDataValues WHERE value=?", (TITLE_VALUE,)).fetchone()
    if title_value_row:
        title_value_id = int(title_value_row[0])
    else:
        cur.execute("INSERT INTO itemDataValues(value) VALUES (?)", (TITLE_VALUE,))
        title_value_id = int(cur.lastrowid)

    rows = cur.execute(
        """
        SELECT i.itemID, i.key, i.libraryID, i.version, i.synced, v.value AS title
        FROM items i
        JOIN itemData d ON i.itemID=d.itemID
        JOIN fields f ON d.fieldID=f.fieldID
        JOIN itemDataValues v ON d.valueID=v.valueID
        WHERE f.fieldName='title'
        """
    ).fetchall()
    by_title: dict[str, list[sqlite3.Row]] = {}
    for row in rows:
        by_title.setdefault(normalize_title(row["title"]), []).append(row)

    existing_attachment_parents = {
        int(row[0])
        for row in cur.execute(
            "SELECT parentItemID FROM itemAttachments WHERE parentItemID IS NOT NULL AND contentType='application/pdf'"
        ).fetchall()
    }
    existing_item_keys = {str(row[0]) for row in cur.execute("SELECT key FROM items").fetchall()}

    matched: list[tuple[str, Path, sqlite3.Row]] = []
    missing: list[str] = []
    ambiguous: list[str] = []
    resolved_multi: list[str] = []
    skipped_existing: list[str] = []

    for bib_key, bib_title in bib_titles:
        pdf_path = pdfs.get(bib_key)
        if not pdf_path:
            continue
        candidates = by_title.get(normalize_title(bib_title), [])
        if len(candidates) == 0:
            missing.append(bib_key)
            continue
        if len(candidates) > 1:
            candidates = sorted(candidates, key=lambda row: int(row["itemID"]))
            parent = candidates[-1]
            resolved_multi.append(bib_key)
            if len({int(row["itemID"]) for row in candidates}) > 2:
                ambiguous.append(bib_key)
        else:
            parent = candidates[0]
        if int(parent["itemID"]) in existing_attachment_parents:
            skipped_existing.append(bib_key)
            continue
        matched.append((bib_key, pdf_path, parent))

    print(f"PDFs available: {len(pdfs)}")
    print(f"Attachable matches: {len(matched)}")
    print(f"Already attached: {len(skipped_existing)}")
    print(f"No Zotero title match: {len(missing)}")
    if missing[:10]:
        print(f"Missing title matches: {missing[:10]}")
    print(f"Resolved duplicate-title matches: {len(resolved_multi)}")
    print(f"Ambiguous matches kept for review: {len(ambiguous)}")
    unattached_keys = [bib_key for bib_key, _, parent in matched if int(parent["itemID"]) not in existing_attachment_parents]
    if unattached_keys[:10]:
        print(f"Unattached keys: {unattached_keys[:10]}")
    if resolved_multi[:5]:
        print("Resolved samples:")
        for bib_key in resolved_multi[:5]:
            title = next(title for key, title in bib_titles if key == bib_key)
            candidates = by_title.get(normalize_title(title), [])
            print(f"  {bib_key}: chose {int(sorted(candidates, key=lambda row: int(row['itemID']))[-1]['itemID'])} from {[int(row['itemID']) for row in candidates[:5]]}")
    if args.dry_run:
        return 0

    backup_path = args.zotero_dir / f"zotero.sqlite.attach-backup-{int(time.time())}.bak"
    shutil.copy2(db_path, backup_path)
    print(f"Database backup: {backup_path}")

    max_item_id = int(cur.execute("SELECT COALESCE(MAX(itemID), 0) FROM items").fetchone()[0])
    max_version = int(cur.execute("SELECT COALESCE(MAX(version), 0) FROM items").fetchone()[0])

    now_ms = int(time.time() * 1000)
    now_ts = time.strftime("%Y-%m-%d %H:%M:%S")
    attached_count = 0

    for bib_key, pdf_path, parent in matched:
        max_item_id += 1
        max_version += 1
        item_id = max_item_id
        item_key = generate_key(existing_item_keys)
        target_dir = storage_dir / item_key
        target_dir.mkdir(parents=True, exist_ok=False)
        target_name = pdf_path.name
        target_path = target_dir / target_name
        shutil.copy2(pdf_path, target_path)
        stat = target_path.stat()
        storage_mod_time = int(stat.st_mtime * 1000)
        last_processed = int(stat.st_mtime)
        hash_value = md5sum(target_path)
        library_id = int(parent["libraryID"])

        cur.execute(
            """
            INSERT INTO items(itemID, itemTypeID, dateAdded, dateModified, clientDateModified, libraryID, key, version, synced)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
            """,
            (item_id, ATTACHMENT_ITEM_TYPE_ID, now_ts, now_ts, now_ts, library_id, item_key, max_version, 1),
        )
        cur.execute(
            """
            INSERT INTO itemAttachments(itemID, parentItemID, linkMode, contentType, charsetID, path, syncState, storageModTime, storageHash, lastProcessedModificationTime)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            """,
            (
                item_id,
                int(parent["itemID"]),
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
            (item_id, title_field_id, title_value_id),
        )
        attached_count += 1

    conn.commit()
    print(f"Created attachments: {attached_count}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
