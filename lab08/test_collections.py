from collections_lab import (
    word_counts,
    common_topics,
    all_topics,
    totals_by_category,
    titles_in_category
)

print("Подсчёт слов:")
print(word_counts("Python, python! SQL"))
print(word_counts("!!!"))

print("\nУчебные интересы:")
first = ["python", "sql", "python"]
second = ["sql", "git"]
print(common_topics(first, second))
print(all_topics(first, second))
print(common_topics([], ["python", "sql"]))
print(all_topics([], ["python", "sql"]))

print("\nПроверка рецептов:")
records = [
    {"title": "A", "category": "основное", "amount": 4},
    {"title": "B", "category": "дополнительное", "amount": 2},
    {"title": "C", "category": "основное", "amount": 3}
]

print(totals_by_category(records))
print(titles_in_category(records, "основное"))
print(titles_in_category(records, "нет"))
print(totals_by_category([]))
