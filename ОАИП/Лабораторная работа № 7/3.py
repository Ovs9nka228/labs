text = input("Введите текст: ")
word = input("Введите слово для поиска: ")

words_list = text.lower().split()
search_word = word.lower()
count = words_list.count(search_word)

if count > 0:
    print(f"Слово '{word}' встречается в тексте {count} раз(а)")
else:
    print(f"Слова '{word}' нет в тексте")
