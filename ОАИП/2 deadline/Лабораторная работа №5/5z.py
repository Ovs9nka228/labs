math_students = {"Alice", "Bob", "Charlie", "David"}
physics_students = {"Bob", "David", "Eve", "Frank"}
cs_students = {"Alice", "Charlie", "Eve", "Grace"}
print("Студенты на математике:", math_students)
print("Студенты на физике:", physics_students)
print("Студенты на программировании:", cs_students)
print()
all_three = set()
for student in math_students:
    if student in physics_students and student in cs_students:
        all_three.add(student)
print("Все три курса:", all_three)
only_one_course = set()
for student in math_students:
    if student not in physics_students and student not in cs_students:
        only_one_course.add(student)
for student in physics_students:
    if student not in math_students and student not in cs_students:
        only_one_course.add(student)
for student in cs_students:
    if student not in math_students and student not in physics_students:
        only_one_course.add(student)
print("Только один курс:", only_one_course)
math_not_physics = set()
for student in math_students:
    if student not in physics_students:
        math_not_physics.add(student)
print("Математика но не физика:", math_not_physics)
all_students = set()
for student in math_students:
    all_students.add(student)
for student in physics_students:
    all_students.add(student)
for student in cs_students:
    all_students.add(student)
print("Всего студентов:", len(all_students))
print("Все студенты:", all_students)
