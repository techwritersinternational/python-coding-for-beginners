class LivingPlanet:
   def __init__(self, name, color, size):
       """Initialize the living planet.
       
       Parameters:
           name (str): Name of the planet
           color (str): Dominant color of the planet
           size (str): Size classification of the planet
       """
       self.name = name
       self.color = color
       self.size = size
       self.consciousness = True
       

# Create a living planet
gaia_prime = LivingPlanet("Gaia Prime", "emerald green", "medium")

print(f"{gaia_prime.name} is a {gaia_prime.size}, {gaia_prime.color} planet.")