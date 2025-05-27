import random

# Generate a random integer between 1 and 10
asteroid_size = random.randint(1, 10)
print(f"Encountered an asteroid of size: {asteroid_size}")

# Randomly select an item from a list
planet_types = ["Rocky", "Gas Giant", "Ice Giant", "Dwarf"]
discovered_planet = random.choice(planet_types)
print(f"Discovered a new {discovered_planet} planet!")

# Shuffle a list
crew_members = ["Captain", "Engineer", "Scientist", "Pilot"]
random.shuffle(crew_members)
print(f"Crew duty rotation: {crew_members}")

