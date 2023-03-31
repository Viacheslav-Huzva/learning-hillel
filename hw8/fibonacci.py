# Функция-генератор для последовательности чисел Фибоначчи
def fibonacci():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b


# Функция для поиска ближайшего числа Фибоначчи, которое больше или равно n
def find_fibonacci_number(n):
    for i, f in enumerate(fibonacci()):
        if f >= n:
            return i, f


# Функция для вывода последовательности чисел Фибоначчи до максимального допустимого значения из чисел Фибоначи
def print_fibonacci_sequence(n):
    index, fibonacci_number = find_fibonacci_number(n)  # находим ближайшее число Фибоначчи, которое больше или равно n
    print("Числа Фибоначчи до", fibonacci_number)
    for f in fibonacci():
        if f > fibonacci_number:  # выходим из цикла, если достигли максимального значения
            break
        print(f)


number = input("Введите число: ")
if not number.isdigit():  # проверяем, что введенное значение является целым числом
    print("Ошибка: введите целое число.")
else:
    n = int(number)
    if n == 0:
        print("Число является числом Фибоначчи.")
    else:
        index, fibonacci_number = find_fibonacci_number(
            n)  # находим ближайшее число Фибоначчи, которое больше или равно n
        if fibonacci_number == n:  # проверяем, является ли введенное число числом Фибоначчи
            print(n, "является числом Фибоначчи.")
        else:
            print(n, "не является числом Фибоначчи.")
        print_fibonacci_sequence(
            fibonacci_number)  # выводим последовательность чисел Фибоначчи до максимального значения
