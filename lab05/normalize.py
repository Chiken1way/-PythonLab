text = input("Введите текст: ")

old_len = len(text)
words = text.split()

new_text = " ".join(words)
new_len = len(new_text)

print("Исходная длина:", old_len)
print("Новая длина:", new_len)
print("Нормализованный текст:", new_text)
print("Слов:", len(words))
