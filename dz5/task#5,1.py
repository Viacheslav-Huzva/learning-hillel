def is_palindrome(s):
    s = s.lower().replace(' ', '').replace('\t', '').replace('\n', '').replace(',', '').replace('.', '')
    return s == s[::-1]

string = input('Введіть рядок: ')

if is_palindrome(string):
    print(f'{string} є паліндромом')
else:
    print(f'{string} не є паліндромом')

    