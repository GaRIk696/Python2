words = []

while True:
    i = input("Введите строку: ").strip()
    if not i:
        print("Вы не ввели исходный список")
        continue

    punctuation = '!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~'
    cleaned_input = ''.join(char for char in i if char not in punctuation)
    words = [word.lower() for word in cleaned_input.split()]

    if words:
        break
    else:
        print("Строка не может состоять только из знаков препинания!")

dictionary = {}
for word in words:
    dictionary[word] = dictionary.get(word, 0) + 1

for word, count in dictionary.items():
    print(f"{word}: {count}")