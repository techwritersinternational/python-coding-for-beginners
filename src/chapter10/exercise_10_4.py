def passenger_sign_in():
    """Handle passenger sign-in for space shuttle."""
    print("Space Shuttle Passenger Sign-In System")
    print("Enter 'quit' for passenger name to finish")
    print("-" * 50)
   
    # Get passenger information
    name = input("\nPassenger name: ").strip()
        
    destination = input("Destination: ").strip()
    
    # Format passenger entry
    entry = f"Name: {name}, Destination: {destination}"
    
    # Append to manifest file
    with open('passenger_manifest.txt', 'w') as manifest:
        manifest.write(entry + '\n')
    print("Passenger successfully registered.")
           
passenger_sign_in()