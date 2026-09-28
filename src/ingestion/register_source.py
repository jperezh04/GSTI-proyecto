"""Register acquisition evidence for an existing, unmodified source file."""

import argparse
import hashlib
import json
from datetime import datetime
from pathlib import Path
from urllib.parse import urlparse


def register(path, *, url, acquired_at, output):
    path, output = Path(path), Path(output)
    stamp = datetime.fromisoformat(acquired_at.replace("Z", "+00:00"))
    if stamp.utcoffset() is None:
        raise ValueError("Acquisition timestamp must include timezone")
    if urlparse(url).scheme not in {"https", "http"} or not urlparse(url).netloc:
        raise ValueError("Use the exact public resource URL")
    digest = hashlib.sha256()
    with path.open("rb") as stream:
        for chunk in iter(lambda: stream.read(1024 * 1024), b""):
            digest.update(chunk)
    result = {
        "source_url": url,
        "file": path.name,
        "acquired_at": stamp.isoformat(),
        "bytes": path.stat().st_size,
        "sha256": digest.hexdigest(),
        "available_at": None,
        "note": "Acquisition time supplied by operator; not historical publication time",
    }
    output.parent.mkdir(parents=True, exist_ok=True)
    with output.open("x", encoding="utf-8") as stream:
        json.dump(result, stream, ensure_ascii=False, indent=2)
        stream.write("\n")
    return result


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("path", type=Path)
    parser.add_argument("--url", required=True)
    parser.add_argument("--acquired-at", required=True)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    register(args.path, url=args.url, acquired_at=args.acquired_at, output=args.output)


if __name__ == "__main__":
    main()
