class House:
    def __init__(self, how_many_flours: int, house_area_inside: float) -> None:
        self._adress_: str = "Street and hose number"
        self.how_many_flours = 3
        self.house_area_inside = 155

    def my_home_outside(self, color: str) -> None:
        print(f"My house color: {color}")        
    
    def my_home_inside(self, how_many_rooms: int) -> None:
        self.how_many_rooms = 15

class Area_of_the_house(House):
    def __init__(self, a_x: int, a_z: float) -> None:
        super().__init__(how_many_flours= a_x)
        super().__init__(house_area_inside= a_z)

    def trees(self, number_of_trees: int):
        print(f"Number of tree: {number_of_trees}")

home_sweet_home = Area_of_the_house()
print(f"About my SWEET HOMES: ")
print(f"It hass {home_sweet_home.how_many_flours} flours")
print(f"{home_sweet_home.house_area_inside} area of the house")
print(f"")
home_sweet_home.my_home_outside("Brown")
