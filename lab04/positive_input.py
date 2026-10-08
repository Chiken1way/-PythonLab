number = int(input("Введите целое число: "))
count = 0
while number <= 0:
    count += 1
    number = int(input("Введите целое число: "))
print(f"Квадрат числа: {number ** 2}")
print(f"Кол-во попыток: {count}")
