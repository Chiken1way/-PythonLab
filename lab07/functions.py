def sum_digits(number):
    """Вернуть сумму цифр модуля числа."""
    number = abs(number)  # сначала берем модуль, чтобы с минусом не зациклилось
    total = 0
    while number > 0:
        total = total + number % 10  # последняя цифра
        number = number // 10        # отбрасываем последнюю цифру
    return total


def average(numbers):
    """Вернуть среднее списка или None, если список пустой."""
    if len(numbers) == 0:
        return None
    return sum(numbers) / len(numbers)


def normalize_text(text):
    """Нижний регистр, без пробелов по краям, между словами один пробел."""
    words = text.lower().split()  # split() сам убирает лишние пробелы
    return " ".join(words)


def select_numbers(numbers, threshold):
    """Вариант 6: вернуть новый список из чисел, равных порогу."""
    result = []
    for n in numbers:
        if n == threshold:
            result.append(n)
    return result


def is_palindrome(text):
    """Дополнительно: палиндром ли текст (пробелы и знаки не учитываем)."""
    text = normalize_text(text)
    letters = ""
    for ch in text:
        if ch.isalnum():
            letters = letters + ch
    if letters == "":
        return False
    return letters == letters[::-1]
