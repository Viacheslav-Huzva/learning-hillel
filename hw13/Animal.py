import random


class Animal:
    def __init__(self, hunger, sleepiness, playfulness, walkiness, friendliness):
        self.hunger = hunger
        self.sleepiness = sleepiness
        self.playfulness = playfulness
        self.walkiness = walkiness
        self.friendliness = friendliness

    def how_hungry(self):
        return self.hunger

    def how_sleepy(self):
        return self.sleepiness

    def wants_to_play(self):
        if self.playfulness > 5:
            return True
        else:
            reason = random.choice(
                ["Я устал", "Я не настроен на игру", "Мне скучно", "Я жду кого-то", "Меня что-то беспокоит"])
            print(f"{self.__class__.__name__}: Я не хочу играть, потому что {reason}")
            return False

    def wants_to_walk(self):
        if self.walkiness > 5:
            return True
        else:
            return False

    def how_friendly(self):
        return self.friendliness
