# filename: exercise_5_2.py
# Tests for equality and inequality with strings
planet = "Mars"
print("Is planet == 'Mars'? I predict True.")
print(planet == "Mars")

print("\nIs planet != 'Earth'? I predict True.")
print(planet != "Earth")

# Tests using the lower() method
spacecraft = "VOYAGER"
print("\nIs spacecraft.lower() == 'voyager'? I predict True.")
print(spacecraft.lower() == "voyager")

# Numerical tests
astronauts = 5
print("\nIs astronauts > 3? I predict True.")
print(astronauts > 3)

print("\nIs astronauts <= 4? I predict False.")
print(astronauts <= 4)

# Tests using "and" and "or" operators
fuel = 50
oxygen = 80
print("\nIs fuel > 40 and oxygen > 70? I predict True.")
print(fuel > 40 and oxygen > 70)

print("\nIs fuel > 60 or oxygen > 70? I predict True.")
print(fuel > 60 or oxygen > 70)

# Test whether an item is in a list
planets = ["Mars", "Venus", "Jupiter"]
print("\nIs 'Earth' in planets? I predict False.")
print("Earth" in planets)

# Test whether an item is not in a list
print("\nIs 'Saturn' not in planets? I predict True.")
print("Saturn" not in planets)