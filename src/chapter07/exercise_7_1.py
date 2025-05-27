star_systems = {
    "Sol": "Our home system, with 8 planets.",
    "Alpha Centauri": "The closest star system to Sol, actually a triple star system.",
    "Sirius": "The brightest star in Earth's night sky, actually a binary star system.",
    "Epsilon Eridani": "A young star system, possibly hosting planets.",
}

chosen_system = input("Which star system would you like to learn about? ").title()

if chosen_system in star_systems:
    print(f"{chosen_system}: {star_systems[chosen_system]}")
else:
    print("Sorry, I don't have information about that star system.")

