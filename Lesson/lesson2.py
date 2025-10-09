class Hero:
    def __init__(self, name, lvl, classname):
        self.name = name
        self.lvl = lvl
        self.classname = classname

    def action(self):
        return f"Hero: {self.name}\nlvl: {self.lvl}\nclassname: {self.classname}"


class MageHero(Hero):
    def __init__(self, name, lvl, classname, mp):
        super().__init__ (name, lvl, classname)
        self.mp = mp


    def cast_spell(self):
        return f"{self.name} manna: {self.mp} \n{self.name} cast fire bal"
loki = Hero("loki", 20, "healer")
thor = MageHero("thor", 20, "healer", 100)
print(loki.action())
print(thor.cast_spell())