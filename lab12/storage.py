"""Модуль чтения и записи записей в JSON без консольных диалогов."""

import json
from pathlib import Path

from logic import validate_records


def load_records(path):
    """Загружает и проверяет список записей из JSON-файла в кодировке UTF-8.

    Контракт:
    - Возвращает проверенный список словарей.
    - Пробрасывает FileNotFoundError, если файл отсутствует.
    - Пробрасывает UnicodeError, json.JSONDecodeError, ValueError, OSError при ошибках
      чтения или некорректном содержимом; файл при этом не изменяется.
    """
    file_path = Path(path)
    with open(file_path, "r", encoding="utf-8") as file:
        data = json.load(file)
    return validate_records(data)


def save_records(path, records):
    """Проверяет и сохраняет список записей в JSON-файл в кодировке UTF-8.

    Контракт:
    - Не изменяет переданный список records.
    - При нарушении структуры выбрасывает ValueError до открытия файла на запись.
    - При ошибках файловой системы пробрасывает OSError.
    """
    validate_records(records)
    file_path = Path(path)
    with open(file_path, "w", encoding="utf-8") as file:
        json.dump(records, file, ensure_ascii=False, indent=2)
        file.write("\n")
