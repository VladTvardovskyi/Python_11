from .shopAnimal import ShopAnimal
from .kindOfAnimal import KindOfAnimal
from .sex import Sex
from .birdsSoundsType import BirdsSoundsType


class Birds(ShopAnimal):

    def __init__(self,
                 name="no name", price=0,
                 kindOfAnimal=KindOfAnimal.CASUAL,
                 colour="no colour", age=0,
                 weight=0, sex=Sex.MALE, food="Some food",
                 birdsSoundsType=BirdsSoundsType
                 ):
        super().__init__(name, price, kindOfAnimal, colour,
                         age, weight, sex, food)
        self.birdsSoundsType=birdsSoundsType

    def __str__(self):
        return "{" + "name='" + str(self.name) + '\'' \
            + ", price='" + str(self.price) + '\'' \
            + ", kindOfAnimal=" + str(self.kindOfAnimal) \
            + ", colour=" + str(self.colour) \
            + ", age=" + str(self.age)\
            + ", weight=" + str(self.weight)\
            + ", sex=" + str(self.sex)\
            + ", food" + str(self.food)\
            + ", birds sounds type=" + str(self.birdsSoundsType)