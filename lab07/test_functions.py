from functions import average, normalize_text, sum_digits, select_numbers, is_palindrome

assert sum_digits(0) == 0
assert sum_digits(507) == 12
assert sum_digits(-507) == 12
assert average([]) is None
assert average([2, 4, 6]) == 4
assert abs(average([1, 2]) - 1.5) < 1e-9
assert normalize_text("  ПРИВЕТ   Мир  ") == "привет мир"
assert normalize_text("   ") == ""

# --- вариант 6 (равно порогу) ---
assert select_numbers([-5, 0, 2, 5], 2) == [2]
assert select_numbers([], 2) == []
assert select_numbers([-5, 0, 5], 2) == []
assert select_numbers([1, 2, 3], 2) == [2]
assert select_numbers([2, 2, 5, 2], 2) == [2, 2, 2]
assert select_numbers([0, 1, 0], 0) == [0, 0]
assert select_numbers([-2, 2], 2) == [2]

original = [3, 2, 7, 2]
copy = [3, 2, 7, 2]
select_numbers(original, 2)
assert original == copy

assert is_palindrome("Топот") is True
assert is_palindrome("А роза упала на лапу Азора") is True
assert is_palindrome("привет") is False
assert is_palindrome("") is False
assert is_palindrome("   ") is False

print("Базовые проверки пройдены")
