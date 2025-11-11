grades = []
grades.append(5)
grades.append(4)
grades.append(3)
grades.append(5)
grades.append(2)
print("Текущие оценки:", grades)
del grades[0]
del grades[-1]
summa = 0
for ocenka in grades:
    summa = summa + ocenka
sredniy_ball = summa / len(grades)
print("Средний балл:", sredniy_ball)
print("Итоговые оценки:", grades)
