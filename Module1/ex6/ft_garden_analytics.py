class Plant:
    def __init__(self, name: str, height: int):
        self.name = name
        self.height = height


class FloweringPlant(Plant):
    def __init__(self, name, height, color: str):
        super().__init__(name, height)
        self.color = color


class PrizeFlower(FloweringPlant):
    def __init__(self, name, height, color, prize: int):
        super().__init__(name, height, color)
        self.prize = prize


class GardenManager:
    def __init__(self, name: str):
        self.name = name
        self.lst_plant = []
    
    class GardenStat:
        def get_nb_plant(self):
            i = 0
            for n in self.lst_plant:
                if n.__class__.__name__ == "Plant":
                    i += 1
            return i

        def get_nb_flowplant(self):
            i = 0
            for n in self.lst_plant:
                if n.__class__.__name__ == "FloweringPlant":
                    i += 1
                return i
            