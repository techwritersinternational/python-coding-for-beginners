num_doors = 5
exit_door = 3
attempts = 0

print("Welcome to the Space Station Escape!")
print(f"You're trapped in a space station with {num_doors} doors, but only one leads to freedom.")
print("Can you find the exit before you run out of oxygen?")

while True:
    print(f"\nYou are facing {num_doors} doors numbered 1 to {num_doors}.")
    choice = input("Which door do you choose? ")
    
    attempts += 1
    
    if not choice.isdigit():
        print("Invalid input. Please enter a number.")
        continue
    
    choice = int(choice)
    
    if choice < 1 or choice > num_doors:
        print(f"Invalid door number. Please choose a number between 1 and {num_doors}.")
        continue
    
    if choice == exit_door:
        print("Congratulations! You've found the exit!")
        break
    else:
        print("This isn't the exit. Try another door!")

print(f"\nYou escaped in {attempts} attempts!")
if attempts == 1:
    print("Incredible! You found the exit on your first try!")
elif attempts <= 3:
    print("Great job! That was quick thinking!")
else:
    print("Phew! That was a close one, but you made it out safely.")

print("Thanks for playing Space Station Escape!")