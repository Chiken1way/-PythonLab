"""Основной скрипт лабораторной работы №11: анализ todos.json и сохранение leaders.json."""

import json
from pathlib import Path

from analysis import (
    completion_counts,
    leader_completed_tasks,
    load_todos,
    save_json,
    top_users,
)


def main():
    base_dir = Path(__file__).resolve().parent
    input_path = base_dir / "todos.json"
    leaders_path = base_dir / "leaders.json"

    try:
        todos = load_todos(input_path)
    except FileNotFoundError:
        print(f"Ошибка: файл не найден ({input_path})")
        return
    except UnicodeError as error:
        print(f"Ошибка кодировки файла: {error}")
        return
    except json.JSONDecodeError as error:
        print(f"Ошибка синтаксиса JSON: {error}")
        return
    except ValueError as error:
        print(f"Ошибка структуры данных: {error}")
        return
    except OSError as error:
        print(f"Ошибка доступа к файлу: {error}")
        return

    counts = completion_counts(todos)
    leaders = top_users(counts)
    leader_tasks = leader_completed_tasks(todos, leaders)

    try:
        save_json(leaders_path, leader_tasks)
    except OSError as error:
        print(f"Ошибка записи файла {leaders_path}: {error}")
        return

    print(f"Всего задач: {len(todos)}")
    print("Завершённые задачи по пользователям:")
    for user_id in sorted(counts):
        print(f"  Пользователь {user_id}: {counts[user_id]}")

    if leaders:
        leaders_str = ", ".join(str(uid) for uid in leaders)
        print(f"Лидеры по завершённым задачам: {leaders_str}")
    else:
        print("Лидеры по завершённым задачам: нет")

    task_ids = [task["id"] for task in leader_tasks]
    print(f"Сохранено задач лидеров в {leaders_path.name}: {len(leader_tasks)} (id: {task_ids})")


if __name__ == "__main__":
    main()
