students = [
    ("Анна", 21, 4.5),
    ("Петр", 22, 4.2),
    ("Мария", 19, 4.8),
    ("Иван", 20, 4.1),
    ("Ольга", 23, 4.7)
]
print("Студенты старше 20 лет:")
found_older = False
for student in students:
    name = student[0]
    age = student[1]
    grade = student[2]
    if age > 20:
        print(f"- {name} ({age}), средний балл: {grade}")
        found_older = True
if not found_older:
    print("Студентов старше 20 лет нет")
print()
best_student = students[0]
for student in students:
    if student[2] > best_student[2]:
        best_student = student
print(f"Лучший студент: {best_student[0]}, средний балл: {best_student[2]}")
print()
sorted_students = students.copy()
for i in range(len(sorted_students)):
    for j in range(len(sorted_students) - 1):
        if sorted_students[j][0] > sorted_students[j + 1][0]:
            temp = sorted_students[j]
            sorted_students[j] = sorted_students[j + 1]
            sorted_students[j + 1] = temp
print("Студенты отсортированные по имени:")
for student in sorted_students:
    print(f"- {student[0]}, возраст: {student[1]}, средний балл: {student[2]}")
