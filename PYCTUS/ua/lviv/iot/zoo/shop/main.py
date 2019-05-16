from models.mamals import Mamals
from models.kindOfAnimal import KindOfAnimal
from models.sex import Sex
from models.animalWoolType import AnimalWoolType
from models.fish import Fish
from models.fishFormType import FishFormType
from models.birds import Birds
from models.birdsSoundsType import BirdsSoundsType
from manager.zooManager import ZooManager


def main():
    shopAnimals = [
        Mamals("Sanya", 400, KindOfAnimal.CASUAL,
                "Orange", 4, 350, Sex.FEMALE, "SpecialGrain", AnimalWoolType.LONG),
        Fish("Krasava", 1200, KindOfAnimal.CASUAL,
                "Grey", 7, 2000, Sex.MALE, "SpecialGrain", FishFormType.THIN),
        Birds("Krasava", 900, KindOfAnimal.CASUAL,
                "Grey", 6, 2000, Sex.FEMALE, "SpecialGrain", BirdsSoundsType.SOUNDS),
        Mamals("Krasava", 1500, KindOfAnimal.PREDATORS,
                "Grey", 3, 200, Sex.MALE, "AIGrain", AnimalWoolType.SHORT)
    ]
    manager = ZooManager(*shopAnimals)

    filtered_list = manager.filter_for_name("Krasava")
    for s in filtered_list:
        print(s)
    print()

    filtered_list2 = manager.filter_for_sex(Sex.FEMALE)
    for s in filtered_list2:
        print(s)
    print()

    sorted_food_list = manager.sort_by_food(shopAnimals)
    for s in sorted_food_list:
        print(s)

    sorted_price_increased_list = manager.sort_by_price_increase(shopAnimals)
    for s in sorted_price_increased_list:
        print(s)

    sorted_price_decreased_list = manager.sort_by_price_decrease(shopAnimals)
    for s in sorted_price_decreased_list:
        print(s)

    sorted_weight_increased_list = manager.sort_by_weight_increase(shopAnimals)
    for s in sorted_weight_increased_list:
        print(s)

    sorted_weight_decreased_list = manager.sort_by_weight_decrease(shopAnimals)
    for s in sorted_weight_decreased_list:
        print(s)


main()