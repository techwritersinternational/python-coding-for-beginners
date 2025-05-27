active = True
count = 0
max_turns = 5

while active:
    count += 1
    response = input("Enter a command (type 'quit' to exit): ")
    if response.lower() == "quit":
        active = False
    else:
        print(f"You entered: {response}")

    if count == max_turns:
        active = False

    print(f"You have {max_turns - count} turns remaining.")

print("Thanks for using our program!")