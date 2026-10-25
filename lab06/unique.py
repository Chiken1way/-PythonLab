text = input("Целые числа через пробел: ")

numbers = []
for part in text.split():
    numbers.append(int(part))

result = []
for number in numbers:
    if number not in result:
        result.append(number)

print(result)
