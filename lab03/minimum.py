first = int(input("Введите первое целое число: "))
second = int(input("Введите второе целое число: "))
third = int(input("Введите третье целое число: "))

if first <= second and first <= third:
    minimum = first
elif second <= first and second <= third:
    minimum = second
else:
    minimum = third
print(f"Минимальное число: {minimum}")
