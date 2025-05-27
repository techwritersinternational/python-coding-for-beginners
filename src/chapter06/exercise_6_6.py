alien_cities = {
   'Under Croft': 'Kepler-186f',
   'Nebulor': 'Gliese 667Cc',
   'Quasar Prime': 'TRAPPIST-1e'
}

hottest_destinations = ['Nebulor', 'Quasar Prime']

for city in alien_cities.keys():
   if city in hottest_destinations:
       print(f"{city} is a recommended place to visit. It is on planet {alien_cities[city]}.")

