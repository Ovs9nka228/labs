symbol = input("Выберите символ для рисования: ")
height = int(input("Введите высоту прямоугольника: "))
width = int(input("Введите ширину прямоугольника: "))
print("Результат:")
row = 0
while row < height:
    col = 0
    line = ""
    while col < width:
        line += symbol
        col += 1
    print(line)
    row += 1
