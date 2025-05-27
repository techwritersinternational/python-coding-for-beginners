crew = ["Engineer", "Pilot", "Navigator", "Engineer", "Science Officer"]

print("Current crew:", crew)

while True:
    member = input("Enter a crew member to remove (or 'q' to quit): ")
    if member.lower() == 'q':
        break
    elif not member in crew:
        print(f"{member} is not in the crew.")
        continue
    while member in crew:
        crew.remove(member)
    else:
        print(f"{member} has been removed from the crew.")

print("\nFinal crew:", crew)