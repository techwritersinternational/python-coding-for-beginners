import random
import math

def determine_planet_count(star_mass, seed):
    """Determine the number of planets based on the star's mass and seed."""
    random.seed(seed)
    base_count = random.randint(0, 10)
    # Adjust count based on star mass (larger stars tend to have more planets)
    adjusted_count = int(base_count * (1 + (star_mass - 1) * 0.5))
    return max(0, min(adjusted_count, 15))  # Limit to 0-15 planets


def generate_planet_properties(star_mass, orbit_index, seed):
    """Generate planet properties based on star mass, orbit index, and seed."""
    random.seed(seed)
    
    # Generate planet size (Earth radii)
    size = random.uniform(0.1, 15)
    
    # Generate planet mass (Earth masses)
    mass = size ** 3 * (random.uniform(0.5, 2))  # Simplified mass-radius relation
    
    # Generate orbital period (Earth years)
    orbital_period = math.sqrt((orbit_index + 1) ** 3 / star_mass)
    
    return size, mass, orbital_period

def is_in_habitable_zone(star_temperature, orbital_period):
    """Determine if a planet is in the habitable zone based on star temperature and orbital period."""
    # Simplified habitable zone calculation
    habitable_zone_inner = 0.95 * (star_temperature / 5778) ** 2
    habitable_zone_outer = 1.37 * (star_temperature / 5778) ** 2
    return habitable_zone_inner <= orbital_period <= habitable_zone_outer


class Planet:
    def __init__(self, star_mass, star_temperature, orbit_index, seed):
        self.seed = seed
        self.size, self.mass, self.orbital_period = generate_planet_properties(star_mass, orbit_index, seed)
        self.habitable = is_in_habitable_zone(star_temperature, self.orbital_period)
        self.name = None  # Will be set by PlanetarySystem
        self.moons = []  # Will be populated by PlanetarySystem

    def __str__(self):
        return (f"Planet {self.name}: Size: {self.size:.2f} Earth radii, "
                f"Mass: {self.mass:.2f} Earth masses, "
                f"Orbital Period: {self.orbital_period:.2f} Earth years, "
                f"Habitable: {'Yes' if self.habitable else 'No'}")



def generate_planets(star_mass, star_temperature, seed):
    """Generate a list of planets for a star."""
    planet_count = determine_planet_count(star_mass, seed)
    planets = []
    for i in range(planet_count):
        planet_seed = seed + i  # Ensure unique seed for each planet
        planets.append(Planet(star_mass, star_temperature, i, planet_seed))
    return planets

# Example usage
if __name__ == "__main__":
    from seed_generator import generate_initial_seed, generate_next_seed
    from star_generator import generate_star

    seed = generate_initial_seed()
    star = generate_star(seed)
    planets = generate_planets(star.mass, star.temperature, generate_next_seed(seed))
    
    print(star)
    for planet in planets:
        print(planet)