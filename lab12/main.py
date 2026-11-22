"""Консольное приложение «План приготовления блюд» (Лабораторная работа №12, вариант 6)."""

import json
from pathlib import Path

from logic import (
    add_record,
    delete_record,
    find_records,
    set_completed,
    statistics,
)
from storage import load_records, save_records


DATA_FILENAME = "data.json"


def format_record(record):
    """Форматирует одну запись о блюде для вывода в консоль."""
    status = "приготовлено" if record["completed"] else "не приготовлено"
    return (
        f"ID {record['id']} | {record['title']} | "
        f"категория: {record['category']} | "
        f"{record['amount']} порц. | статус: {status}"
    )


def show_records(records):
    """Выводит все записи по возрастанию ID или 'Нет записей'."""
    if not records:
        print("Нет записей")
        return
    for record in sorted(records, key=lambda item: item["id"]):
        print(format_record(record))


def prompt_non_empty(prompt_text, error_text):
    """Запрашивает непустую строку с повторным вводом при ошибке."""
    while True:
        value = input(prompt_text).strip()
        if value:
            return value
        print(error_text)


def prompt_non_negative_int(prompt_text):
    """Запрашивает целое неотрицательное число с повторным вводом при ошибке."""
    while True:
        raw = input(prompt_text).strip()
        try:
            value = int(raw)
        except ValueError:
            print("Ошибка: введите целое неотрицательное число.")
            continue
        if value < 0:
            print("Ошибка: количество порций не может быть отрицательным.")
            continue
        return value


def prompt_positive_int(prompt_text):
    """Запрашивает положительный целый ID с повторным вводом при ошибке."""
    while True:
        raw = input(prompt_text).strip()
        try:
            value = int(raw)
        except ValueError:
            print("Ошибка: введите положительное целое число.")
            continue
        if value <= 0:
            print("Ошибка: ID должен быть положительным целым числом.")
            continue
        return value


def handle_add(records):
    """Диалог добавления нового блюда."""
    title = prompt_non_empty(
        "Введите название блюда: ",
        "Ошибка: название блюда не должно быть пустым.",
    )
    category = prompt_non_empty(
        "Введите категорию (например, завтрак, обед, ужин): ",
        "Ошибка: категория не должна быть пустой.",
    )
    amount = prompt_non_negative_int("Введите количество порций (целое >= 0): ")
    record = add_record(records, title, category, amount)
    print(f"Добавлена запись: {format_record(record)}")


def handle_find(records):
    """Диалог поиска блюд по подстроке названия."""
    query = input("Введите подстроку для поиска по названию: ").strip()
    if not query:
        print("Ошибка: поисковый запрос не должен быть пустым.")
        return
    found = find_records(records, query)
    if not found:
        print(f"По запросу '{query}' ничего не найдено.")
        return
    print(f"Найдено записей: {len(found)}")
    for record in found:
        print(format_record(record))


def handle_change_status(records):
    """Диалог явного изменения статуса приготовления по ID."""
    record_id = prompt_positive_int("Введите ID записи: ")
    existing = next((r for r in records if r["id"] == record_id), None)
    if existing is None:
        print(f"Запись с ID {record_id} не найдена. Данные не изменены.")
        return

    print(f"Выбрана запись: {format_record(existing)}")
    while True:
        choice = input(
            "Установить статус (1 — приготовлено, 2 — не приготовлено): "
        ).strip().lower()
        if choice in ("1", "выполнено", "приготовлено"):
            new_status = True
            break
        if choice in ("2", "не выполнено", "не приготовлено"):
            new_status = False
            break
        print("Ошибка: выберите 1 (приготовлено) или 2 (не приготовлено).")

    set_completed(records, record_id, new_status)
    status_text = "приготовлено" if new_status else "не приготовлено"
    print(f"Статус записи с ID {record_id} изменён на «{status_text}».")


def handle_delete(records):
    """Диалог удаления записи по ID с подтверждением 'да'."""
    record_id = prompt_positive_int("Введите ID записи для удаления: ")
    existing = next((r for r in records if r["id"] == record_id), None)
    if existing is None:
        print(f"Запись с ID {record_id} не найдена. Список не изменён.")
        return

    print(f"Найдена запись: {format_record(existing)}")
    confirmation = input(
        "Подтвердите удаление (введите 'да' для удаления): "
    ).strip().lower()
    if confirmation == "да":
        delete_record(records, record_id)
        print(f"Запись с ID {record_id} удалена.")
    else:
        print("Удаление отменено.")


def handle_statistics(records):
    """Вывод статистики по текущему плану приготовления блюд."""
    stats = statistics(records)
    print("Статистика по плану приготовления блюд:")
    print(f"  Всего записей: {stats['total']}")
    print(f"  Приготовлено: {stats['completed']}")
    print(f"  Не приготовлено: {stats['uncompleted']}")
    print(f"  Общее количество порций: {stats['total_amount']}")
    if stats["by_category"]:
        print("  Количество порций по категориям:")
        for category, amount in stats["by_category"].items():
            print(f"    {category}: {amount} порц.")
    else:
        print("  Количество порций по категориям: нет данных")


def handle_save(data_path, records):
    """Сохраняет данные в JSON. Возвращает True при успехе и False при ошибке."""
    try:
        save_records(data_path, records)
    except (OSError, ValueError) as error:
        print(f"Ошибка сохранения данных: {error}")
        return False
    print(f"Данные успешно сохранены в {data_path.name}.")
    return True


def handle_exit(data_path, records):
    """Предлагает сохранить данные перед выходом. Возвращает True для выхода."""
    while True:
        answer = input("Сохранить текущие данные перед выходом? (да/нет): ").strip().lower()
        if answer == "да":
            if handle_save(data_path, records):
                print("Выход из программы.")
                return True
            print("Сохранение не выполнено. Возврат в меню.")
            return False
        if answer == "нет":
            print("Выход без сохранения.")
            return True
        print("Пожалуйста, введите 'да' или 'нет'.")


def print_menu():
    """Выводит консольное меню."""
    print()
    print("=== План приготовления блюд (вариант 6) ===")
    print("1. Показать записи")
    print("2. Добавить запись")
    print("3. Найти записи")
    print("4. Изменить статус")
    print("5. Удалить запись")
    print("6. Показать статистику")
    print("7. Сохранить данные")
    print("8. Выйти")


def main(data_path=None):
    """Точка входа консольной программы."""
    if data_path is None:
        data_path = Path(__file__).resolve().parent / DATA_FILENAME
    else:
        data_path = Path(data_path)

    try:
        records = load_records(data_path)
        print(f"Загружено записей из {data_path.name}: {len(records)}")
    except FileNotFoundError:
        records = []
        print(f"Файл {data_path.name} не найден. Работа начата с пустым списком.")
    except UnicodeError as error:
        print(f"Ошибка кодировки файла {data_path.name}: {error}")
        print("Запуск прекращён. Исходный файл не изменён.")
        return 1
    except json.JSONDecodeError as error:
        print(f"Ошибка синтаксиса JSON в файле {data_path.name}: {error}")
        print("Запуск прекращён. Исходный файл не изменён.")
        return 1
    except ValueError as error:
        print(f"Ошибка структуры данных в файле {data_path.name}: {error}")
        print("Запуск прекращён. Исходный файл не изменён.")
        return 1
    except OSError as error:
        print(f"Ошибка доступа к файлу {data_path.name}: {error}")
        print("Запуск прекращён. Исходный файл не изменён.")
        return 1

    while True:
        print_menu()
        command = input("Выберите команду (1-8): ").strip()

        if command == "1":
            show_records(records)
        elif command == "2":
            handle_add(records)
        elif command == "3":
            handle_find(records)
        elif command == "4":
            handle_change_status(records)
        elif command == "5":
            handle_delete(records)
        elif command == "6":
            handle_statistics(records)
        elif command == "7":
            handle_save(data_path, records)
        elif command == "8":
            if handle_exit(data_path, records):
                return 0
        else:
            print("Неизвестная команда. Введите число от 1 до 8.")


if __name__ == "__main__":
    raise SystemExit(main())
