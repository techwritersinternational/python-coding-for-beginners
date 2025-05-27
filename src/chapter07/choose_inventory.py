inventory = ["space suit", "helmet", "boots", "gloves", "oxygen tank"]
equipped = []

print("Your inventory:", inventory)

while inventory:
    item = input("What item do you want to equip? (or 'q' to quit) ")
    if item.lower() == 'q':
        break
    if item in inventory:
        inventory.remove(item)
        equipped.append(item)
        print(f"Equipped: {item}")
    else:
        print("That item is not in your inventory.")

print("\nFinal inventory:", inventory)
print("Equipped items:", equipped)