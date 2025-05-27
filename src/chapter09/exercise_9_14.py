import random

class StellarEncounter:
   def __init__(self):
       self.star_types = [
           "Red Dwarf", "Yellow Dwarf", "Blue Giant",
           "White Dwarf", "Neutron Star", "Binary System"
       ]
       
       self.planet_types = [
           "Rocky", "Gas Giant", "Ice Giant",
           "Desert World", "Ocean World", "Volcanic World"
       ]
   
   def generate_star(self):
       """Generate a random star with type and temperature."""
       star_type = random.choice(self.star_types)
       temperature = random.randint(2000, 50000)
       
       return {
           'type': star_type,
           'temperature': temperature,
           'description': f"A {star_type} with surface temperature of {temperature}K"
       }
   
   def generate_planet(self):
       """Generate a random planet and determine habitability."""
       planet_type = random.choice(self.planet_types)
       is_habitable = random.random() < 0.1  # 10% chance
       
       atmosphere = random.choice([
           "no", "thin", "breathable", "toxic", "dense"
       ])
       
       size = random.randint(1000, 100000)  # km diameter
       
       return {
           'type': planet_type,
           'size': size,
           'atmosphere': atmosphere,
           'habitable': is_habitable,
           'description': self._generate_planet_description(
               planet_type, size, atmosphere, is_habitable
           )
       }
   
   def generate_asteroid(self):
       """Generate a random asteroid with designation and size."""
       designation = f"Asteroid-{random.randint(1, 9999):04d}"
       size = random.randint(1, 1000)
       composition = random.choice([
           "rocky", "metallic", "icy", "carbon-rich"
       ])
       
       return {
           'designation': designation,
           'size': size,
           'composition': composition,
           'description': f"A {size}m {composition} asteroid"
       }
   
   def _generate_planet_description(self, type, size, atmosphere, habitable):
       """Generate a detailed description for a planet."""
       desc = f"A {size}km diameter {type} planet with {atmosphere} atmosphere"
       if habitable:
           desc += " - POTENTIALLY HABITABLE!"
       return desc
   
   def random_encounter(self):
       """Generate a random stellar encounter."""
       print("\n=== Random Stellar Encounter Generated ===")
       
       # Generate objects
       star = self.generate_star()
       planet = self.generate_planet()
       asteroid = self.generate_asteroid()
       
       # Print encounter details
       print("\nStar Encountered:")
       print(star['description'])
       
       print("\nPlanet Detected:")
       print(planet['description'])
       
       print("\nAsteroid Detected:")
       print(asteroid['description'])
       
       return star, planet, asteroid


"""Simulate multiple stellar encounters."""
encounter_system = StellarEncounter()

num_encounters = 3

for i in range(num_encounters):
    print(f"\nENCOUNTER {i+1}")
    print("="* 50)
    encounter_system.random_encounter()
