text = input("Целые числа через пробел: ")

numbers = []
for part in text.split():
    numbers.append(int(part))

new_numbers = []
for number in numbers:
    if number < 0:
        new_numbers.append(-number)
    else:
        new_numbers.append(number)

print(f"Исходный список: {numbers}")
print(f"Новый список: {new_numbers}")
