text = input("Введите текст: ")
clean_text = ""
for char in text:
    if char.isalpha() or char == " ":
        clean_text = clean_text + char.lower()
    else:
        clean_text = clean_text + " "
words_list = clean_text.split()
unique_words = set()
for word in words_list:
    unique_words.add(word)
print("Уникальные слова:", len(unique_words))
long_words = set()
for word in unique_words:
    if len(word) > 5:
        long_words.add(word)
print("Длинные слова:", long_words)
has_python = False
has_programming = False
for word in unique_words:
    if word == "python":
        has_python = True
    if word == "programming":
        has_programming = True
found_keywords = has_python or has_programming
print("Найдены ключевые слова:", found_keywords)
if has_python or has_programming:
    print("Конкретно найдены:")
    if has_python:
        print("- python")
    if has_programming:
        print("- programming")
else:
    print("Ключевые слова не найдены")
