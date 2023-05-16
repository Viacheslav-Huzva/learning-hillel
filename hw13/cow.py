import cow as cow

from Animal import Animal
import random


class Cow(Animal):
    def __init__(self):
        ...
        self.milk_production = random.randint(1, 10)
        self.milk_produced = 0

    def produce_milk(self):
        if self.hunger >= 5 or self.sleepiness >= 5 or self.playfulness >= 5 or self.walkiness >= 5 or self.friendliness >= 5:
            print(f'{self} не может давать молоко, так как не чувствует себя хорошо')
            return 0

        milk_amount = self.milk_production
        self.milk_produced += milk_amount
        return milk_amount


cow.names = ['Буренка', 'Ромашка', 'Зорька', 'Марта', 'Масяня', 'Полечка']
cows = []
for name in cow.names:
    cow = Cow()
    cows.append(cow)

for cow in cows:
    print(f'Имя: {cow}')
    print(f'Уровень голода: {cow.hunger}')
    print(f'Уровень сонливости: {cow.sleepiness}')
    print(f'Уровень игривости: {cow.playfulness}')
    print(f'Уровень желания гулять: {cow.walkiness}')
    print(f'Уровень дружелюбия: {cow.friendliness}')
    print(f'Уровень молокопроизводства: {cow.milk_production}')
    print(f'Количество произведенного молока: {cow.milk_produced}')
    print()
