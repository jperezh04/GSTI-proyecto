import hashlib
import tempfile
import unittest
from pathlib import Path

from src.ingestion.register_source import register


class ManifestTests(unittest.TestCase):
    def test_hash_and_no_overwrite(self):
        with tempfile.TemporaryDirectory() as folder:
            path = Path(folder) / "source.csv"
            path.write_bytes(b"CUI\n001\n")
            output = Path(folder) / "manifest.json"
            args = dict(
                url="https://example.invalid/source.csv",
                acquired_at="2026-09-28T00:00:00Z",
                output=output,
            )
            result = register(path, **args)
            self.assertEqual(result["sha256"], hashlib.sha256(path.read_bytes()).hexdigest())
            self.assertIsNone(result["available_at"])
            with self.assertRaises(FileExistsError):
                register(path, **args)

    def test_rejects_naive_time(self):
        with self.assertRaises(ValueError):
            register(
                "unused",
                url="https://example.invalid/data",
                acquired_at="2026-09-28T00:00:00",
                output="unused",
            )
