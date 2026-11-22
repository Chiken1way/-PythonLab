# test_table.py

from table import row_sums, column_sums, diagonal_pattern, transform


# Таблица из двух строк и трёх столбцов
matrix = [[1, 2, 3], [4, 5, 6]]
assert row_sums(matrix) == [6, 15]
assert column_sums(matrix) == [5, 7, 9]

# Таблица из одного элемента
assert row_sums([[7]]) == [7]
assert column_sums([[7]]) == [7]
assert diagonal_pattern(1) == [[0]]

# Таблица из одного столбца
matrix = [[1], [-1], [0]]
assert row_sums(matrix) == [1, -1, 0]
assert column_sums(matrix) == [0]

# Пустая таблица
assert row_sums([]) == []
assert column_sums([]) == []
assert transform([]) == []

# Диагональный узор
assert diagonal_pattern(3) == [
    [0, 1, 1],
    [2, 0, 1],
    [2, 2, 0]
]

# Индивидуальный вариант 6: нули заменить единицами
matrix = [[-2, 0, 3], [4, -5, 6]]
result = transform(matrix)

assert result == [[-2, 1, 3], [4, -5, 6]]

# Проверяем, что новая таблица не меняет исходную
result[0][0] = 100
assert matrix == [[-2, 0, 3], [4, -5, 6]]

print("Все проверки пройдены!")
