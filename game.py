import random

NAMES = ('Ring', 'Sword', 'Kilt', 'Gloves', 'Lance', 'Hat')
MAX_DEFENCE = 10
MAX_DAMAGE_HP = 20


class Thing(): 
    def __init__(self): 
        self.name = random.choice(NAMES)
        self.defence = random.randint(0, MAX_DEFENCE) / 100
        self.damage = random.randint(0, MAX_DAMAGE_HP)
        self.hp = random.randint(0, MAX_DAMAGE_HP)


def main():
    # Шаг 1. Создаём список вещей
    things = []
    for i in range(10):
        things.append(Thing())
    things.sort(key=lambda x: x.defence)
    print(things)

    persons = []
    # Шаг 3. Одеваем персонажей
    for person in persons:
        person.set_things(things)

    # Шаг 4. Отправляем персонажей на арену
    while len(persons) > 1
        attacking = random.choice(persons)
        persons.pop(attacking)
        defending = random.choice(persons)
        persons.pop(defending)
        
        while attacking.hp > 0 or defending.hp > 0:
            
            print(f'{attacking.name} наносит удар по {defending.name} на {кол-во урона} урона')
            new_attacing = defending
            defending = attacking
            attacking  = new_attacing

if __name__ == '__main__':
    main()