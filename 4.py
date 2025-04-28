def count_words():
    input_string = input("Введите строку: ")
    words = input_string.lower().split()

    unique_words = set(words)

    word_count = {word: words.count(word) for word in unique_words}

    for word, count in word_count.items():
        print(f"{word}: {count}")

count_words()