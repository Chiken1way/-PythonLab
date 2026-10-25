# Лабораторная 6, задание 3: позиции максимума

text = input("Целые числа через пробел: ")

numbers = []
for part in text.split():
    numbers.append(int(part))

if len(numbers) == 0:
    print("Нет данных")
else:
    biggest = max(numbers)  # сначала находим максимум

    # потом ищем все места, где он встречается
    positions = []
    for index, value in enumerate(numbers):
        if value == biggest:
            positions.append(index)

    print(positions)
