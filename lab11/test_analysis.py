"""Автоматические тесты для лабораторной работы №11 (без сетевых вызовов)."""

import json
import tempfile
import unittest
from pathlib import Path

from analysis import (
    completion_counts,
    leader_completed_tasks,
    load_todos,
    save_json,
    top_users,
    validate_todos,
)
from variant6 import select_tasks


SAMPLE_TODOS = [
    {"id": 1, "userId": 5, "title": "Ввод", "completed": True},
    {"id": 2, "userId": 5, "title": "Циклы", "completed": False},
    {"id": 3, "userId": 10, "title": "Строки", "completed": True},
    {"id": 4, "userId": 10, "title": "Файлы", "completed": True},
    {"id": 5, "userId": 5, "title": "Списки", "completed": True},
]


class TestAnalysis(unittest.TestCase):
    def test_sample_dataset(self):
        validated = validate_todos(SAMPLE_TODOS)
        counts = completion_counts(validated)
        self.assertEqual(counts, {5: 2, 10: 2})

        leaders = top_users(counts)
        self.assertEqual(leaders, [5, 10])

        selected_leaders = leader_completed_tasks(validated, leaders)
        self.assertEqual([t["id"] for t in selected_leaders], [1, 3, 4, 5])

    def test_empty_and_all_false(self):
        self.assertEqual(completion_counts([]), {})
        self.assertEqual(top_users({}), [])
        self.assertEqual(leader_completed_tasks([], []), [])

        only_false = [
            {"id": 1, "userId": 2, "title": "Задача 1", "completed": False},
            {"id": 2, "userId": 3, "title": "Задача 2", "completed": False},
        ]
        counts = completion_counts(only_false)
        self.assertEqual(counts, {2: 0, 3: 0})
        leaders = top_users(counts)
        self.assertEqual(leaders, [])
        self.assertEqual(leader_completed_tasks(only_false, leaders), [])

    def test_single_and_multiple_leaders(self):
        single = [
            {"id": 1, "userId": 1, "title": "A", "completed": True},
            {"id": 2, "userId": 1, "title": "B", "completed": True},
            {"id": 3, "userId": 2, "title": "C", "completed": True},
            {"id": 4, "userId": 3, "title": "D", "completed": False},
        ]
        counts = completion_counts(single)
        self.assertEqual(counts, {1: 2, 2: 1, 3: 0})
        self.assertEqual(top_users(counts), [1])

        tie = [
            {"id": 1, "userId": 20, "title": "A", "completed": True},
            {"id": 2, "userId": 3, "title": "B", "completed": True},
            {"id": 3, "userId": 10, "title": "C", "completed": False},
        ]
        tie_counts = completion_counts(tie)
        self.assertEqual(tie_counts, {20: 1, 3: 1, 10: 0})
        # Числовая сортировка: 3 < 20 (строковая дала бы '20' < '3')
        self.assertEqual(top_users(tie_counts), [3, 20])

    def test_variant6_select_tasks(self):
        # Результат по таблице при user_id=5 -> [2]
        result = select_tasks(SAMPLE_TODOS, 5)
        self.assertEqual([t["id"] for t in result], [2])

        # Неизвестный пользователь -> []
        self.assertEqual(select_tasks(SAMPLE_TODOS, 999), [])

        # Непустой набор без совпадений (у пользователя 7 только нечётные id)
        odd_only = [
            {"id": 1, "userId": 7, "title": "Раз", "completed": True},
            {"id": 3, "userId": 7, "title": "Три", "completed": False},
        ]
        self.assertEqual(select_tasks(odd_only, 7), [])

        # Исходные записи не изменяются
        snapshot = [dict(t) for t in SAMPLE_TODOS]
        selected = select_tasks(SAMPLE_TODOS, 5)
        selected[0]["title"] = "Изменено"
        self.assertEqual(SAMPLE_TODOS, snapshot)

    def test_validation_errors(self):
        # Вместо списка передан объект
        with self.assertRaises(ValueError):
            validate_todos({"id": 1, "userId": 5, "title": "A", "completed": True})

        # Повторный id
        with self.assertRaises(ValueError):
            validate_todos([
                {"id": 1, "userId": 5, "title": "A", "completed": True},
                {"id": 1, "userId": 6, "title": "B", "completed": False},
            ])

        # Отсутствующий userId
        with self.assertRaises(ValueError):
            validate_todos([
                {"id": 1, "title": "A", "completed": True},
            ])

        # completed="false" (строка вместо bool)
        with self.assertRaises(ValueError):
            validate_todos([
                {"id": 1, "userId": 5, "title": "A", "completed": "false"},
            ])

        # id=True (bool вместо int)
        with self.assertRaises(ValueError):
            validate_todos([
                {"id": True, "userId": 5, "title": "A", "completed": True},
            ])

        # Дополнительные ключи допустимы
        with_extra = [
            {"id": 1, "userId": 5, "title": "A", "completed": True, "priority": "high"}
        ]
        self.assertEqual(validate_todos(with_extra), with_extra)

    def test_json_roundtrip(self):
        leaders = top_users(completion_counts(SAMPLE_TODOS))
        leader_tasks = leader_completed_tasks(SAMPLE_TODOS, leaders)

        with tempfile.TemporaryDirectory() as tmpdir:
            file_path = Path(tmpdir) / "roundtrip.json"
            save_json(file_path, leader_tasks)
            restored = load_todos(file_path)
            self.assertEqual(restored, leader_tasks)

            # Проверка, что кириллица записана читаемо (ensure_ascii=False)
            raw_text = file_path.read_text(encoding="utf-8")
            self.assertIn("Ввод", raw_text)


if __name__ == "__main__":
    unittest.main()
