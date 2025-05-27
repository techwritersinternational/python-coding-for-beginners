available_supplies = ["oxygen tanks", "space suits", "food packs", "water containers", "medical kits"]
mission_supplies = {}

print("Welcome to the Orion Run Mission Supply Allocator!")
print("You need to allocate supplies for the mission to the Orion Nebula.")

while available_supplies:
    print("\nAvailable supplies:")
    for supply in available_supplies:
        print(f"{supply}")
    print("Enter 'q' to finish allocating.")
    
    choice = input("Which supply do you want to allocate? (Enter the number or name): ").lower()
    
    if choice == 'q':
        break
    
    if choice in available_supplies:
        chosen_supply = choice
    else:
        print("Invalid supply. Please try again.")
        continue
    
    quantity = input(f"How many {chosen_supply} do you want to allocate? ")
    if not quantity.isdigit() or int(quantity) <= 0:
        print("Please enter a positive number.")
        continue
    
    quantity = int(quantity)
    mission_supplies[chosen_supply] = quantity
    available_supplies.remove(chosen_supply)
    print(f"{quantity} {chosen_supply} allocated to the mission.")

print("\nMission supply allocation complete!")
if mission_supplies:
    print("Allocated supplies:")
    for supply, quantity in mission_supplies.items():
        print(f"- {supply}: {quantity}")
else:
    print("No supplies were allocated to the mission.")

if available_supplies:
    print("\nRemaining available supplies:")
    for supply in available_supplies:
        print(f"- {supply}")
else:
    print("\nAll supplies have been allocated.")

print("Good luck on your mission to the Orion Nebula!")