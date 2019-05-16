from .kindOfAnimal import KindOfAnimal
from .sex import Sex


class ShopAnimal:

    def __init__(self,
                name = "no name", price = 0,
                kindOfAnimal = KindOfAnimal.CASUAL,
                colour = "no colour", age = 0,
                weight=0, sex = Sex.MALE, food = "Some food"
                 ):
        self.name = name
        self.price = price
        self.kindOfAnimal = kindOfAnimal
        self.colour = colour
        self.age = age
        self.weight = weight
        self.sex = sex
        self.food = food

    def __str__(self):
        return "{" + "name='" + self.name + '\'' \
            + ", price='" + str(self.price) + '\'' \
            + ", kind Of Animals=" + str(self.kindOfAnimal) \
            + ", colour=" + self.colour \
            + ", age=" + self.age\
            + ", weight=" + self.weight\
            + ", sex=" + self.sex\
            + ", sfood=" + str(self.food)
