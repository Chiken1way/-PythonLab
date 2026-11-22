records = [
    {"title": "Борщ", "category": "супы", "amount": 4},
    {"title": "Сырники", "category": "завтраки", "amount": 2},
    {"title": "Паста с сыром", "category": "основные блюда", "amount": 3},
    {"title": "Грибной суп", "category": "супы", "amount": 5},
    {"title": "Омлет", "category": "завтраки", "amount": 2},
    {"title": "Курица с рисом", "category": "основные блюда", "amount": 4}
]


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
    totals = totals_by_category(records)

    print("Количество порций по категориям:")
    for category in sorted(totals):
        print(f"{category}: {totals[category]}")

    category = input("Введите категорию для поиска: ")
    titles = titles_in_category(records, category)
    print("Найденные рецепты:", titles)
