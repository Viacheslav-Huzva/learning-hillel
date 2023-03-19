import math


def read_positive_number(prompt):
    while True:
        num = float(input(prompt))
        if num <= 0:
            print("Введіть додатнє число")
        else:
            return num


def is_triangle_possible(a, b, c):
    return (a + b > c) and (a + c > b) and (b + c > a)


def calculate_perimeter(a, b, c):
    return a + b + c


def calculate_area(a, b, c):
    p = calculate_perimeter(a, b, c) / 2
    return math.sqrt(p * (p - a) * (p - b) * (p - c))

# говорим user ввести углы трикутника. если такой трикутник есть то идем дальше по

if __name__ == '__main__':
    a = read_positive_number("Введіть першу сторону трикутника: ")
    b = read_positive_number("Введіть другу сторону трикутника: ")
    c = read_positive_number("Введіть третю сторону трикутника: ")

    if is_triangle_possible(a, b, c):
        perimeter = calculate_perimeter(a, b, c)
        area = calculate_area(a, b, c)
        print(
            f"Трикутник зі сторонами {a}, {b} та {c} існує. Його периметр дорівнює {perimeter:.2f}, а площа - {area:.2f}.")
    else:
        print(f"Трикутник зі сторонами {a}, {b} та {c} не існує.")
