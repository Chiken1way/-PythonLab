def word_counts(text):
    words = text.lower().split()
    counts = {}

    for word in words:
        word = word.strip(".,!?;:")
        if word != "":
            counts[word] = counts.get(word, 0) + 1

    return counts


def print_word_counts(counts):
    for word in sorted(counts):
        print(f"{word}: {counts[word]}")


def common_topics(first, second):
    first_set = set(first)
    second_set = set(second)
    result = first_set & second_set
    return sorted(result)


def all_topics(first, second):
    first_set = set(first)
    second_set = set(second)
    result = first_set | second_set
    return sorted(result)


def totals_by_category(records):
    totals = {}

    for record in records:
        category = record["category"]
        totals[category] = totals.get(category, 0) + record["amount"]

    return totals


def titles_in_category(records, category):
    titles = []

    for record in records:
        if record["category"] == category:
            titles.append(record["title"])

    return titles


if __name__ == "__main__":
    print("Частоты слов:")
    text = input("Введите текст: ")
    counts = word_counts(text)
    print_word_counts(counts)

    print("\nУчебные интересы:")
    first = ["python", "sql", "python"]
    second = ["sql", "git"]
    print("Общие темы:", common_topics(first, second))
    print("Все темы:", all_topics(first, second))

    print("\nСловарь и кортеж:")
    recipe = {"title": "Борщ", "hours": 2}
    recipe["hours"] = 3
    recipe["completed"] = False

    pair = (recipe["title"], recipe["hours"])
    title, hours = pair
    print(f"Пара: {title}, {hours}")
