# Start with your list of villains
guests = ["Admiral Tarquin", "Color Out of Space", "Martian Warboss", "Xenomorph Queen", "Lady Starkiller", "Cyber Imperator"]

# Print the original guest list
print(f"Original guest list: {guests}")

# Add new villains
guests.insert(0, "Starspawn")
guests.insert(4, "Rocketra")
guests.append("Heat Death of the Universe")

# Print the updated guest list
print(f"\nUpdated guest list: {guests}")
