stroka = input("Введите строку: ")
chist = stroka.lower().replace(" ","")
left = 0
right = len(chist) - 1
palindrom = True
while right > left:
    if chist[left] != chist[right]:
        palindrom = False
        break
    left = left + 1
    right = right -1
if palindrom:
    print("Да, это палиндром")
else:
    print("Нет, это не палиндром")
