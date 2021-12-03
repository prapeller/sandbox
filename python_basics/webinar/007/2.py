from abc import ABC, abstractmethod


class Clothes(ABC):
    @abstractmethod
    @property
    def tissue_consumption(self):
        pass


class Coat(Clothes):
    def __init__(self, size):
        self.size = size

    @property
    def tissue_consumption(self):
        return self.size / 6.5 + 0.5


class Suit(Clothes):
    def __init__(self, height):
        self.height = height

    @property
    def tissue_consumption(self):
        return self.height * 2 + 0.3


coat_38 = Coat(38)
print(coat_38.tissue_consumption)

suit_25 = Suit(25)
print(suit_25.tissue_consumption)
