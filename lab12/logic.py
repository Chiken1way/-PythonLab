"""Бизнес-логика проекта «План приготовления блюд» (вариант 6).

Модуль не использует изменяемые глобальные переменные и не выполняет
ввод-вывод в консоль или файлы.
"""


def validate_records(records):
    """Проверяет корректность списка записей о блюдах.

    Контракт:
    - Не изменяет переданный список.
    - Возвращает переданный список при успешной проверке.
    - Выбрасывает ValueError с пояснением при любом нарушении формата.

    Правила:
    - Корень — list, каждый элемент — dict.
    - Обязательные ключи: id, title, category, amount, completed.
    - Дополнительные ключи допускаются и сохраняются без обработки.
    - id: положительное целое (type is int, > 0), уникальное в списке.
    - title, category: str, непустые после strip().
    - amount: целое число >= 0 (type is int, bool не принимается).
    - completed: строго bool (type is bool).
    """
    if not isinstance(records, list):
        raise ValueError("Корневой элемент JSON должен быть списком.")

    seen_ids = set()

    for index, record in enumerate(records):
        if not isinstance(record, dict):
            raise ValueError(f"Запись с индексом {index} должна быть словарём.")

        for key in ("id", "title", "category", "amount", "completed"):
            if key not in record:
                raise ValueError(
                    f"В записи с индексом {index} отсутствует обязательное поле '{key}'."
                )

        record_id = record["id"]
        if type(record_id) is not int or record_id <= 0:
            raise ValueError(
                f"Поле 'id' в записи с индексом {index} должно быть положительным целым числом."
            )
        if record_id in seen_ids:
            raise ValueError(f"Обнаружен повторяющийся идентификатор id={record_id}.")
        seen_ids.add(record_id)

        title = record["title"]
        if not isinstance(title, str) or not title.strip():
            raise ValueError(
                f"Поле 'title' в записи с индексом {index} должно быть непустой строкой."
            )

        category = record["category"]
        if not isinstance(category, str) or not category.strip():
            raise ValueError(
                f"Поле 'category' в записи с индексом {index} должно быть непустой строкой."
            )

        amount = record["amount"]
        if type(amount) is not int or amount < 0:
            raise ValueError(
                f"Поле 'amount' в записи с индексом {index} должно быть целым числом не меньше 0."
            )

        completed = record["completed"]
        if type(completed) is not bool:
            raise ValueError(
                f"Поле 'completed' в записи с индексом {index} должно быть логическим значением (bool)."
            )

    return records


def next_record_id(records):
    """Вычисляет следующий уникальный ID: max существующих ID + 1 (или 1 для пустого списка).

    Контракт: не изменяет переданный список.
    """
    if not records:
        return 1
    return max(record["id"] for record in records) + 1


def add_record(records, title, category, amount):
    """Добавляет новую запись о блюде в список records.

    Контракт:
    - Изменяет переданный список records на месте (добавляет словарь в конец).
    - Убирает пробелы по краям у title и category.
    - Назначает новый ID (max + 1 или 1) и начальный статус completed=False.
    - При некорректных аргументах выбрасывает ValueError и не изменяет список.
    - Возвращает созданную запись (dict).
    """
    if not isinstance(title, str) or not title.strip():
        raise ValueError("Название блюда не должно быть пустым.")
    if not isinstance(category, str) or not category.strip():
        raise ValueError("Категория не должна быть пустой.")
    if type(amount) is not int or amount < 0:
        raise ValueError("Количество порций должно быть целым числом не меньше 0.")

    new_record = {
        "id": next_record_id(records),
        "title": title.strip(),
        "category": category.strip(),
        "amount": amount,
        "completed": False,
    }
    records.append(new_record)
    return new_record


def find_records(records, query):
    """Ищет записи, название которых содержит подстроку query без учёта регистра.

    Контракт:
    - Не изменяет исходный список и записи внутри него.
    - Если query не строка или пустая после strip(), выбрасывает ValueError.
    - Возвращает новый список копий найденных записей, отсортированный по возрастанию ID.
    """
    if not isinstance(query, str) or not query.strip():
        raise ValueError("Поисковый запрос не должен быть пустым.")

    needle = query.strip().casefold()
    matched = [
        dict(record)
        for record in records
        if needle in record["title"].casefold()
    ]
    matched.sort(key=lambda item: item["id"])
    return matched


def set_completed(records, record_id, completed):
    """Устанавливает статус приготовления (completed) для записи с указанным ID.

    Контракт:
    - Изменяет найденную запись в списке records на месте.
    - Если completed не строго bool, выбрасывает ValueError.
    - Возвращает True, если запись найдена и обновлена; False — если ID не найден.
    """
    if type(completed) is not bool:
        raise ValueError("Статус completed должен быть логическим значением (bool).")

    for record in records:
        if record["id"] == record_id:
            record["completed"] = completed
            return True
    return False


def delete_record(records, record_id):
    """Удаляет запись с указанным ID из списка records без перенумерации остальных.

    Контракт:
    - Изменяет список records на месте при наличии записи.
    - Возвращает True, если запись удалена; False — если ID не найден.
    """
    for index, record in enumerate(records):
        if record["id"] == record_id:
            del records[index]
            return True
    return False


def statistics(records):
    """Подсчитывает статистику по текущему списку блюд.

    Контракт:
    - Не изменяет исходный список records.
    - Возвращает словарь с ключами:
      - 'total': общее число записей (int),
      - 'completed': число приготовленных блюд (int),
      - 'uncompleted': число не приготовленных блюд (int),
      - 'total_amount': суммарное количество порций (int),
      - 'by_category': словарь {категория: сумма порций}, отсортированный по алфавиту.
    """
    total = len(records)
    completed = sum(1 for record in records if record["completed"])
    uncompleted = total - completed
    total_amount = sum(record["amount"] for record in records)

    category_totals = {}
    for record in records:
        category = record["category"].strip()
        category_totals[category] = category_totals.get(category, 0) + record["amount"]

    by_category = {
        category: category_totals[category]
        for category in sorted(category_totals)
    }

    return {
        "total": total,
        "completed": completed,
        "uncompleted": uncompleted,
        "total_amount": total_amount,
        "by_category": by_category,
    }
