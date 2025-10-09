class Hero:
    def __init__(self, name, lvl, hp):
        self.name = name
        self.lvl = lvl
        self.hp = hp

    def action(self):
        return f"{self.name} walkin"

loki = Hero('loki', 1000, 1000)
thor = Hero('thor', 1000, 1000)

#print(loki.action())

class Maghero(Hero):
    def __init__(self, name, lvl, hp, manna, ability):
        super().__init__ (name, lvl, hp)
        self.manna = manna
        self.ability = ability

spider_man = Hero('spider_man', 1000, 1000)
super_man = Maghero('super_man', 1000, 1000, 1000, 'flying')
#print(loki.lvl)
#print(super_man.ability)