import random
from collections import namedtuple

StarType = namedtuple('StarType', ['name', 'mass_range', 'radius_range', 'temp_range'])

STAR_TYPES = [
    StarType('M', (0.08, 0.45), (0.1, 0.7), (2400, 3700)),
    StarType('K', (0.45, 0.8), (0.7, 0.96), (3700, 5200)),
    StarType('G', (0.8, 1.04), (0.96, 1.15), (5200, 6000)),
    StarType('F', (1.04, 1.4), (1.15, 1.4), (6000, 7500)),
    StarType('A', (1.4, 2.1), (1.4, 1.8), (7500, 10000)),
]

def determine_star_type(seed):
    """Determine the star type based on the seed."""
    random.seed(seed)
    probabilities = [0.76, 0.12, 0.076, 0.03, 0.014]  # Approximate real-world probabilities
    return random.choices(STAR_TYPES, weights=probabilities)[0]

def generate_star_properties(star_type, seed):
    """Generate star properties based on its type and seed."""
    random.seed(seed)
    mass = random.uniform(*star_type.mass_range)
    radius = random.uniform(*star_type.radius_range)
    temperature = random.uniform(*star_type.temp_range)
    return mass, radius, temperature

class Star:
    def __init__(self, seed):
        self.seed = seed
        self.type = determine_star_type(seed)
        self.mass, self.radius, self.temperature = generate_star_properties(self.type, seed)
        self.name = None  # Will be set by PlanetarySystem

    def __str__(self):
        return (f"Star {self.name}: Type {self.type.name}, "
                f"Mass: {self.mass:.2f} solar masses, "
                f"Radius: {self.radius:.2f} solar radii, "
                f"Temperature: {self.temperature:.0f} K")

def generate_star(seed):
    """Generate a star based on the given seed."""
    return Star(seed)

# Example usage
if __name__ == "__main__":
    from seed_generator import generate_initial_seed, generate_next_seed

    seed = generate_initial_seed()
    for _ in range(5):
        star = generate_star(seed)
        print(star)
        seed = generate_next_seed(seed)