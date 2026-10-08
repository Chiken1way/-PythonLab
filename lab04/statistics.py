n = int(input("Введите n (n >= 1): "))

first = int(input("Введите число: "))
total = first
positive_count = 1 if first > 0 else 0
maximum = first  # инициализация первым значением, а не нулём

for _ in range(n - 1):
    number = int(input("Введите число: "))
    total += number
    if number > 0:
        positive_count += 1
    if number > maximum:
        maximum = number

print(f"Сумма: {total}")
print(f"Положительных: {positive_count}")
print(f"Максимум: {maximum}")
