text = input("Введите текст: ")
search_word = input("Введите слово для поиска: ")
words = text.split()
word_count = words.count(search_word)

if word_count > 0:
    first_index = words.index(search_word)
    print(f"Слово '{search_word}' встречается {word_count} раз(а)")
    print(f"Первое вхождение имеет индекс: {first_index}")
else:
    print(f"Слово '{search_word}' не найдено в тексте")
    first_index = -1

cleaned_text = text.replace(search_word, "")
print("Текст без искомого слова:")
print(cleaned_text)
