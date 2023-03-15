# сама функция что удаляет слова в скобках

def remove_brackets(text):
    while '(' in text:
        start = text.index('(')
        end = text.index(')')
        while '((' in text:
            start = text.index('((')
            end = text.index('))')
            text = text[:start] + text[end + 2:]
        text = text[:start] + text[end + 1:]
    return text

string = input('Введіть рядок: ')

# текст что ввел пользователь только без слов в скобках

new_string = remove_brackets(string)

print(new_string)
