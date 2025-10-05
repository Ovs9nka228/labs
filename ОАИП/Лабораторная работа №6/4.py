text = input("Введите текст: ")
numbers = input("Введите диапазон (число1 число2): ")

numbers1 = numbers.split()
num1 = numbers1[0]
num2 = numbers1[1]

start = int(num1)
end = int(num2)

result = text[start:end]
print(result)
