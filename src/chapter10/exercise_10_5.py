def passenger_sign_in():
   """Handle passenger sign-in for space shuttle."""
   print("Space Shuttle Passenger Sign-In System")
   print("Enter 'quit' for passenger name to finish")
   print("-" * 50)
   
   while True:
        # Get passenger information
        name = input("\nPassenger name: ").strip()
        if name.lower() == 'quit':
           break
           
        destination = input("Destination: ").strip()
       
        # Format passenger entry
        entry = f"Name: {name}, Destination: {destination}"
       
        # Append to manifest file
        with open('passenger_manifest.txt', 'a') as manifest:
            manifest.write(entry + '\n')
        print("Passenger successfully registered.")
                          

while True:
    print("\nSpace Shuttle Registration System")
    print("1. Sign in new passenger")
    print("2. Exit")
    
    choice = input("Select option (1 or 2): ")
    
    if choice == '1':
        passenger_sign_in()
    elif choice == '2':
        print("\nExiting system. Safe travels!")
        break
    else:
        print("Invalid option. Please try again.")
