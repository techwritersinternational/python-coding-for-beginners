cosmic_phenomena = []  # Start with an empty list

if cosmic_phenomena:
    favorite = 'Black Hole'
    if favorite in cosmic_phenomena:
        print(f"Wow! {favorite} is one of the cosmic phenomena in our list!")
    else:
        print(f"{favorite} is not in our list, but it's still an awesome choice!")
else:
    print("We don't have any cosmic phenomena in our list yet!")
    new_phenomenon = 'Quasar'
    cosmic_phenomena.append(new_phenomenon)
    print(f"Great! {new_phenomenon} has been added to our list of cosmic phenomena.")
