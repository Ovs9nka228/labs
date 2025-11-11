statistics = {}
while True:
    text = input()
    if text == "":
        break
    words = text.split()
    for word in words:
        clean_word = ""
        for char in word:
            if char.isalpha():
                clean_word += char
        clean_word = clean_word.lower()
        if clean_word == "":
            continue
        if clean_word in statistics:
            statistics[clean_word] += 1
        else:
            statistics[clean_word] = 1
print("Статистика слов:", statistics)
