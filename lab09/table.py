# table.py

def row_sums(matrix):
    sums = []

    for row in matrix:
        total = 0

        for number in row:
            total = total + number

        sums.append(total)

    return sums


def column_sums(matrix):
    sums = []

    if matrix == []:
        return sums

    columns = len(matrix[0])

    for column in range(columns):
        total = 0

        for row in matrix:
            total = total + row[column]

        sums.append(total)

    return sums


def diagonal_pattern(size):
    matrix = []

    for row in range(size):
        line = []

        for column in range(size):
            if row == column:
                line.append(0)
            elif row < column:
                line.append(1)
            else:
                line.append(2)

        matrix.append(line)

    return matrix


# Вариант 6: нули заменить единицами.
def transform(matrix):
    result = []

    for row in matrix:
        new_row = []

        for number in row:
            if number == 0:
                new_row.append(1)
            else:
                new_row.append(number)

        result.append(new_row)

    return result
