active = True
count = 0
max_turns = 5

while active:
    count += 1
    response = input("Enter a command (type 'quit' to exit): ")
    if response.lower() == "quit":
        break
    elif not count == max_turns:
        print(f"You entered: {response}")
        print(f"You have {max_turns - count} turns remaining.")
    else:
        active = False

print("Thanks for using our program!")