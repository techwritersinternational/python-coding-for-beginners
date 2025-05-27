class Spacecraft:
    """A class to represent a generic spacecraft."""

    def __init__(self, name, speed):
        """Initialize the spacecraft."""
        self.name = name
        self.speed = speed

    def move(self):
        """Simulate the spacecraft moving."""
        print(f"{self.name} is moving at {self.speed} speed.")


class CargoShip(Spacecraft):
    """A class to represent a cargo ship, inheriting from Spacecraft."""

    def __init__(self, name, speed, cargo_capacity):
        """Initialize the cargo ship."""
        super().__init__(name, speed)
        self.cargo_capacity = cargo_capacity
        self.current_cargo = 0

    def load_cargo(self, amount):
        """Load cargo onto the ship."""
        if self.current_cargo + amount <= self.cargo_capacity:
            self.current_cargo += amount
            print(f"Loaded {amount} units. Current cargo: {self.current_cargo}")
        else:
            print("Error: Exceeds cargo capacity")


# Create a regular spacecraft
galaxy_end = Spacecraft("Galaxy's End", "warp 5")
galaxy_end.move()

# Create a cargo ship
hauler = CargoShip("Star Hauler", "warp 3", 1000)

# Test the cargo ship's movement (inherited from Spacecraft)
hauler.move()

# Test cargo loading
print(f"\nCargo operations for {hauler.name}:")
print(f"Capacity: {hauler.cargo_capacity}")
hauler.load_cargo(500)
hauler.load_cargo(300)
hauler.load_cargo(300)  # This should exceed capacity and fail

# Print final cargo status
print(f"\nFinal cargo status for {hauler.name}:")
print(f"Current cargo: {hauler.current_cargo}")
print(f"Remaining capacity: {hauler.cargo_capacity - hauler.current_cargo}")