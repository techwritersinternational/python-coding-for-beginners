class Spacecraft:
    """A class to represent a spacecraft."""

    def __init__(self, name, speed):
        self.name = name
        self.speed = speed

    def fly(self):
        print(f"{self.name} is flying at {self.speed} speed.")

class CargoShip(Spacecraft):
    """A class to represent a cargo ship."""

    def __init__(self, name, speed, cargo_capacity):
        super().__init__(name, speed)
        self.cargo_capacity = cargo_capacity

    def load_cargo(self, amount):
        print(f"{self.name} is loading {amount} units of cargo.")

class SpaceTug(Spacecraft):
    """A class to represent a fighter ship."""

    def __init__(self, name, speed, tractor_beam_power):
        super().__init__(name, speed)
        self.tractor_beam_power = tractor_beam_power

    def pull(self):
        print(f"{self.name} is pulling with a tractor beam rated at {self.tractor_beam_power}.")