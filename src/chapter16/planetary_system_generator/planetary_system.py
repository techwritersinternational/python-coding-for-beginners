from star_generator import generate_star
from planet_generator import generate_planets
from moon_generator import generate_moons
from seed_generator import generate_next_seed
from name_generator import generate_star_name, generate_planet_name, generate_moon_name

class PlanetarySystem:
    def __init__(self, seed):
        self.seed = seed
        self.star = generate_star(seed)
        self.star.name = generate_star_name(seed)
        self.planets = self.generate_system_planets()
        while not self.validate_system():
            self.seed = generate_next_seed(self.seed)
            self.planets = self.generate_system_planets()
        self.name = f"The {self.star.name} System"

    def generate_system_planets(self):
        planet_seed = generate_next_seed(self.seed)
        planets = generate_planets(self.star.mass, self.star.temperature, planet_seed)
        for i, planet in enumerate(planets):
            planet.name = generate_planet_name(self.star.name, i, generate_next_seed(planet_seed))
            moon_seed = generate_next_seed(planet.seed)
            planet.moons = generate_moons(planet.mass, planet.size, moon_seed)
            for j, moon in enumerate(planet.moons):
                moon.name = generate_moon_name(planet.name, j, generate_next_seed(moon_seed))
        return planets


    def validate_system(self):
        """Perform checks to ensure system stability and realism."""
        if not self.planets:
            return False  # System must have at least one planet

        # Check for minimum separation between planets
        for i in range(len(self.planets) - 1):
            if self.planets[i].orbital_period * 1.5 > self.planets[i+1].orbital_period:
                return False

        # Check that total planet mass is not too large compared to star
        total_planet_mass = sum(planet.mass for planet in self.planets)
        if total_planet_mass > 0.01 * self.star.mass * 333000:  # 333000 is approximate Earth masses in a solar mass
            return False

        # Check that innermost planet is not too close to the star
        if self.planets[0].orbital_period < 0.1:  # Arbitrary minimum of 0.1 Earth years
            return False

        # Check that outermost planet is not too far from the star
        if self.planets[-1].orbital_period > 100:  # Arbitrary maximum of 100 Earth years
            return False

        return True

    def __str__(self):
        system_info = [f"Planetary System: {self.name}", str(self.star)]
        for i, planet in enumerate(self.planets, 1):
            system_info.append(f"  Planet {i}: {planet}")
            for j, moon in enumerate(planet.moons, 1):
                system_info.append(f"    Moon {j}: {moon}")
        return "\n".join(system_info)

def generate_planetary_system(seed):
    """Generate a new planetary system."""
    return PlanetarySystem(seed)

# Example usage
if __name__ == "__main__":
    from seed_generator import generate_initial_seed

    seed = generate_initial_seed()
    system = generate_planetary_system(seed)
    print(system)