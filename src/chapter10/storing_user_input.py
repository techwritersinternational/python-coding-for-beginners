import json

def get_user_input():
    """Get and validate user input."""
    data = {}
    
    # Get name
    name = input("Enter your name: ")
    data['name'] = name
    
    # Get and validate age
    while True:
        try:
            age = input("Enter your age: ")
            data['age'] = int(age)
            break
        except ValueError as e:
            print("Please enter a valid age using only digits.")
    
    # Get favorite planet
    planet = input("Enter your favorite planet: ")
    data['favorite_planet'] = planet
    
    return data

def save_user_data(data, filename='user_preferences.json'):
    """Save user data to a JSON file."""
    try:
        # Save the data
        with open(filename, 'w') as user_file:
            json.dump(data, user_file, indent=4)
        print("User data saved successfully!")
        
    except IOError as e:
        print(f"Error saving data: {e}")


print("Welcome to the User Preferences System!")
print("-" * 40)

user_data = get_user_input()
save_user_data(user_data)
