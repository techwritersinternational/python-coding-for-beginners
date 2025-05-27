# Create an empty list
guests = []
# Add villains to the list
guests.append("Admiral Tarquin")
guests.append("Xenomorph Queen")
guests.insert(2, "Color Out of Space")
# Print first set of invitations
print("Original invitations:")
print(f"Greetings, {guests[0]}! You're invited to my intergalactic villains' summit.")
print(f"Greetings, {guests[1]}! You're invited to my intergalactic villains' summit.")
print(f"Greetings, {guests[2]}! You're invited to my intergalactic villains' summit.")

# Remove a villain who can't attend
print("\nOh no! The Xenomorph Queen can't make it.")
guests.remove("Xenomorph Queen")
# Add a new villain
guests.append("Martian Warboss")

# Print updated invitations
print("\nUpdated invitations:")
print(f"Greetings, {guests[0]}! You're invited to my intergalactic villains' summit.")
print(f"Greetings, {guests[1]}! You're invited to my intergalactic villains' summit.")
print(f"Greetings, {guests[2]}! You're invited to my intergalactic villains' summit.")
