sum = 0
while True:
    user_input = input("Введіть число або 'sum' для отримання суми: ")
    if user_input == "sum":
        print("Сума введених чисел:", sum)
        break
    else:
        try:
            number = float(user_input)
            sum += number
        except ValueError:
            print("Некоректне введення, введіть число або 'sum'.")
