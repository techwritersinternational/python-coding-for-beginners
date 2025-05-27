class Star:
    def __init__(self, name, x, y, z, luminosity):
        self.name = name
        self.x = x
        self.y = y
        self.z = z
        self.luminosity = luminosity

class StarMap:
    def __init__(self):
        self.stars = {}

    def add_star(self, star):
        if star.name in self.stars:
            print(f"Star '{star.name}' already exists in the map")
        else:
            self.stars[star.name] = star

    def remove_star(self, star_name):
        if star_name not in self.stars:
            print(f"Star '{star_name}' not found in the map")
        else:
            del self.stars[star_name]

    def get_star(self, star_name):
        return self.stars.get(star_name)

    def star_count(self):
        return len(self.stars)