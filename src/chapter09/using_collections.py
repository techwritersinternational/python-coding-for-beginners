from collections import namedtuple, Counter

# Create a named tuple for storing planet data
Planet = namedtuple('Planet', ['name', 'type', 'moons'])

mars = Planet('Mars', 'Rocky', 2)
print(f"{mars.name} is a {mars.type} planet with {mars.moons} moons.")

# Count occurrences in a list
asteroid_sizes = [2, 1, 3, 2, 4, 2, 3, 1, 2]
size_counts = Counter(asteroid_sizes)
print(f"Asteroid size distribution: {dict(size_counts)}")