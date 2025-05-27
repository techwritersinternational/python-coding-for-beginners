# filename: multi_values_list_loop.py
nova_horizon = {
    'name': 'Nova Horizon', 
    'class': 'Explorer', 
    'crew': 250,
    'cargo': ['Rations', 'Water', 'Spacesuits']
}

print(f"The {nova_horizon['name']} is carrying the following cargo:")

for item in nova_horizon['cargo']:
    print(f"\t{item}")

nova_horizon = {
    'name': 'Nova Horizon', 
    'class': 'Explorer', 
    'crew': 250,
'cargo': [
    {'rations': 500}, 
    {'water': 1000}, 
    {'spacesuits': 300}]
}

print(f"The {nova_horizon['name']} is carrying the following cargo:")

for item in nova_horizon['cargo']:
    for key, value in item.items():
        print(f"\t{value} {key}")