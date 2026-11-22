def row_sums(matrix):
    result = []

    for row in matrix:
        total = 0
        for number in row:
            total = total + number
        result.append(total)

    return result


def column_sums(matrix):
    if matrix == []:
        return []

    result = []

    for column in range(len(matrix[0])):
        total = 0
        for row in matrix:
            total = total + row[column]
        result.append(total)

    return result


def diagonal_pattern(size):
    matrix = []

    for row in range(size):
        new_row = []

        for column in range(size):
            if row == column:
                new_row.append(0)
            elif row < column:
                new_row.append(1)
            else:
                new_row.append(2)

        matrix.append(new_row)

    return matrix


def transform(matrix):
    new_matrix = []

    for row in matrix:
        new_row = []

        for number in row:
            if number == 0:
                new_row.append(1)
            else:
                new_row.append(number)

        new_matrix.append(new_row)

    return new_matrix
