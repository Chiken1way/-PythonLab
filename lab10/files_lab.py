def read_matrix(path):
    with open(path, "r", encoding="utf-8") as file:
        lines = file.readlines()

    if len(lines) == 0:
        raise ValueError("Файл пустой")

    header = lines[0].split()

    if len(header) != 2:
        raise ValueError("Строка 1: в заголовке должно быть два числа")

    try:
        rows = int(header[0])
        columns = int(header[1])
    except ValueError:
        raise ValueError("Строка 1: заголовок должен содержать целые числа")

    if rows <= 0 or columns <= 0:
        raise ValueError("Строка 1: количество строк и столбцов должно быть больше нуля")

    if len(lines) != rows + 1:
        raise ValueError("Неверное количество строк с данными")

    matrix = []

    for i in range(rows):
        line_number = i + 2
        parts = lines[i + 1].split()

        if len(parts) != columns:
            raise ValueError("Строка " + str(line_number) + ": неверное количество чисел")

        row = []

        for part in parts:
            try:
                number = int(part)
            except ValueError:
                raise ValueError("Строка " + str(line_number) + ": найдено не целое число")

            row.append(number)

        matrix.append(row)

    return matrix


def selected_sum(matrix):
    total = 0

    for row in matrix:
        for number in row:
            if abs(number) > 2:
                total = total + number

    return total
