# Create a list of cosmic locations
cosmic_locations = ['Andromeda Galaxy', 'Crab Nebula', 'Pillars of Creation', 'Betelgeuse', 'Europa']
# Print the original list
print("Cosmic locations I'd like to visit:")
print(cosmic_locations)
# Change an element
cosmic_locations[1] = 'Horsehead Nebula'
print("\nI'd rather go to the Horsehead Nebula than the Crab Nebula:")
print(cosmic_locations)
# Add elements
cosmic_locations.append('Proxima Centauri')
cosmic_locations.insert(2, 'Sagittarius A*')
print("\nAfter adding Proxima Centauri and Sagittarius A* to the wishlist:")
print(cosmic_locations)
# Remove elements
del cosmic_locations[3]
popped_location = cosmic_locations.pop()
cosmic_locations.remove('Betelgeuse')
print("\nI didn't fancy going to Pillars of Creation, Proxima Centauri, and Betelgeuse any more:")
print(cosmic_locations)
# Sort the list
print("\nSorted list:")
print(sorted(cosmic_locations))
print("Original list (still unsorted):")
print(cosmic_locations)
# Sort the list permanently
cosmic_locations.sort()
print("\nPermanently sorted list:")
print(cosmic_locations)
# Reverse the list
cosmic_locations.reverse()
print("\nReversed list:")
print(cosmic_locations)
# List length
print(f"\nNumber of cosmic locations in the list: {len(cosmic_locations)}")