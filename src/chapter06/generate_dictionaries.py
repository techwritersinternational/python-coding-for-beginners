# filename: generate_dictionaries.py
# The empty starship dictionary that we'll use to store starship records
starships = {}

'''
starships = {
    'sdc001': nova_horizon,
    'gfi021': celestial_voyager,
    'sp011': stellar_phoenix
}
'''

# Generate 10 serial numbers
for serial_number in range(10):
    blank_starship = {
        'sdc00' + str(serial_number): 
        {'class': 'explorer', 'crew': 250}
    }
    starships.update(blank_starship)

# Print out the final database and how many starship records are ready
print(starships)
print(f"Total number of starships: {len(starships)}")

for serial_no, starship_details in starships.items():
    if starship_details.get('name') == None:
        starships[serial_no]['name'] = 'Nova Horizon'
        break

print(starships)

# Commission the Nova Horizon
for serial_no, starship_details in starships.items():
    if starship_details.get('name') == None:
        starships[serial_no]['name'] = 'Nova Horizon II'
        break

# Show the new ship in the catalog
print(starships)