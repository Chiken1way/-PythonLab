name_order = input("Введите название заказа: ")
name_customer = input("Введите свое имя: ")

item1_name = input("Введите название первой позиции: ")
item1_qty = int(input("Введите количество первой позиции: "))
item1_price = float(int(input("Введите цену первой позиции за одну штуку: ")))

item2_name = input("Введите название второй позиции: ")
item2_qty = int(input("Введите количество второй позиции: "))
item2_price = float(input("Введите цену второй позиции за одну штуку: "))

delivery_cost = float(input("Введите стоимость доставки: "))
paid_amount = float(input("Введите внесённую сумму: "))

item1_cost = item1_qty * item1_price
item2_cost = item2_qty * item2_price

total_cost = item1_cost + item2_cost
total_cost_with_delivery = total_cost + delivery_cost

total_qty = item2_qty + item1_qty
change = paid_amount - total_cost_with_delivery

print("Заказ: ", name_order)
print("Имя:, name_customer: ", name_customer)
print(f"{item1_name} {item1_qty} {item1_price:.2f} {item1_cost:.2f}")
print(f"{item2_name} {item2_qty} {item2_price:.2f} {item2_cost:.2f}")
print(f"Стоимость товаров без доставки: {total_cost:.2f}")
print(f"Стоимость доставки: {delivery_cost:.2f}")
print(f"Общая сумма с доставкой: {total_cost_with_delivery:.2f}")
print(f"Общее количество единиц: {total_qty}")
print(f"Внесённая сумма: {paid_amount:.2f}")
print(f"Сдача: {change:.2f}")
