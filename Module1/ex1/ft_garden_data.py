class Plant:
    def __init__(self, plant: str, height: int, age: int):
        self.plant = plant
        self.height = height
        self.age = age

    def toString(self):
        return f"{self.plant}: {self.age}cm, {self.height} days old"


# if __name__ == "__main__":
#    mapetiterosedamour = Plant("Rose", 25, 30)
#    print(mapetiterosedamour.toString())
#    tulipe = Plant("Tulipe", 15, 5)
#    print(tulipe.toString())
