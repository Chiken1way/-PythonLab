total = int(input("Количество деталей: "))
capacity = int(input("Деталей в контейнере: "))

print("Заполненных контейнеров:", total // capacity)
print("Остаток деталей:", total % capacity)
print("Минимум контейнеров:", (total + capacity - 1) // capacity)