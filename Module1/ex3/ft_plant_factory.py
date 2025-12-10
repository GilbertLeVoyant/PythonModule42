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
#    lst_plants = [
#        Plant("Rose", 25, 30),
#        Plant("Oak", 200, 365),
#        Plant("Cactus", 5, 90),
#        Plant("Sunflower", 80, 45),
#        Plant("Fern", 15, 120)
#        ]
#    i = 0
#    for n in lst_plants:
#        print(f"Created: {n.plant} ({n.height}cm, {n.ages} days)")
#        i += 1
#    print(f"Total plants created: {i}")
