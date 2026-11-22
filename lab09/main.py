# main.py

from table import row_sums, column_sums, diagonal_pattern, transform


rows = int(input("Количество строк: "))
columns = int(input("Количество столбцов: "))

matrix = []

for number in range(rows):
    row = [int(part) for part in input("Строка таблицы: ").split()]

    while len(row) != columns:
        print(f"Нужно ровно {columns} чисел")
        row = [int(part) for part in input("Повторите строку: ").split()]

    matrix.append(row)

print("\nИсходная таблица:")
for row in matrix:
    print(*row)

print("Суммы строк:", row_sums(matrix))
print("Суммы столбцов:", column_sums(matrix))

size = int(input("\nВведите положительный размер узора: "))

while size < 1:
    print("Размер должен быть положительным")
    size = int(input("Повторите размер: "))

pattern = diagonal_pattern(size)

print("Диагональный узор:")
for row in pattern:
    print(*row)

new_matrix = transform(matrix)

print("\nТаблица после преобразования (вариант 6):")
for row in new_matrix:
    print(*row)
