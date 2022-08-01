class Player:
    def __init__(self, hp, **kwargs):
        print(super().__init__)
        self.hp = hp

    def sign_in(self):
        print('player sign in')


class Worrior(Player):
    def __init__(self, worrior_name, power, **kwargs):
        super().__init__(**kwargs)
        self.name = worrior_name
        self.power = power

    def __str__(self):
        return "The worrior's name: " f'{self.name} \n' \
               "He has the power:" f'{self.power}'


class Archer(Player):
    def __init__(self, archer_name, agility, **kwargs):
        super().__init__(**kwargs)
        self.name = archer_name
        self.agility = agility

    def __str__(self):
        return "The archer's name: " f'{self.name} \n' \
               "He has the agility:" f'{self.agility}'


class Boss(Worrior, Archer):
    def __init__(self, name, power, agility, hp):
        super().__init__(archer_name=name, worrior_name=name, power=power, agility=agility, hp=hp)

    def __str__(self):
        return "The boss's name: " f'{self.name} \n' \
               "With Worrior's power " f'{self.power} \n' \
               "and With Archer's agilit" f'{self.agility}' \
               "The boss' hp is: " f'{self.hp}'
boss = Boss("Boss", 50, 50, 100)
print(boss.__str__())
