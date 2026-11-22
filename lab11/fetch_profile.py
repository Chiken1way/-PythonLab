"""HTTP-упражнение: получение профиля пользователя GitHub по логину или из локального примера."""

import json
import socket
from pathlib import Path
from urllib.error import HTTPError, URLError
from urllib.parse import quote
from urllib.request import Request, urlopen


def fetch_profile(login):
    if not login.strip():
        raise ValueError("Логин не должен быть пустым")
    url = "https://api.github.com/users/" + quote(login.strip(), safe="")
    request = Request(url, headers={
        "Accept": "application/vnd.github+json",
        "User-Agent": "python-course-lab11",
    })
    with urlopen(request, timeout=10) as response:
        data = json.loads(response.read().decode("utf-8"))
    if not isinstance(data, dict) or not isinstance(data.get("login"), str):
        raise ValueError("Ответ не похож на профиль пользователя")
    return data


def load_local_profile(path):
    """Читает учебный локальный профиль из JSON-файла."""
    with open(path, "r", encoding="utf-8") as file:
        data = json.load(file)
    if not isinstance(data, dict) or not isinstance(data.get("login"), str):
        raise ValueError("Локальный файл не похож на профиль пользователя")
    return data


def display_profile(data, source_description):
    """Общая функция вывода данных профиля для обоих источников."""
    print(f"Источник данных: {source_description}")
    print(f"Логин: {data['login']}")
    if "id" in data:
        print(f"ID: {data['id']}")
    if "name" in data:
        name_value = data["name"]
        print(f"Имя: {name_value if name_value is not None else 'не указано (null)'}")


def main():
    base_dir = Path(__file__).resolve().parent
    print("Выберите источник профиля:")
    print("1 — Сеть (GitHub API)")
    print("2 — Локальный пример (profile_sample.json)")
    choice = input("Ваш выбор (1/2): ").strip()

    try:
        if choice == "1":
            data = fetch_profile(input("Логин GitHub: "))
            output = base_dir / "profile.json"
            with open(output, "w", encoding="utf-8") as file:
                json.dump(data, file, ensure_ascii=False, indent=2)
            display_profile(data, "GitHub API (сеть)")
            print(f"Профиль сохранён: {data['login']}")
        elif choice == "2":
            sample_path = base_dir / "profile_sample.json"
            data = load_local_profile(sample_path)
            display_profile(data, "учебные локальные данные (profile_sample.json)")
        else:
            print("Неизвестный пункт меню. Введите 1 или 2.")
    except HTTPError as error:
        print(f"Сервер вернул HTTP {error.code}")
    except (URLError, TimeoutError, socket.timeout):
        print("Не удалось получить ответ по сети")
    except json.JSONDecodeError as error:
        print(f"Ошибка JSON: {error}")
    except (ValueError, UnicodeError) as error:
        print(f"Ошибка данных: {error}")
    except OSError as error:
        print(f"Ошибка доступа: {error}")


if __name__ == "__main__":
    main()
