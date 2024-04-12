from random import choice, randint

THINGS_NAMES = ('Ring', 'Sword', 'Kilt', 'Gloves', 'Lance', 'Hat')
MAX_DEFENCE = 10
MAX_DAMAGE_HP = 20

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


class Thing(): 
    def __init__(self): 
        self.name = choice(THINGS_NAMES)
        self.defence = randint(0, MAX_DEFENCE) / 100
        self.damage = randint(0, MAX_DAMAGE_HP)
        self.hp = randint(0, MAX_DAMAGE_HP)


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
        """Одеваем персонажа рандомными вещами и устанавливаем финальные характеристики"""
        self.persons_things = []
        for _ in range(randint(1, MAX_THINGS_FOR_PERSON)):
            self.persons_things.append(things.pop())
        for thing in self.persons_things:
            self.final_health_points = self.base_health_points + thing.hp
            self.final_attack = self.base_attack + thing.damage
            self.final_protection = self.base_protection + thing.defence

    def attack_damage(self, attacking):
        self.final_health_points = self.final_health_points - attacking.final_attack/self.final_protection

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
    # Шаг 1. Создаём список вещей
    things = []
    for i in range(10):
        things.append(Thing())
    things.sort(key=lambda x: x.defence)
    print(things)

    # Шаг 2.
    paladins = [Paladin() for _ in range(randint(0, PERSONS_COUNT))]
    warriors = [Warrior() for _ in range(10 - len(paladins))]
    persons = paladins + warriors

    # Шаг 3. Одеваем персонажей
    for person in persons:
        person.set_things(things)

    # Шаг 4. Отправляем персонажей на арену
    while len(persons) > 1
        attacking = choice(persons)
        persons.pop(attacking)
        defending = choice(persons)
        persons.pop(defending)
        #attacking_hp = attacking.hp
        #defending_hp = defending_hp
        while attacking.hp > 0 or defending.hp > 0:
            attacking.attac(defending)
            print(f'{attacking.name} наносит удар по {defending.name} на {кол-во урона} урона')
            new_attacing = defending
            defending = attacking
            attacking  = new_attacing
        if attacking.hp > 0
            attacking.hp = attacking.def_hp
            print(f'{attacking.name} победил {defending.name}')
            persons.append(attacking)
        else:
            defending.hp = defending.def_hp
            print(f'{defending.name} победил {attacking.name}')
            persons.append(defending)

if __name__ == '__main__':
    main()
