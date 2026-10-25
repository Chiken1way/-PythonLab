# variant.py
# Индивидуальный вариант 6: слова длиной ровно 4 символа

text = input("Введите строку: ")

words = text.split()

count = 0

for word in words:
    # убираем знаки препинания по краям и делаем маленькие буквы
    clean_word = word.strip(".,!?;:").lower()

    # пустые слова пропускаем
    if clean_word == "":
        continue

    # условие варианта 6: длина равна 4
    if len(clean_word) == 4:
        print(clean_word)
        count = count + 1

if count == 0:
    print("Нет совпадений")

print("Количество:", count)
