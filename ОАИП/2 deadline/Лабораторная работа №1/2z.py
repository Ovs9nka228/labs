schet = 0
print("Введите числа, для остановки введите 0: ")
while True:
    num = int(input("Введите число: "))
    if num == 0:
        break
    schet = schet + 1
print("Количество чисел: ",schet)
