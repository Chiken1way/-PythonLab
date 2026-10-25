text = input("Целые числа через пробел: ")

numbers = []
for part in text.split():
    numbers.append(int(part))
selected = []
for number in numbers:
    if number % 3 == 0:
        selected.append(number)

count = len(selected)
total = sum(selected)
sorted_copy = sorted(selected)

print(f"Выборка: {selected}")
print(f"Количество: {count}")
print(f"Сумма: {total}")
print(f"Отсортированная копия: {sorted_copy}")
