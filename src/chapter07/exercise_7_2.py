vehicles = {
    "Space Pod": 2,
    "Space Shuttle": 7,
    "Transport Ship": 50,
    "Space Cruiser": 100
}

# We have two places we could use this, so set a reusable variable
invalid_message = "Invalid input. Please supply a positive whole number."

# Get the input, then check if it's a digit
num_passengers = input("How many passengers are in your group? ")
if not num_passengers.isdigit():
    print(invalid_message)
    exit()

# It is a digit, so convert it to an integer
num_passengers = int(num_passengers)

# Set the type of vehicle, only if there are more than zero passengers
if num_passengers <= 0:
    print(invalid_message)
    exit()
elif num_passengers <= 2:
    vehicle = "Space Pod"
elif num_passengers <= 7:
    vehicle = "Space Shuttle"
elif num_passengers <= 50:
    vehicle = "Transport Ship"
else:
    vehicle = "Space Cruiser"

print(f"Your group should use the {vehicle}.")

capacity = vehicles[vehicle]
# First check if we're under capacity
if num_passengers < capacity:
    empty_seats = capacity - num_passengers
    # The only over capacity is multiple Space Cruisers
elif num_passengers > capacity:
    cruisers_needed = (num_passengers + 99) // 100  
    print(f"You will need {cruisers_needed} Space Cruisers.")
    empty_seats = (cruisers_needed * 100) - num_passengers

if empty_seats > 0:
    seat_word = "seat" if empty_seats == 1 else "seats"
    print(f"There will be {empty_seats} empty {seat_word}.")
