import tempfile
import unittest
from pathlib import Path

from src.analysis.profile_sources import profile


class ProfileTests(unittest.TestCase):
    def test_dates_duplicates_nulls_and_identifiers(self):
        result = profile(
            "data/samples/test_fixture.csv",
            dates=["FECHA"],
            date_format="%d/%m/%Y",
            ids=["CUI"],
            locations=["PROVINCIA"],
            texts=["TEXTO"],
        )
        self.assertEqual(result["rows"], 4)
        self.assertEqual(result["duplicate_rows"], 1)
        self.assertEqual(result["columns"]["CUI"]["null_percent"], 25)
        self.assertEqual(result["columns"]["CUI"]["repeated_nonempty_rows"], 1)
        dates = result["columns"]["FECHA"]["date_profile"]
        self.assertEqual(dates["min"], "2024-02-01")
        self.assertEqual(dates["invalid"], 1)
        self.assertIsNone(result["available_at"])
        self.assertEqual(result["columns"]["TEXTO"]["text_profile"]["url_only_rows"], 1)

    def test_malformed_and_duplicate_headers_fail(self):
        with tempfile.TemporaryDirectory() as folder:
            path = Path(folder) / "test.csv"
            for text in ["a,a\n1,2\n", "a,b\n1\n", ""]:
                path.write_text(text, encoding="utf-8")
                with self.assertRaises(ValueError):
                    profile(path)

    def test_empty_dataset_and_missing_mapping(self):
        with tempfile.TemporaryDirectory() as folder:
            path = Path(folder) / "test.csv"
            path.write_text("CUI\n", encoding="utf-8")
            self.assertEqual(profile(path)["rows"], 0)
            self.assertIsNone(profile(path)["columns"]["CUI"]["null_percent"])
            with self.assertRaises(ValueError):
                profile(path, ids=["unknown"])

    def test_leading_zeros_remain_distinct(self):
        with tempfile.TemporaryDirectory() as folder:
            path = Path(folder) / "test.csv"
            path.write_text("CUI\n001\n1\n", encoding="utf-8")
            self.assertEqual(profile(path, ids=["CUI"])["columns"]["CUI"]["distinct_nonempty"], 2)


if __name__ == "__main__":
    unittest.main()
