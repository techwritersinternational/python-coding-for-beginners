rock_age = 65  # Age of the rock in millions of years

if rock_age < 0.0117:
    epoch = "Holocene"
elif rock_age < 2.58:
    epoch = "Pleistocene"
elif rock_age < 5.333:
    epoch = "Pliocene"
elif rock_age < 23.03:
    epoch = "Miocene"
elif rock_age < 33.9:
    epoch = "Oligocene"
elif rock_age < 56:
    epoch = "Eocene"
elif rock_age < 66:
    epoch = "Paleocene"
else:
    epoch = "Predates Cenozoic Era"

print(f"A rock that is {rock_age} million years old is from the {epoch} epoch.")
