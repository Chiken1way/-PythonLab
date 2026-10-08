n = int(input("Введите n (n >= 0): "))

count = 0
total = 0
for _ in range(n):
    number = int(input("Введите число: "))
    if number % 3 == 0:
        count += 1
        total += number

print(f"Количество: {count}")
print(f"Сумма: {total}")
