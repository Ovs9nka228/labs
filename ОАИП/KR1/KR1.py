input_string = input("Введите три слова через пробел: ")
separator = input("Введите символ-разделитель (/, -, # или другой): ")
words = input_string.split()
if len(words) != 3:
    print("Ошибка: нужно ввести ровно три слова!")
else:
    word1 = words[0]
    has_digit1 = False
    for char in word1:
        if char >= '0' and char <= '9':
            has_digit1 = True
            break
    if has_digit1:
        word1 = "NUMBER"
    word2 = words[1]
    has_digit2 = False
    for char in word2:
        if char >= '0' and char <= '9':
            has_digit2 = True
            break
    if has_digit2:
        word2 = "NUMBER"
    word3 = words[2]
    has_digit3 = False
    for char in word3:
        if char >= '0' and char <= '9':
            has_digit3 = True
            break
    if has_digit3:
        word3 = "NUMBER"
    if separator == "/":
        result = word1 + "/" + word2 + "/" + word3
    elif separator == "-":
        result = word1 + "-" + word2 + "-" + word3
    elif separator == "#":
        result = word1 + "#" + word2 + "#" + word3
    else:
        result = word1 + separator + word2 + separator + word3
    print("Результат:", result)
