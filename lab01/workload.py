
subject_1 = input("Введите название первого предмета: ")
subject_2 = input("Введите название второго предмета: ")
number_of_classes_1 = int(input("Введите количество занятий по первому предмету за неделю: "))
number_of_classes_2 = int(input("Введите количество занятий по второму предмету за неделю: "))

duration_1 = int(input("Введите продолжительность занятия первого предмета в минутах: "))
duration_2 = int(input("Введите продолжительность занятия второго предмета в минутах: "))

minutes1 = number_of_classes_1 * duration_1
minutes2 = number_of_classes_2 * duration_2

total_minutes = minutes1 + minutes2
total_hours = total_minutes / 60

available_hours = float(input("Сколько часов в неделю вы можете выделить на учёбу: "))
remaining_hours = available_hours - total_hours

print(f"Предмет {subject_1}: {minutes1} мин. в неделю")
print(f"Предмет {subject_2}: {minutes2} мин. в неделю")
print(f"Общая нагрузка: {total_minutes} мин. ({total_hours:.2f} ч.)")
print(f"Остаток свободного времени: {remaining_hours:.2f} ч.")
print(f"Нагрузка за 4 недели: {total_minutes * 4} мин. ({total_hours * 4} ч.)")