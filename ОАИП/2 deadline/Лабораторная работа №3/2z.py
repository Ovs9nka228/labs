text = input("Введите произвольный текст: ")
text = text.lower()
symbol_count = {}
for char in text:
    if char in symbol_count:
        symbol_count[char] = symbol_count[char] + 1
    else:
        symbol_count[char] = 1
print("Результат подсчета символов: ")
print(symbol_count)
