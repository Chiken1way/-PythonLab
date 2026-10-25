from functions import sum_digits, average, normalize_text, select_numbers


def main():
    # 1. сумма цифр
    number = int(input("Введите целое число: "))
    print("Сумма цифр:", sum_digits(number))

    # 2. среднее
    line = input("Введите числа через пробел: ")
    numbers = []
    for part in line.split():
        numbers.append(int(part))

    avg = average(numbers)
    if avg is None:
        print("Нет данных")
    else:
        print("Среднее:", avg)

    # 3. нормализация текста
    text = input("Введите любой текст: ")
    print("Нормализованный текст:", normalize_text(text))

    # вариант 6
    threshold = int(input("Введите порог (целое, не меньше 0): "))
    print("Числа, равные порогу:", select_numbers(numbers, threshold))


if __name__ == "__main__":
    main()
