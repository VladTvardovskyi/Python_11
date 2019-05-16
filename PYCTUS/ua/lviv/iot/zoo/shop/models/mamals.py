from .shopAnimal import ShopAnimal
from .kindOfAnimal import KindOfAnimal
from .sex import Sex
from .animalWoolType import AnimalWoolType


class Mamals(ShopAnimal):

    def __init__(self,
                 name="no name", price=0,
                 kindOfAnimal=KindOfAnimal.CASUAL,
                 colour="no colour", age=0,
                 weight=0, sex=Sex.MALE, food="Some food",
                 animalWoolType=AnimalWoolType
                 ):
        super().__init__(name, price, kindOfAnimal, colour,
                         age, weight, sex, food)
        self.animalWoolType=animalWoolType

    def __str__(self):
        return "{" + "name=" + str(self.name) + '\'' \
            + ", price='" + str(self.price) + '\'' \
            + ", kindOfAnimal=" + str(self.kindOfAnimal) \
            + ", colour=" + str(self.colour) \
            + ", age=" + str(self.weight)\
            + ", sex=" + str(self.sex)\
            + ", food" + str(self.food)\
            + ", animal wool type=" + str(self.animalWoolType)
