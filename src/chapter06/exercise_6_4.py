# Create the starship dictionary
nova_horizon = {
   'name': 'Nova Horizon',
   'model': 'XR-7000',
   'manufacturer': 'Stellar Dynamics Corporation',
   'length': 385.2,
   'crew': 250
}

# Print each piece of information
for key, value in nova_horizon.items():
    print(f"{key}: {value}")

# Add new key-value pair
nova_horizon['max_speed'] = 'Light Speed 2.5'

# Modify the 'crew' value
nova_horizon['crew'] = 5

# Remove the 'manufacturer' key-value pair
del nova_horizon['manufacturer']

# Print the final dictionary
print("\nUpdated starship information:")
print(nova_horizon)