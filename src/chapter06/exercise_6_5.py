alien_cities = {
   'Under Croft': 'Kepler-186f',
   'Nebulor': 'Gliese 667Cc',
   'Quasar Prime': 'TRAPPIST-1e'
}

for city, planet in alien_cities.items():
   print(f"{city} is on planet {planet}.")

print("\nCities:")
for city in alien_cities.keys():
   print(city)

print("\nPlanets:")
for planet in alien_cities.values():
   print(planet)