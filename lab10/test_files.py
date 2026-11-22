from pathlib import Path
from tempfile import TemporaryDirectory

from files_lab import read_matrix, selected_sum
from table import row_sums, column_sums


def check_value_error(path, message):
    try:
        read_matrix(path)
    except ValueError as error:
        if message != "":
            assert message in str(error)
    else:
        assert False, "Ошибка не обнаружена"


with TemporaryDirectory() as directory:
    folder = Path(directory)
    path = folder / "matrix.txt"

    path.write_text("1 2\n7 -1\n", encoding="utf-8")
    assert read_matrix(path) == [[7, -1]]
    print("Проверка обычной матрицы пройдена")

    path.write_text("1 1\n0\n", encoding="utf-8")
    assert read_matrix(path) == [[0]]
    print("Проверка матрицы 1 на 1 пройдена")

    path.write_text("", encoding="utf-8")
    check_value_error(path, "пустой")
    print("Проверка пустого файла пройдена")

    path.write_text("0 3\n", encoding="utf-8")
    check_value_error(path, "больше нуля")
    print("Проверка нулевого размера пройдена")

    path.write_text("1 2\n1\n", encoding="utf-8")
    check_value_error(path, "Строка 2")
    print("Проверка короткой строки пройдена")

    path.write_text("1 2\n1 x\n", encoding="utf-8")
    check_value_error(path, "Строка 2")
    print("Проверка нечислового значения пройдена")

    path.write_text("1 1\n5\n6\n", encoding="utf-8")
    check_value_error(path, "")
    print("Проверка лишней строки пройдена")

    missing_path = folder / "missing.txt"

    try:
        read_matrix(missing_path)
    except FileNotFoundError:
        pass
    else:
        assert False, "Не обнаружен отсутствующий файл"
    print("Проверка отсутствующего файла пройдена")


matrix = [[1, -2, 3], [4, 0, -6]]
assert row_sums(matrix) == [2, -2]
assert column_sums(matrix) == [5, -2, -3]
assert selected_sum(matrix) == 1
print("Проверка сумм и варианта 6 пройдена")

matrix_without_matches = [[-2, 0], [1, 2]]
assert selected_sum(matrix_without_matches) == 0
print("Проверка отсутствия подходящих элементов пройдена")

print("Все проверки пройдены!")
