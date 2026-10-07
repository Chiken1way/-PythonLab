price = int(input('Введите цену одной тетради : '))
count = int(input("Введите количество: "))
paid = int(input("Введите переданную сумму: "))
cost = price * count
change = paid - cost

print(f"Стоимость: {cost}руб Сдача: {change}руб")
