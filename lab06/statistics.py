text = input("Целые числа через пробел: ")

numbers = []
for part in text.split():
    numbers.append(int(part))
if len(numbers) == 0:
    print("Нет данных")
else:
    count = len(numbers)
    total = sum(numbers)
    smallest = min(numbers)
    biggest = max(numbers)
    average = total / count

    print(f"Количество: {count}")
    print(f"Сумма: {total}")
    print(f"Минимум: {smallest}")
    print(f"Максимум: {biggest}")
    print(f"Среднее: {average:.2f}")
