import string

def word_input():
    words = []
    while True:
        user_input = input("Введіть слово (або введіть порожній рядок для виходу): ")
        if user_input == "":
            # Вихід з циклу, якщо користувач ввів порожній рядок
            break
        elif user_input.isalpha():
            # Видалення символів пунктуації зі слова
            user_input = user_input.translate(str.maketrans('', '', string.punctuation))
            words.append(user_input)
        else:
            print("Введіть тільки слово!")
    return words


words = word_input()

for word in words:
    print(word)
