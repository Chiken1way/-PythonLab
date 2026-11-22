"""Автоматические тесты чтения и записи JSON (storage.py)."""

import json
import tempfile
import unittest
from pathlib import Path

from storage import load_records, save_records


class TestStorage(unittest.TestCase):
    def test_save_and_reload_in_temp_dir(self):
        records = [
            {
                "id": 1,
                "title": "Борщ",
                "category": "обед",
                "amount": 6,
                "completed": True,
                "extra": "доп. поле",
            },
            {
                "id": 2,
                "title": "Сырники",
                "category": "завтрак",
                "amount": 3,
                "completed": False,
            },
        ]

        with tempfile.TemporaryDirectory() as tmpdir:
            file_path = Path(tmpdir) / "data.json"
            save_records(file_path, records)

            raw_text = file_path.read_text(encoding="utf-8")
            self.assertIn("Борщ", raw_text)

            reloaded = load_records(file_path)
            self.assertEqual(reloaded, records)

    def test_missing_file_raises_file_not_found(self):
        with tempfile.TemporaryDirectory() as tmpdir:
            missing_path = Path(tmpdir) / "missing.json"
            with self.assertRaises(FileNotFoundError):
                load_records(missing_path)

    def test_corrupted_json_raises_and_file_unchanged(self):
        broken_content = '[{"id": 1, "title": '
        with tempfile.TemporaryDirectory() as tmpdir:
            file_path = Path(tmpdir) / "broken.json"
            file_path.write_text(broken_content, encoding="utf-8")

            with self.assertRaises(json.JSONDecodeError):
                load_records(file_path)

            self.assertEqual(file_path.read_text(encoding="utf-8"), broken_content)

    def test_invalid_structure_raises_value_error(self):
        invalid_data = [
            {"id": 1, "title": "Борщ", "category": "обед", "amount": 4, "completed": True},
            {"id": 1, "title": "Суп", "category": "обед", "amount": 2, "completed": False},
        ]
        with tempfile.TemporaryDirectory() as tmpdir:
            file_path = Path(tmpdir) / "dup.json"
            raw = json.dumps(invalid_data, ensure_ascii=False)
            file_path.write_text(raw, encoding="utf-8")

            with self.assertRaises(ValueError):
                load_records(file_path)

            self.assertEqual(file_path.read_text(encoding="utf-8"), raw)


if __name__ == "__main__":
    unittest.main()
