supplies = []

print("Welcome, space traveler! Let's make a list of supplies for your journey.")
print("Enter the supplies you need, one at a time. Enter 'q' when you're finished.")

while True:
    # We get the input and strip any whitespace
    supply = input("Enter a supply (or 'q' to quit): ").strip()
    
    if supply.lower() == 'q':
        break
    
    # Warn the user that they've already added this item
    if supply in supplies:
        print(f"{supply} is already on your supply list.")
        continue

    # We want to add the supply only if it is a non-empty string 
    if supply:
        supplies.append(supply)
        print(f"Added '{supply}' to your supply list.")
    else:
        print("Please specify a supply to add.")
        continue

print("\nSupply list compilation complete.")

if not supplies:
    print("No supplies were added to the list.")
else:
    print("Here's your list of supplies:")
    for index, item in enumerate(supplies, 1):
        print(f"{index}. {item}")

print("\nSafe travels, space adventurer!")