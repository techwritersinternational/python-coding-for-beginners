import random
import math

def determine_moon_count(planet_mass, planet_size, seed):
    """Determine the number of moons based on the planet's mass, size, and seed."""
    random.seed(seed)
    # Larger, more massive planets tend to have more moons
    base_count = int((planet_mass * planet_size) ** 0.5)
    variation = random.randint(-2, 2)
    return max(0, base_count + variation)

def generate_moon_properties(planet_mass, planet_size, orbit_index, seed):
    """Generate moon properties based on planet mass, size, orbit index, and seed."""
    random.seed(seed)
    
    # Generate moon size (relative to planet size)
    size = random.uniform(0.01, 0.5) * planet_size
    
    # Generate moon mass (assuming similar density to the planet)
    mass = (size / planet_size) ** 3 * planet_mass
    
    # Generate orbital period (in Earth days)
    orbital_period = math.sqrt((orbit_index + 1) ** 3 / (planet_mass * 332946))  # 332946 is mass of Earth relative to Moon
    
    return size, mass, orbital_period

class Moon:
    def __init__(self, planet_mass, planet_size, orbit_index, seed):
        self.seed = seed
        self.size, self.mass, self.orbital_period = generate_moon_properties(planet_mass, planet_size, orbit_index, seed)
        self.name = f"Moon-{seed % 10000:04d}"  # Placeholder name

    def __str__(self):
        return (f"Moon {self.name}: Size: {self.size:.2f} Earth radii, "
                f"Mass: {self.mass:.4f} Earth masses, "
                f"Orbital Period: {self.orbital_period:.2f} Earth days")

def generate_moons(planet_mass, planet_size, seed):
    """Generate a list of moons for a planet."""
    moon_count = determine_moon_count(planet_mass, planet_size, seed)
    moons = []
    for i in range(moon_count):
        moon_seed = seed + i  # Ensure unique seed for each moon
        moons.append(Moon(planet_mass, planet_size, i, moon_seed))
    return moons

import random
import math

def determine_moon_count(planet_mass, planet_size, seed):
    """Determine the number of moons based on the planet's mass, size, and seed."""
    random.seed(seed)
    # Larger, more massive planets tend to have more moons
    base_count = int((planet_mass * planet_size) ** 0.5)
    variation = random.randint(-2, 2)
    return max(0, base_count + variation)

def generate_moon_properties(planet_mass, planet_size, orbit_index, seed):
    """Generate moon properties based on planet mass, size, orbit index, and seed."""
    random.seed(seed)
    
    # Generate moon size (relative to planet size)
    size = random.uniform(0.01, 0.5) * planet_size
    
    # Generate moon mass (assuming similar density to the planet)
    mass = (size / planet_size) ** 3 * planet_mass
    
    # Generate orbital period (in Earth days)
    orbital_period = math.sqrt((orbit_index + 1) ** 3 / (planet_mass * 332946))  # 332946 is mass of Earth relative to Moon
    
    return size, mass, orbital_period

class Moon:
    def __init__(self, planet_mass, planet_size, orbit_index, seed):
        self.seed = seed
        self.size, self.mass, self.orbital_period = generate_moon_properties(planet_mass, planet_size, orbit_index, seed)
        self.name = None  # Will be set by PlanetarySystem

    def __str__(self):
        return (f"Moon {self.name}: Size: {self.size:.2f} Earth radii, "
                f"Mass: {self.mass:.4f} Earth masses, "
                f"Orbital Period: {self.orbital_period:.2f} Earth days")

def generate_moons(planet_mass, planet_size, seed):
    """Generate a list of moons for a planet."""
    moon_count = determine_moon_count(planet_mass, planet_size, seed)
    moons = []
    for i in range(moon_count):
        moon_seed = seed + i  # Ensure unique seed for each moon
        moons.append(Moon(planet_mass, planet_size, i, moon_seed))
    return moons

# Example usage
if __name__ == "__main__":
    from seed_generator import generate_initial_seed, generate_next_seed
    from star_generator import generate_star
    from planet_generator import generate_planets

    seed = generate_initial_seed()
    star = generate_star(seed)
    planets = generate_planets(star.mass, star.temperature, generate_next_seed(seed))
    
    print(star)
    for planet in planets:
        print(planet)
        moons = generate_moons(planet.mass, planet.size, generate_next_seed(planet.seed))
        for moon in moons:
            print(f"  {moon}")