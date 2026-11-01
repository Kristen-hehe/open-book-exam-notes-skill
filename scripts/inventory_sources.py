#!/usr/bin/env python3
"""Create a read-only JSON manifest for mixed course-material folders."""

from __future__ import annotations

import argparse
import csv
import hashlib
import json
import zipfile
from pathlib import Path
from xml.etree import ElementTree as ET


SUPPORTED = {'.csv', '.docx', '.ods', '.ows', '.pdf', '.pptx', '.tsv', '.xls', '.xlsx'}


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open('rb') as stream:
        for block in iter(lambda: stream.read(1024 * 1024), b''):
            digest.update(block)
    return digest.hexdigest()


def zip_counts(path: Path) -> dict[str, int]:
    result: dict[str, int] = {}
    try:
        with zipfile.ZipFile(path) as archive:
            names = archive.namelist()
            if path.suffix.lower() == '.docx':
                result['embedded_media'] = sum(n.startswith('word/media/') for n in names)
                xml = archive.read('word/document.xml')
                root = ET.fromstring(xml)
                ns = {'w': 'http://schemas.openxmlformats.org/wordprocessingml/2006/main'}
                result['paragraphs'] = len(root.findall('.//w:p', ns))
                result['tables'] = len(root.findall('.//w:tbl', ns))
            elif path.suffix.lower() == '.pptx':
                result['slides'] = sum(
                    n.startswith('ppt/slides/slide') and n.endswith('.xml') for n in names
                )
                result['embedded_media'] = sum(n.startswith('ppt/media/') for n in names)
            elif path.suffix.lower() == '.xlsx':
                result['worksheets'] = sum(
                    n.startswith('xl/worksheets/sheet') and n.endswith('.xml') for n in names
                )
    except (KeyError, ET.ParseError, zipfile.BadZipFile):
        result['container_warning'] = 1
    return result


def delimited_shape(path: Path) -> dict[str, int]:
    delimiter = '\t' if path.suffix.lower() == '.tsv' else ','
    rows = 0
    columns = 0
    try:
        with path.open('r', encoding='utf-8-sig', errors='replace', newline='') as stream:
            reader = csv.reader(stream, delimiter=delimiter)
            for row in reader:
                rows += 1
                columns = max(columns, len(row))
    except OSError:
        return {'read_warning': 1}
    return {'rows_including_header': rows, 'max_columns': columns}


def describe(path: Path, root: Path) -> dict[str, object]:
    suffix = path.suffix.lower()
    item: dict[str, object] = {
        'path': str(path.relative_to(root)),
        'extension': suffix,
        'bytes': path.stat().st_size,
        'sha256': sha256(path),
    }
    if suffix in {'.docx', '.pptx', '.xlsx'}:
        item['structure'] = zip_counts(path)
    elif suffix in {'.csv', '.tsv'}:
        item['structure'] = delimited_shape(path)
    return item


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('source', type=Path, help='Course file or folder to inventory')
    parser.add_argument('--output', type=Path, help='Write JSON here; stdout when omitted')
    args = parser.parse_args()

    source = args.source.expanduser().resolve()
    if not source.exists():
        parser.error(f'source does not exist: {source}')

    root = source if source.is_dir() else source.parent
    candidates = [source] if source.is_file() else sorted(p for p in source.rglob('*') if p.is_file())
    files = [describe(p, root) for p in candidates if p.suffix.lower() in SUPPORTED and not p.name.startswith('.')]
    payload = {
        'source_root': str(root),
        'file_count': len(files),
        'total_bytes': sum(int(item['bytes']) for item in files),
        'files': files,
    }
    rendered = json.dumps(payload, indent=2, ensure_ascii=False)
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(rendered + '\n', encoding='utf-8')
    else:
        print(rendered)
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
