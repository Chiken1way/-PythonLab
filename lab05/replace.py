# replace.py
# Задание 3. Замена с подсчётом

text = input("Введите текст: ")

# сначала считаем двоеточия в исходном тексте
count = text.count(":")

# потом заменяем (replace не меняет text, а возвращает новую строку)
new_text = text.replace(":", "-")

print("Замен:", count)
print("Новая строка:", new_text)
