"""Автоматические тесты бизнес-логики (logic.py)."""

import unittest

from logic import (
    add_record,
    delete_record,
    find_records,
    set_completed,
    statistics,
    validate_records,
)


class TestLogic(unittest.TestCase):
    def test_empty_list_statistics_and_validation(self):
        self.assertEqual(validate_records([]), [])
        stats = statistics([])
        self.assertEqual(
            stats,
            {
                "total": 0,
                "completed": 0,
                "uncompleted": 0,
                "total_amount": 0,
                "by_category": {},
            },
        )

    def test_add_record_trims_and_allows_duplicate_titles(self):
        records = []
        r1 = add_record(records, "  Борщ  ", "  обед  ", 4)
        r2 = add_record(records, "Борщ", "ужин", 2)

        self.assertEqual(r1["id"], 1)
        self.assertEqual(r1["title"], "Борщ")
        self.assertEqual(r1["category"], "обед")
        self.assertEqual(r1["amount"], 4)
        self.assertIs(r1["completed"], False)

        self.assertEqual(r2["id"], 2)
        self.assertEqual(r2["title"], "Борщ")
        self.assertEqual(len(records), 2)

    def test_add_record_invalid_inputs(self):
        records = []
        with self.assertRaises(ValueError):
            add_record(records, "   ", "обед", 2)
        with self.assertRaises(ValueError):
            add_record(records, "Борщ", "", 2)
        with self.assertRaises(ValueError):
            add_record(records, "Борщ", "обед", -1)
        with self.assertRaises(ValueError):
            add_record(records, "Борщ", "обед", True)
        self.assertEqual(records, [])

    def test_validate_strict_types_and_errors(self):
        # Корень не список
        with self.assertRaises(ValueError):
            validate_records({"id": 1})

        # Повторный ID
        with self.assertRaises(ValueError):
            validate_records([
                {"id": 1, "title": "А", "category": "обед", "amount": 1, "completed": False},
                {"id": 1, "title": "Б", "category": "обед", "amount": 2, "completed": True},
            ])

        # id=True (bool вместо int)
        with self.assertRaises(ValueError):
            validate_records([
                {"id": True, "title": "А", "category": "обед", "amount": 1, "completed": False},
            ])

        # amount=False (bool вместо int)
        with self.assertRaises(ValueError):
            validate_records([
                {"id": 1, "title": "А", "category": "обед", "amount": False, "completed": False},
            ])

        # amount < 0
        with self.assertRaises(ValueError):
            validate_records([
                {"id": 1, "title": "А", "category": "обед", "amount": -1, "completed": False},
            ])

        # completed не bool
        with self.assertRaises(ValueError):
            validate_records([
                {"id": 1, "title": "А", "category": "обед", "amount": 1, "completed": "false"},
            ])

        # Отсутствует обязательный ключ
        with self.assertRaises(ValueError):
            validate_records([
                {"id": 1, "title": "А", "amount": 1, "completed": False},
            ])

        # Дополнительные ключи допускаются
        extra = [
            {
                "id": 1,
                "title": "Борщ",
                "category": "обед",
                "amount": 0,
                "completed": False,
                "note": "без мяса",
            }
        ]
        self.assertEqual(validate_records(extra), extra)

    def test_find_records_case_insensitive_and_immutable(self):
        records = [
            {"id": 2, "title": "Паста карбонара", "category": "обед", "amount": 4, "completed": False},
            {"id": 1, "title": "Python-пирог", "category": "десерт", "amount": 6, "completed": True},
        ]
        snapshot = [dict(r) for r in records]

        found = find_records(records, "PY")
        self.assertEqual([r["id"] for r in found], [1])

        found_ru = find_records(records, "ПАСТА")
        self.assertEqual([r["id"] for r in found_ru], [2])

        # Изменение результата поиска не меняет исходный список
        found[0]["title"] = "Изменено"
        self.assertEqual(records, snapshot)

        # Пустой запрос отклоняется
        with self.assertRaises(ValueError):
            find_records(records, "   ")

    def test_set_completed_and_unknown_id(self):
        records = [
            {"id": 1, "title": "Борщ", "category": "обед", "amount": 4, "completed": False},
        ]
        self.assertTrue(set_completed(records, 1, True))
        self.assertIs(records[0]["completed"], True)

        self.assertTrue(set_completed(records, 1, False))
        self.assertIs(records[0]["completed"], False)

        # Неизвестный ID
        self.assertFalse(set_completed(records, 99, True))
        self.assertIs(records[0]["completed"], False)

    def test_delete_record_and_id_not_renumbered(self):
        records = []
        add_record(records, "Блюдо 1", "обед", 4)
        add_record(records, "Блюдо 2", "обед", 2)

        self.assertFalse(delete_record(records, 999))
        self.assertTrue(delete_record(records, 1))
        self.assertEqual([r["id"] for r in records], [2])

        r3 = add_record(records, "Блюдо 3", "ужин", 3)
        self.assertEqual(r3["id"], 3)
        self.assertEqual([r["id"] for r in records], [2, 3])

    def test_statistics_two_categories_alphabetical(self):
        records = [
            {"id": 1, "title": "Борщ", "category": "обед", "amount": 6, "completed": True},
            {"id": 2, "title": "Омлет", "category": "завтрак", "amount": 2, "completed": True},
            {"id": 3, "title": "Паста", "category": "обед", "amount": 4, "completed": False},
            {"id": 4, "title": "Сырники", "category": "завтрак", "amount": 3, "completed": False},
        ]
        snapshot = [dict(r) for r in records]
        stats = statistics(records)

        self.assertEqual(stats["total"], 4)
        self.assertEqual(stats["completed"], 2)
        self.assertEqual(stats["uncompleted"], 2)
        self.assertEqual(stats["total_amount"], 15)
        self.assertEqual(list(stats["by_category"].items()), [("завтрак", 5), ("обед", 10)])
        self.assertEqual(records, snapshot)


if __name__ == "__main__":
    unittest.main()
