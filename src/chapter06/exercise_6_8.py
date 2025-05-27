starships = {
   'Nova Horizon': {'class': 'Explorer', 'length': 385.2, 'crew': 250, 'hyperdrive': 'Class 1.5'},
   'Celestial Voyager': {'class': 'Cruiser', 'length': 523.7, 'crew': 180, 'hyperdrive': 'Class 2'},
   'Stellar Phoenix': {'class': 'Arcology', 'length': 1200.0, 'crew': 500, 'hyperdrive': 'Class 3'},
   'Quantum Dart': {'class': 'Scout', 'length': 50.0, 'crew': 4, 'hyperdrive': 'Class 0.5'},
   'Nebula Seeker': {'class': 'Science Vessel', 'length': 275.5, 'crew': 120, 'hyperdrive': 'Class 2.5'}
}

large_crew_ships = []
# A short-hand way to do it, which we will do for the other examples
#large_crew_ships = [ship for ship, info in starships.items() if info['crew'] > 150]
for ship in starships:
    if starships[ship]['crew'] > 150:
        large_crew_ships.append(ship)
print("Ships with crew larger than 150:", large_crew_ships)

average_length = sum(ship['length'] for ship in starships.values()) / len(starships)
print(f"Average ship length: {average_length:.2f} meters")

# Set a really high value for this so we have something to compare
best_hyperdrive_class = float('inf')

for ship, info in starships.items():
    # Let's save this because we need it twice
    current_hyperdrive_class = float(info['hyperdrive'][6:])
    # First to check if it's a better drive than the best so far
    if current_hyperdrive_class < best_hyperdrive_class:
        # Second to remember its value if it is the best so far
        best_hyperdrive_class = current_hyperdrive_class
        best_hyperdrive_ship = ship

print(f"Ship with best hyperdrive: {best_hyperdrive_ship}")