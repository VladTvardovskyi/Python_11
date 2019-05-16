class ZooManager:

    def __init__(self, *shopAnimals):
        self.shopAnimals = shopAnimals

    @staticmethod
    def sort_by_food(shopAnimals, from_up_to_down=False):
        return sorted(shopAnimals, key=lambda shopAnimal: shopAnimal.food, reverse=from_up_to_down)

    @staticmethod
    def sort_by_price_decrease(shopAnimals, from_Up_To_Down=True):
        return sorted(shopAnimals, key=lambda shopAnimal: shopAnimal.price, reverse=from_Up_To_Down)

    @staticmethod
    def sort_by_price_increase(shopAnimals, from_Up_To_Down=False):
        return sorted(shopAnimals, key=lambda shopAnimal: shopAnimal.price, reverse=from_Up_To_Down)

    @staticmethod
    def sort_by_weight_increase(shopAnimals, from_Up_To_Dowm=False):
        return sorted(shopAnimals, key=lambda shopAnimal: shopAnimal.weight, reverse=from_Up_To_Dowm)

    @staticmethod
    def sort_by_weight_decrease(shopAnimals, from_Up_To_Dowm=True):
        return sorted(shopAnimals, key=lambda shopAnimal: shopAnimal.weight, reverse=from_Up_To_Dowm)

    def filter_for_name(self, name):
        return list(filter(lambda shopAnimal: shopAnimal.name == name, self.shopAnimals))

    def filter_for_sex(self, sex):
        return list(filter(lambda shopAnimal: shopAnimal.sex == sex, self.shopAnimals))














