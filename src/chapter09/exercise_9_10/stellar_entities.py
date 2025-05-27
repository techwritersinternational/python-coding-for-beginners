class Star:
    def __init__(self, name, type, temperature):
        self.name = name
        self.type = type
        self.temperature = temperature

    def describe(self):
        return f"{self.name} is a {self.type} star with a temperature of {self.temperature}K."


class Planet:
    def __init__(self, name, type):
        self.name = name
        self.type = type

    def describe(self):
        return f"{self.name} is a {self.type} planet, {self.distance_from_star} million km from its star."


class Moon:
    def __init__(self, name, planet):
        self.name = name
        self.planet = planet

    def describe(self):
        return f"{self.name} is a moon orbiting {self.planet.name}."