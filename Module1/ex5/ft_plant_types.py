class Plant:
    def __init__(self, plant: str, height: int, age: int):
        self.plant = plant
        self.height = height
        self.ages = age


class Tree(Plant):
    def __init__(self, plant: str, height: int, age: int, d: int, s: int):
        super().__init__(plant, height, age)
        self.diameter = d
        self.shade = s

    def produce_shade(self):
        if self.shade > 0:
            area = int(self.diameter*self.height)
            return f"{self.plant} provides {area} square meters of shade"
        else:
            return f"{self.plant} dosn't provides shade"

    def __str__(self):
        return (f"{self.plant} ({self.__class__.__name__}): {self.height}cm, "
                f"{self.ages} days, {self.diameter}cm diameter")


class Flower(Plant):
    def __init__(self, plant: str, height: int, age: int, color: str, b: int):
        super().__init__(plant, height, age)
        self.color = color
        self.blooming = b

    def bloom(self):
        if self.blooming > 0:
            return f"{self.plant} is blooming beautifully!"
        else:
            return f"{self.plant} isn't blooming, it's sad"

    def __str__(self):
        return (f"{self.plant} ({self.__class__.__name__}): {self.height}cm, "
                f"{self.ages} days, {self.color} color")


class Vegetable(Plant):
    def __init__(self, plant, height, age, season: str, nutri_v: str):
        super().__init__(plant, height, age)
        self.season = season
        self.nutri_v = nutri_v

    def __str__(self):
        return (f"{self.plant} ({self.__class__.__name__}): {self.height}cm, "
                f"{self.ages} days, {self.season} harvest")


# if __name__ == "__main__":
#    print("=== Garden Plant Types ===\n")
#    tulipe = Flower("Tulipe", 14, 12, "yellow", 0)
#    rose = Flower("Rose", 20, 10, "red", 1)
#    print(tulipe)
#    print(tulipe.bloom())
#    print("\n")
#    print(rose)
#    print(rose.bloom())
#    print("\n")

#    oak = Tree("Oak", 500, 1825, 50, 0)
#    acacia = Tree("Acacia", 20000, 2542, 75, 1)
#    print(oak)
#    print(oak.produce_shade())
#    print("\n")
#    print(acacia)
#    print(acacia.produce_shade())
#    print("\n")

#    tomato = Vegetable("Tomato", 15, 26, "summer", "Vitamin C")
#    salad = Vegetable("Salad", 7, 2, "spring", "Vitamin B")
#    print(tomato)
#    print(f"{tomato.plant} is rich in {tomato.nutri_v}")
#    print("\n")
#    print(salad)
#    print(f"{salad.plant} is rich in {salad.nutri_v}")
#    print("\n")
