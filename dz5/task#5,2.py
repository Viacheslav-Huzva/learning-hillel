def remove_brackets(text):
    while '(' in text:
        start = text.index('(')
        end = text.index(')')
        text = text[:start] + text[end+1:]
    return text

string = input('Введіть рядок: ')

new_string = remove_brackets(string)

print(new_string)