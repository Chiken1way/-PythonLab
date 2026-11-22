"""Модуль валидации и анализа списка задач (todos)."""

import json
from pathlib import Path


def validate_todos(data):
    """Проверяет структуру списка задач.

    Корень должен быть списком, каждая запись — словарём с положительными
    целыми id и userId, непустой строкой title и логическим completed.
    Поле id должно быть уникальным. Дополнительные ключи допустимы.
    При нарушении выбрасывает ValueError.
    """
    if not isinstance(data, list):
        raise ValueError("Корневой элемент JSON должен быть списком")

    seen_ids = set()

    for index, item in enumerate(data):
        if not isinstance(item, dict):
            raise ValueError(f"Запись с индексом {index} должна быть словарём")

        if "id" not in item:
            raise ValueError(f"В записи с индексом {index} отсутствует поле 'id'")
        task_id = item["id"]
        if type(task_id) is not int or task_id <= 0:
            raise ValueError(
                f"Поле 'id' в записи с индексом {index} должно быть положительным целым числом"
            )
        if task_id in seen_ids:
            raise ValueError(f"Обнаружен повторяющийся 'id': {task_id}")
        seen_ids.add(task_id)

        if "userId" not in item:
            raise ValueError(f"В записи с индексом {index} отсутствует поле 'userId'")
        user_id = item["userId"]
        if type(user_id) is not int or user_id <= 0:
            raise ValueError(
                f"Поле 'userId' в записи с индексом {index} должно быть положительным целым числом"
            )

        if "title" not in item:
            raise ValueError(f"В записи с индексом {index} отсутствует поле 'title'")
        title = item["title"]
        if not isinstance(title, str) or not title.strip():
            raise ValueError(
                f"Поле 'title' в записи с индексом {index} должно быть непустой строкой"
            )

        if "completed" not in item:
            raise ValueError(f"В записи с индексом {index} отсутствует поле 'completed'")
        completed = item["completed"]
        if type(completed) is not bool:
            raise ValueError(
                f"Поле 'completed' в записи с индексом {index} должно быть логическим значением"
            )

    return data


def completion_counts(todos):
    """Возвращает словарь {userId: количество завершённых задач} для всех пользователей."""
    counts = {}
    for task in todos:
        user_id = task["userId"]
        if user_id not in counts:
            counts[user_id] = 0
        if task["completed"]:
            counts[user_id] += 1
    return counts


def top_users(counts):
    """Возвращает отсортированный список userId с максимумом завершённых задач.

    Для пустого словаря или максимума 0 возвращает [].
    """
    if not counts:
        return []
    max_completed = max(counts.values())
    if max_completed == 0:
        return []
    return sorted(user_id for user_id, count in counts.items() if count == max_completed)


def leader_completed_tasks(todos, leaders):
    """Отбирает завершённые задачи пользователей-лидеров с сохранением порядка."""
    leader_set = set(leaders)
    return [
        dict(task)
        for task in todos
        if task["userId"] in leader_set and task["completed"]
    ]


def load_todos(path):
    """Загружает и проверяет список задач из JSON-файла."""
    file_path = Path(path)
    with open(file_path, "r", encoding="utf-8") as file:
        data = json.load(file)
    return validate_todos(data)


def save_json(path, data):
    """Сохраняет данные в JSON-файл в кодировке UTF-8 с отступом 2."""
    file_path = Path(path)
    with open(file_path, "w", encoding="utf-8") as file:
        json.dump(data, file, ensure_ascii=False, indent=2)
