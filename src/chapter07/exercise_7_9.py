prohibited_items = ["particle accelerator", "black hole generator", "time machine", "antimatter", "warp drive"]
luggage = {}

print("Welcome to Galactic Space Lines Luggage Inspection!")
print("I'm here to ensure no prohibited items make it aboard our spacecraft.")

while True:
    passenger_name = input("\nPlease enter the passenger's name (or 'q' to quit): ").strip()
    if passenger_name.lower() == 'q':
        break
    
    luggage[passenger_name] = []
    
    while True:
        item = input(f"What item is {passenger_name} carrying? ").strip().lower()
        
        is_prohibited = False
        for prohibited in prohibited_items:
            if prohibited in item:
                print(f"I'm sorry, but '{item}' is not allowed on board.")
                is_prohibited = True
                break
        
        if not is_prohibited:
            luggage[passenger_name].append(item)
            print(f"'{item}' is allowed. It has been added to {passenger_name}'s luggage.")
        
        more_items = input("Are there more items to check? (yes/no): ").strip().lower()
        if more_items != 'yes':
            break

print("\nLuggage inspection complete. Here's a summary of allowed items:")
for passenger, items in luggage.items():
    if items:
        print(f"{passenger}: {', '.join(items)}")
    else:
        print(f"{passenger}: No allowed items")

print("\nThank you for choosing Galactic Space Lines. Have a safe journey!")