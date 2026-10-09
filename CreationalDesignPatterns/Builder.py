class House:
    def __init__(self):
        self.walls = 0
        self.has_roof = False
        self.has_pool = False
        self.paint_color = "white"
        self.has_garage = False

    def __str__(self):
        return (
            f"House Details:\n"
            f"- Walls: {self.walls}\n"
            f"- Roof: {self.has_roof}\n"
            f"- Pool: {self.has_pool}\n"
            f"- Paint: {self.paint_color}\n"
            f"- Garage: {self.has_garage}"
        )

class HouseBuilder:
    def __init__(self):
        self.house = House()

    def add_walls(self, count):
        self.house.walls = count
        return self

    def add_roof(self):
        self.house.has_roof = True
        return self

    def add_pool(self):
        self.house.has_pool = True
        return self

    def set_paint_color(self, color):
        self.house.paint_color = color
        return self

    def add_garage(self):
        self.house.has_garage = True
        return self

    def get_result(self):
        return self.house

my_house = (
    HouseBuilder()
    .add_walls(4)
    .add_roof()
    .set_paint_color("blue")
    .get_result()
)

neighbor_house = (
    HouseBuilder()
    .add_walls(6)
    .add_roof()
    .set_paint_color("green")
    .add_garage()
    .get_result()
)

print(my_house)

print(neighbor_house)