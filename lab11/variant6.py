"""Индивидуальный вариант №6: задачи указанного пользователя с чётным id."""

import json
from pathlib import Path

from analysis import load_todos, save_json


def select_tasks(todos, user_id, parameter=None):
    """Отбирает задачи пользователя user_id с чётным id (вариант 6).

    Дополнительный параметр не используется (parameter=None).
    Порядок записей сохраняется, исходные записи не изменяются.
    Для неизвестного пользователя возвращает пустой список.
    """
    return [
        dict(task)
        for task in todos
        if task["userId"] == user_id and task["id"] % 2 == 0
    ]


def prompt_user_id():
    """Запрашивает положительный целый user_id с повторным вводом при ошибке."""
    while True:
        raw = input("Введите положительный целый user_id: ").strip()
        try:
            value = int(raw)
        except ValueError:
            print("Ошибка: введите целое число.")
            continue
        if value <= 0:
            print("Ошибка: user_id должен быть положительным целым числом.")
            continue
        return value


def main():
    base_dir = Path(__file__).resolve().parent
    input_path = base_dir / "todos.json"
    output_path = base_dir / "selected.json"

    try:
        todos = load_todos(input_path)
    except FileNotFoundError:
        print(f"Ошибка: файл не найден ({input_path})")
        return
    except UnicodeError as error:
        print(f"Ошибка кодировки файла: {error}")
        return
    except json.JSONDecodeError as error:
        print(f"Ошибка разбора JSON: {error}")
        return
    except ValueError as error:
        print(f"Ошибка структуры данных: {error}")
        return
    except OSError as error:
        print(f"Ошибка доступа к файлу: {error}")
        return

    user_id = prompt_user_id()
    selected = select_tasks(todos, user_id)

    try:
        save_json(output_path, selected)
    except OSError as error:
        print(f"Ошибка сохранения файла {output_path}: {error}")
        return

    selected_ids = [task["id"] for task in selected]
    print(f"Вариант 6 (чётный id) для user_id={user_id}: найдено задач — {len(selected)}")
    print(f"Идентификаторы отобранных задач: {selected_ids}")
    print(f"Результат сохранён в {output_path.name}")


if __name__ == "__main__":
    main()
