"""Explicit-column CSV profiling. No inference of historical availability."""

import argparse
import csv
import hashlib
import json
from collections import Counter
from datetime import datetime
from pathlib import Path


def profile(
    path,
    *,
    encoding="utf-8-sig",
    delimiter=",",
    dates=(),
    date_format="%Y-%m-%d",
    ids=(),
    locations=(),
    texts=(),
):
    """Profile the complete input file, preserving identifiers as strings."""
    path = Path(path)
    with path.open(encoding=encoding, newline="") as stream:
        reader = csv.reader(stream, delimiter=delimiter, strict=True)
        header = next(reader, None)
        if not header or any(not h.strip() for h in header):
            raise ValueError("CSV must have a nonempty header")
        if len(header) != len(set(header)):
            raise ValueError("Duplicate column names")
        requested = set(dates) | set(ids) | set(locations) | set(texts)
        missing = requested - set(header)
        if missing:
            raise ValueError(f"Missing requested columns: {sorted(missing)}")
        rows = []
        for line, row in enumerate(reader, 2):
            if len(row) != len(header):
                raise ValueError(f"Row {line}: expected {len(header)} cells")
            rows.append(row)
    count = len(rows)
    columns = {}
    for index, name in enumerate(header):
        values = [row[index] for row in rows]
        present = [value for value in values if value.strip()]
        item = {
            "storage_type": "string",
            "nonempty": len(present),
            "nulls": count - len(present),
            "null_percent": 100 * (count - len(present)) / count if count else None,
            "distinct_nonempty": len(set(present)),
        }
        if name in ids:
            item["semantic_type"] = "identifier_string"
            item["repeated_nonempty_rows"] = len(present) - len(set(present))
        if name in dates:
            valid = []
            for value in present:
                try:
                    valid.append(datetime.strptime(value.strip(), date_format).date())
                except ValueError:
                    pass
            item["date_profile"] = {
                "format": date_format,
                "invalid": len(present) - len(valid),
                "min": str(min(valid)) if valid else None,
                "max": str(max(valid)) if valid else None,
            }
        if name in locations:
            item["location_counts"] = dict(sorted(Counter(present).items()))
        if name in texts:
            lengths = [len(value) for value in present]
            item["text_profile"] = {
                "max_characters": max(lengths, default=0),
                "mean_characters": sum(lengths) / len(lengths) if lengths else None,
                "url_only_rows": sum(
                    value.strip().startswith(("https://", "http://"))
                    and not any(c.isspace() for c in value.strip())
                    for value in present
                ),
                "narrative_sufficiency": "requires manual review",
            }
        columns[name] = item
    return {
        "schema_version": 1,
        "source_file": path.name,
        "sha256": hashlib.sha256(path.read_bytes()).hexdigest(),
        "bytes": path.stat().st_size,
        "rows": count,
        "duplicate_rows": count - len(set(map(tuple, rows))),
        "columns": columns,
        "scope": "complete supplied CSV only; no population coverage inference",
        "null_policy": "empty or whitespace only; other sentinels remain literal",
        "available_at": None,
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("path", type=Path)
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--encoding", default="utf-8-sig")
    parser.add_argument("--delimiter", default=",")
    parser.add_argument("--date", action="append", default=[])
    parser.add_argument("--date-format", default="%Y-%m-%d")
    parser.add_argument("--id", action="append", default=[])
    parser.add_argument("--location", action="append", default=[])
    parser.add_argument("--text", action="append", default=[])
    args = parser.parse_args()
    result = profile(
        args.path,
        encoding=args.encoding,
        delimiter=args.delimiter,
        dates=args.date,
        date_format=args.date_format,
        ids=args.id,
        locations=args.location,
        texts=args.text,
    )
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(
        json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )


if __name__ == "__main__":
    main()
