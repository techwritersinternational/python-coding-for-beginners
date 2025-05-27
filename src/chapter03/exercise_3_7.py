# Start with your list of villains from Exercise 3-6
guests = ["Starspawn", "Admiral Tarquin", "Color Out of Space", "Martian Warboss", "Rocketra", "Xenomorph Queen", "Lady Starkiller", "Cyber Imperator", "Heat Death of the Universe"]

# Print message about the smaller table
print("I'm sorry, there isn't space for all of you.\n")

removed_guest = guests.pop()

print(f"Sorry, {removed_guest}. I can't invite you to the convention.\n")

print(guests)
