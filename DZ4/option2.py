numbers = []
while True:
    user_input = input("Введіть число або 'sum' для отримання суми: ")
    if user_input == "sum":
        print("Сума введених чисел:", sum(numbers))
        break
    else:
        try:
            number = float(user_input)
            numbers.append(number)
        except ValueError:
            print("Некоректне введення, введіть число або 'sum'.")
