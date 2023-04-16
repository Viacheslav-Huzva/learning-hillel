import random


class Cat:

    def __init__(self, name, breed, age):
        self.name = name
        self.breed = breed
        self.age = age
        self.hunger = random.randint(0, 10)  # рівень голоду (випадкове значення від 0 до 10)
        self.energy = random.randint(0, 10)  # рівень енергії (випадкове значення від 0 до 10)

    def eat(self):
        if self.hunger > 5:
            self.hunger -= 5
            print(f"{self.name} їсть і задоволений/на")
        else:
            print(f"{self.name} не хоче їсти")

    def walk(self):
        if self.energy > 3:
            self.energy -= 3
            print(f"{self.name} гуляє і насолоджується свіжим повітрям")
        else:
            print(f"{self.name} занадто втомлений/а, щоб гуляти")

    def meow(self):
        print(f"{self.name}: М'яу!")

    def sleep(self):
        self.energy += 5
        print(f"{self.name} спить і заряджається енергією")


# Створюємо кішок
cat1 = Cat("Мурка", "Домашня кішка", 3)
cat2 = Cat("Барсік", "Сіамська", 2)
cat3 = Cat("Рижик", "Британська", 1)
cat4 = Cat("Сірко", "Шотландська", 4)
cat5 = Cat("Вася", "Персидська", 5)
cat6 = Cat("Мурзик", "Домашня кішка", 2)

# День кішок
for cat in [cat1, cat2, cat3, cat4, cat5, cat6]:
    print(f"{cat.name}:")
    cat.eat()
    cat.walk()
    cat.meow()
    cat.sleep()
    print("-" * 20)


class Dog:
    def __init__(self, name, breed, age, weight):
        self.name = name
        self.breed = breed
        self.age = age
        self.weight = weight
        self.hunger = random.randint(0, 10)  # ступінь голоду, де 0 - повна ситість, 10 - голод
        self.energy = random.randint(0, 10)  # рівень енергії, де 0 - дуже втомлена, 10 - повна енергія

    def eat(self):
        self.hunger -= 3
        if self.hunger < 0:
            self.hunger = 0
        print(self.name, "їсть. Ступінь голоду:", self.hunger)

    def walk(self):
        if self.energy < 3:
            print(self.name, "надто втомлена, щоб гуляти")
        else:
            self.energy -= 3
            if self.energy < 0:
                self.energy = 0
            print(self.name, "гуляє. Рівень енергії:", self.energy)

    def sleep(self):
        self.energy += 2
        if self.energy > 10:
            self.energy = 10
        print(self.name, "спить. Рівень енергії:", self.energy)


# Створення 6 об'єктів класу Собака
dogs = []
breeds = ["Сибірський хаскі", "Німецька вівчарка", "Бульдог", "Пекінес", "Бігль", "Пудель"]
names = ["Рекс", "Белла", "Макс", "Барон", "Джек", "Бейлі"]
for i in range(6):
    breed = random.choice(breeds)
    name = names[i]
    age = random.randint(1, 10)
    weight = random.randint(5, 40)
    dog = Dog(name, breed, age, weight)
    dogs.append(dog)

# Запуск "звичайного дня" питомців
for dog in dogs:
    print("\n", dog.name, "(", dog.breed, ",", dog.age, "р.,", dog.weight, "кг )")
    dog.eat()
    dog.walk()
    dog.sleep()
