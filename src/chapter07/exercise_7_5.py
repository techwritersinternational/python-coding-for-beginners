max_capacity = 1000
current_load = 0
num_items = 0

print("Welcome, space trucker!")
print(f"Your truck can carry up to {max_capacity} units of cargo.")

while True:
    print(f"\nCurrent load: {current_load:.2f} units")
    print(f"Remaining capacity: {max_capacity - current_load:.2f} units")
    
    item_weight = input("Enter the weight of the next item (or 'q' to finish loading): ").strip().lower()
    
    if item_weight == 'q':
        break
    
    try:
        item_weight = float(item_weight)
        if item_weight <= 0:
            print("Weight must be a positive number. Please try again.")
            continue
        
        if current_load + item_weight > max_capacity:
            print("That item is too heavy! It would exceed the truck's capacity.")
            continue
        
        current_load += item_weight
        num_items += 1
        print(f"Added {item_weight:.2f} units to the truck.")
        
        if current_load == max_capacity:
            print("The truck is now full!")
            break
    except ValueError:
        print("Invalid input. Please enter a number or 'q' to quit.")

print("\nLoading complete. Here's your summary:")
print(f"Total weight loaded: {current_load:.2f} units")
print(f"Number of items loaded: {num_items}")

remaining_capacity = max_capacity - current_load
if remaining_capacity > 0:
    print(f"Remaining capacity: {remaining_capacity:.2f} units")
    print("The truck is not full.")
else:
    print("The truck is full to capacity!")