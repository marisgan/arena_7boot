from random import choice, randint

THINGS_NAMES = ('Ring', 'Sword', 'Kilt', 'Gloves', 'Lance', 'Hat')
MAX_DEFENCE = 10
MAX_DAMAGE_HP = 20

PERSONS_NAMES = [
    'Скорпион', 'Китана', 'Кобра', 'Горо', 'Шао Кан', 'Джейд', 'Саб-Зиро',
    'Джонни Кейдж', 'Кунг Лао', 'Кабал', 'Генерал Шао', 'Ашра', 'Барака',
    'Герас', 'Кэнси', 'Лю Кан', 'Таня', 'Хавик', 'Нитара', 'Милина'
]
persons_names = PERSONS_NAMES.copy()

THINGS_NUM = 50
MAX_THINGS_FOR_PERSON = 4
PERSONS_COUNT = 10
BASE_HP = 50
BASE_ATTACK = 10
BASE_PROTECTION = 0.01


def set_name(names):
    """Выбираем уникальное рандомное имя из списка имён"""
    return names.pop(randint(0, len(names) - 1))


class Thing():
    """Класс игровых вещей"""
    def __init__(self):
        self.name = choice(THINGS_NAMES)
        self.defence = randint(0, MAX_DEFENCE) / 100
        self.damage = randint(0, MAX_DAMAGE_HP)
        self.hp = randint(0, MAX_DAMAGE_HP)

    def __str__(self):
        return f'{self.name} {self.defence} {self.damage} {self.hp}'


class Person:
    """Базовый класс для игровых персонажей"""

    def __init__(
            self,
            base_hp=BASE_HP,
            base_attack=BASE_ATTACK,
            base_protection=BASE_PROTECTION
    ):
        self.name = set_name(persons_names)
        self.hp = base_hp
        self.attack = base_attack
        self.protection = base_protection

    def __str__(self):
        return self.name

    def set_things(self, things):
        """Одеваем вещи на персонажа, применяем их характеристики"""
        self.persons_things = []
        for _ in range(randint(1, MAX_THINGS_FOR_PERSON)):
            self.persons_things.append(things.pop(randint(0, len(things) - 1)))
        for thing in self.persons_things:
            self.hp += thing.hp
            self.attack += thing.damage
            self.protection += thing.defence

    def decrease_hp(self, attack_damage):
        """Метод для уменьшения жизней во время боя"""
        self.hp -= attack_damage


class Paladin(Person):

    def __init__(self):
        super().__init__()
        self.hp *= 2
        self.protection *= 2


class Warrior(Person):

    def __init__(self):
        super().__init__()
        self.attack *= 2


def main():
    """Шаг 1. Создаём список вещей"""
    things = []
    for i in range(THINGS_NUM):
        things.append(Thing())
    things.sort(key=lambda x: x.defence)

    """Шаг 2. Создаём персонажей"""
    paladins = [Paladin() for _ in range(randint(0, PERSONS_COUNT - 1))]
    warriors = [Warrior() for _ in range(PERSONS_COUNT - len(paladins))]
    persons = paladins + warriors

    """Шаг 3. Одеваем персонажей"""
    for person in persons:
        person.set_things(things)
        print(
            f'Участник: {person}, {type(person).__name__}, '
            f'Здоровье: {person.hp}, Атака: {person.attack}, '
            f'Защита: {round(person.protection, 5)}'
        )

    """Шаг 4. Отправляем персонажей на арену"""
    while len(persons) > 1:
        attacker = persons.pop(randint(0, len(persons) - 1))
        defender = persons.pop(randint(0, len(persons) - 1))
        while True:
            attack_damage = (
                attacker.attack - attacker.attack * defender.protection
            )
            defender.decrease_hp(attack_damage)
            print(
                f'{attacker.name} наносит удар по {defender.name} '
                f'на {round(attack_damage, 5)} урона'
            )
            if defender.hp < 0:
                persons.append(attacker)
                print(
                    f'В поединке побеждает {attacker.name}. '
                    f'{defender.name} выбывает.'
                )
                break
            else:
                attacker, defender = defender, attacker
    print(f'Финальный победитель: {persons.pop().name}')


if __name__ == '__main__':
    main()
