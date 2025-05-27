starships = {
   'Nova Horizon': {
       'model': 'Explorer-class',
       'length': 385.2,
       'crew': [
           {'name': 'Elena Vega', 'position': 'Captain', 'age': 34},
           {'name': 'Zorn Laroo', 'position': 'Engineer', 'age': 45},
           {'name': 'Lyra Starwind', 'position': 'Navigator', 'age': 21}
       ]
   },
   'Celestial Voyager': {
       'model': 'Cruiser-class',
       'length': 523.7,
       'crew': [
           {'name': 'Kai Chang', 'position': 'Commander', 'age': 54},
           {'name': 'T\'Lek Mackay', 'position': 'Science Officer', 'age': 39},
           {'name': 'Rax Starblaze', 'position': 'Tactical Officer', 'age': 63}
       ]
   }
}

# Print all information
for ship_name, ship_info in starships.items():
   print(f"\nStarship: {ship_name}")
   print(f"Model: {ship_info['model']}")
   print(f"Length: {ship_info['length']} meters")
   print("Crew:")
   for crew_member in ship_info['crew']:
       print(f"  - {crew_member['name']}, {crew_member['position']}, {crew_member['age']}")

# Add a new crew member
starships['Nova Horizon']['crew'].append({
   'name': 'Aria Moonwhisper',
   'position': 'Medical Officer',
   'age': 56
})

# Bonus: Transfer crew member
transferred_crew = starships['Celestial Voyager']['crew'].pop(1)
starships['Nova Horizon']['crew'].append(transferred_crew)

print("\nAfter changes:")
for ship_name, ship_info in starships.items():
   print(f"\nStarship: {ship_name}")
   print("Crew:")
   for crew_member in ship_info['crew']:
       print(f"  - {crew_member['name']}, {crew_member['position']}, {crew_member['age']}")