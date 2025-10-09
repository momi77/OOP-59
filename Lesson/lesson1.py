class Hero:
    def __init__(self, name, lvl, classname):
        self.name = name
        self.lvl = lvl
        self.classname = classname

    def action(self):
        return f"Hero: {self.name}\n lvl: {self.lvl}\n classname: {self.classname}"

    def attaking(self):
        return f"{self.name} attacking"

loki = Hero("loki", 100, "healer")
thor = Hero("thor", 100, "tank")
print(loki.action())
print(thor.action())
print(loki.attaking())