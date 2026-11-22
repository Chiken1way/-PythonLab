from pathlib import Path

from files_lab import read_matrix, selected_sum
from table import row_sums, column_sums


folder = Path(__file__).resolve().parent
matrix_path = folder / "matrix.txt"
report_path = folder / "report.txt"


def read_positive_integer():
    while True:
        try:
            number = int(input("Введите положительное целое число: "))
        except ValueError:
            print("Нужно ввести целое число")
        else:
            if number <= 0:
                print("Число должно быть больше нуля")
            else:
                return number


def numbers_to_string(numbers):
    result = ""

    for number in numbers:
        result = result + str(number) + " "

    return result.strip()


def main():
    number = read_positive_integer()
    print("Введено число:", number)

    try:
        matrix = read_matrix(matrix_path)

        sums_rows = row_sums(matrix)
        sums_columns = column_sums(matrix)
        result_variant = selected_sum(matrix)

        report_text = "Суммы строк: " + numbers_to_string(sums_rows) + "\n"
        report_text = report_text + "Суммы столбцов: " + numbers_to_string(sums_columns) + "\n"
        report_text = report_text + "Результат варианта: " + str(result_variant) + "\n"

        with open(report_path, "w", encoding="utf-8") as file:
            file.write(report_text)

        print("Отчёт сохранён в report.txt")

    except FileNotFoundError:
        print("Файл matrix.txt не найден")
    except UnicodeError:
        print("Ошибка кодировки файла")
    except ValueError as error:
        print("Ошибка формата:", error)
    except OSError:
        print("Ошибка доступа к файлу")


if __name__ == "__main__":
    main()
