from abc import ABC, abstractmethod
import practika
loki = practika.Maghero("loki", 1000, 1000, 1000, "ilusion")
print(loki.manna)

class Song:
    def __init__(self, text, janr, autor):
        self.text = text
        self.janr = janr
        self.autor = autor

    @abstractmethod
    def singing(self):
        return f"bad singer {self.autor}"

    @abstractmethod
    def dancing(self):
        return f"bad dancer {self.autor}"