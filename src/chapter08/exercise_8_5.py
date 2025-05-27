def describe_wonderful_place(name, feature, atmosphere, sights, detail_level="detailed"):
    description = f"Welcome to {name}, a truly remarkable place in our galaxy! "
    description += f"Its most striking feature is its {feature}. "

    if detail_level == "detailed":
        description += f"The atmosphere is {atmosphere}, creating an unforgettable ambiance. "
        description += f"Visitors can marvel at the {sights}. "

    print(description.strip())

# Test the function with different combinations of arguments

# Detailed description (default)
describe_wonderful_place(
    "Shoulder of Orion",
    "glittering c-beams",
    "filled with swirling nebulae",
    "Horsehead Nebula, Orion Nebula, Flame Nebula"
)

print("\n")

# Brief description
describe_wonderful_place(
    "The Pleiades",
    "cluster of hot, blue stars",
    "dusty and ethereal",
    "Seven Sisters, Merope Nebula",
    detail_level="brief"
)

print("\n")

# Minimal description
describe_wonderful_place(
    "Alpha Centauri",
    "closest star system to Earth",
    "similar to our solar system",
    "triple star system",
    detail_level="brief"
)