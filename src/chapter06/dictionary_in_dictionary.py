# filename: dictionary_in_dictionary.py
nova_horizon = {'name': 'Nova Horizon', 'class': 'Explorer', 'crew': 250}
celestial_voyager = {'name': 'Celestial Voyager', 'class': 'Cruiser', 'crew': 180}
stellar_phoenix = {'name': 'Stellar Phoenix', 'class': 'Hydroponic', 'crew': 500}

starships = {
    'sdc001': nova_horizon,
    'gfi021': celestial_voyager,
    'sp011': stellar_phoenix
}
'''
starships = {
    'sdc001': {
        'name': 'Nova Horizon', 
        'class': 'Explorer', 
        'crew': 250
    },
    'gfi021': {
        'name': 'Celestial Voyager', 
        'class': 'Cruiser', 
        'crew': 180
    },
    'sp011': {
        'name': 'Stellar Phoenix', 
        'class': 'Hydroponic', 
        'crew': 500
    }
}
'''

for id, details in starships.items():
    print(f"\nStarship {id} has the following details:")
   # Print each piece of information
    for key, value in details.items():
        print(f"\t{key.title()}: {value}")

for id, details in starships.items():
    print(f"\nStarship {id} has the following details:")
    # Print each piece of information
    print(f"\tName: {details['name']}")
    print(f"\tClass: {details['class']}")
    print(f"\tCrew: {details['crew']}")