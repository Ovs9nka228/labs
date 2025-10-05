print("Введите произвольный текст:")
text = input()

print("Введите две строки через пробел (что заменить на что):")
strings = input()

strings_l = strings.split()

string1 = strings_l[0]
string2 = strings_l[1]
new_text = text.replace(string1, string2)

print("Результат:")
print(new_text)
