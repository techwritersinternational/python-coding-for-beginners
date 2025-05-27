# Start with your list of villains
guests = ["Admiral Tarquin", "Color Out of Space", "Martian Warboss"]
# Print the original guest list
print(f"Original guest list: {guests}")
# Change the second villain
guests[1] = "Lady Starkiller"
# Print the updated guest list
print(f"\nUpdated guest list: {guests}")
# Print new invitation messages
print("\nNew invitations:")
print(f"Greetings, {guests[0]}! You're invited to my intergalactic villains' summit.")
print(f"Greetings, {guests[1]}! You're invited to my intergalactic villains' summit.")
print(f"Greetings, {guests[2]}! You're invited to my intergalactic villains' summit.")
