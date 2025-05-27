from spacecraft import Spacecraft, CargoShip, SpaceTug

class Fleet:
    def __init__(self, name):
        self.name = name
        self.ships = []

    def add_ship(self, ship):
        self.ships.append(ship)

    def list_ships(self):
        for ship in self.ships:
            print(f"{ship.name} - {type(ship).__name__}")