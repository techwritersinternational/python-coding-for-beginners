class ChrystalineLifeform:
    """A class to represent a chrystaline lifeform."""

    def __init__(self, name, color, size):
        """Initialize the chrystaline lifeform."""
        self.name = name
        self.color = color
        self.size = size


    def grow(self):
        """Simulate the lifeform growing."""
        print(f"{self.name} is growing larger!")


    def refract_light(self):
        """Simulate the lifeform refracting light."""
        print(f"{self.name} refracts light, creating a beautiful {self.color} display!")


crystal_entity = ChrystalineLifeform("Sparkle", "blue", "medium")

print(crystal_entity.name)  # Output: Sparkle
print(crystal_entity.color)  # Output: blue
print(crystal_entity.size)  # Output: medium

crystal_entity.grow()  # Output: Sparkle is growing larger!
crystal_entity.refract_light()  # Output: Sparkle refracts light, creating a beautiful blue display!

crystal_entity2 = ChrystalineLifeform("Glimmer", "green", "small")
print(f"{crystal_entity2.name} is {crystal_entity2.color}")  # Output: Glimmer is green
crystal_entity2.grow()  # Output: Glimmer is growing larger!