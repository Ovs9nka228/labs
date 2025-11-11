text = input("Введите текст: ")
clean_text = ""
for char in text:
    if char.isalpha() or char == " ":
        clean_text = clean_text + char
    else:
        clean_text = clean_text + " "
words = clean_text.split()
lower_words = []
for word in words:
    lower_words.append(word.lower())
longest_word = ""
for word in lower_words:
    if len(word) > len(longest_word):
        longest_word = word
shortest_word = lower_words[0]
for word in lower_words:
    if len(word) < len(shortest_word) and len(word) > 0:
        shortest_word = word
total_length = 0
for word in lower_words:
    total_length = total_length + len(word)
average_length = total_length / len(lower_words)
word_count = {}
for word in lower_words:
    if word in word_count:
        word_count[word] = word_count[word] + 1
    else:
        word_count[word] = 1
pairs = []
for word, count in word_count.items():
    pairs.append((word, count))
for i in range(len(pairs)):
    for j in range(len(pairs) - 1):
        if pairs[j][1] < pairs[j + 1][1]:
            temp = pairs[j]
            pairs[j] = pairs[j + 1]
            pairs[j + 1] = temp
top_words = pairs[:5]
print("\nРезультаты анализа:")
print("Самое длинное слово:", longest_word)
print("Самое короткое слово:", shortest_word)
print("Средняя длина:", round(average_length, 1))
print("Топ-5 слов:", top_words)
