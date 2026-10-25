text = input("Введите строку: ")

words = text.split()

count = 0

for word in words:
    clean_word = word.strip(".,!?;:").lower()

    if clean_word == "":
        continue

    if len(clean_word) == 4:
        print(clean_word)
        count = count + 1

if count == 0:
    print("Нет совпадений")

print("Количество:", count)
