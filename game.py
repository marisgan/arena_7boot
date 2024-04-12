from random import choice, randint

PERSONS_NAMES = [
    'Скорпион', 'Китана', 'Кобра', 'Горо', 'Шао Кан', 'Джейд', 'Саб-Зиро',
    'Джонни Кейдж', 'Кунг Лао', 'Кабал',
]
persons_names = PERSONS_NAMES.copy()

MAX_THINGS_FOR_PERSON = 4
PERSONS_COUNT = 10
HEALTH_POINTS = 100
BASE_ATTACK = 10
BASE_PROTECTION = 0.01


def set_name(names):
    return names.pop(randint(0, len(names) - 1))


class Person:
    """Базовый класс для игровых персонажей"""

    def __init__(
            self,
            health_points=HEALTH_POINTS,
            base_attack=BASE_ATTACK,
            base_protection=BASE_PROTECTION
    ):
        self.name = set_name(persons_names)
        self.base_health_points = health_points
        self.base_attack = base_attack
        self.base_protection = base_protection

    def __str__(self):
        return self.name

    def set_things(self, things):
        """Одеваем персонажа рандомными вещами"""
        self.persons_things = []
        for _ in range(randint(1, MAX_THINGS_FOR_PERSON)):
            self.persons_things.append(things.pop())

    def set_final_attributes(
            self,
            things_health_points,
            things_base_attack,
            things_base_protection
    ):
        self.final_health_points = self.base_health_points + things_health_points
        self.final_attack = self.base_attack + things_base_attack
        self.final_protection = self.base_protection + things_base_protection


class Paladin(Person):

    def __init__(self):
        super().__init__()
        self.base_health_points *= 2
        self.base_protection *= 2


class Warrior(Person):

    def __init__(self):
        super().__init__()
        self.base_attack *= 2


def main():
    paladins = [Paladin() for _ in range(randint(0, PERSONS_COUNT))]
    warriors = [Warrior() for _ in range(10 - len(paladins))]
    for paladin in paladins:
        print(paladin)
    print('--------')
    for warrior in warriors:
        print(warrior)


if __name__ == '__main__':
    main()
