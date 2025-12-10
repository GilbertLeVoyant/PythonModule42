class Plant:
    def __init__(self, plant: str, height: int, age: int):
        self.plant = plant
        self.height = height
        self.ages = age

    def grow(self):
        self.height += 1

    def age(self):
        self.ages += 1

    def get_info(self):
        return f"{self.plant}: {self.ages}cm, {self.height} days old"

# if __name__ == "__main__":
#    mapetiterosedamour = Plant("Rose", 25, 30)
#    tulipe = Plant("Tulipe", 15, 5)
#    print("=== Day 1 ===\n")
#    print(mapetiterosedamour.get_info())
#    print(tulipe.get_info())
#    print("=== Day 2 ===\n")
#    tulipe.grow()
#    tulipe.age()
#    mapetiterosedamour.grow()
#    mapetiterosedamour.age()
#    print(mapetiterosedamour.get_info())
#    print(tulipe.get_info())
#    print("=== Day 3 ===\n")
#    tulipe.grow()
#    tulipe.age()
#    mapetiterosedamour.grow()
#    mapetiterosedamour.age()
#    print(mapetiterosedamour.get_info())
#    print(tulipe.get_info())
