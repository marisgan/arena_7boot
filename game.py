import random

NAMES = ('Ring', 'Sword', 'Kilt', 'Gloves', 'Lance', 'Hat')
MAX_DEFENCE = 10
MAX_DAMAGE_HP = 20


class Thing(): 
    def __init__(self): 
        self.name = random.choice(NAMES)
        self.defence = random.randint(0, MAX_DEFENCE)
        self.damage = random.randint(0, MAX_DAMAGE_HP)
        self.hp = random.randint(0, MAX_DAMAGE_HP)


def main():

    things = []
    for i in range(10):
        things.append(Thing())
    things.sort(key=lambda x: x.defence)
    print(things)


if __name__ == '__main__':
    main()