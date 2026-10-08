load = int(input("Загрузка процессора от 0 до 100: "))

if load < 0 or load > 100:
    print("Ошибка диапазона")
elif load <= 29:
    print("Низкая")
elif load <= 69:
    print("Средняя")
else:
    print("Высокая")
