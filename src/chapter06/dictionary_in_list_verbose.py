# filename: dictionary_in_list_verbose.py
nova_horizon = {'name': 'Nova Horizon', 'class': 'Explorer', 'crew': 250}
celestial_voyager = {'name': 'Celestial Voyager', 'class': 'Cruiser', 'crew': 180}
stellar_phoenix = {'name': 'Stellar Phoenix', 'class': 'Hydroponic', 'crew': 500}

starships = [nova_horizon, celestial_voyager, stellar_phoenix]

for starship in starships:
    print()
   # Print each piece of information
    for key, value in starship.items():
        print(f"{key}: {value}")