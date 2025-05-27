# Create a list of places to visit in the universe
places = ['Andromeda Galaxy', 'Crab Nebula', 'Pillars of Creation', 'Betelgeuse', 'Europa']
# Print original list
print("Original order:")
print(places)
# Print sorted list without modifying the original list
print("\nAlphabetical order:")
print(sorted(places))
# Show list is still in original order
print("\nOriginal order:")
print(places)
# Print list in reverse alphabetical order without changing the original list
print("\nReverse alphabetical order:")
print(sorted(places, reverse=True))
# Show list is still in original order
print("\nOriginal order:")
print(places)
# Change the order of list using reverse()
places.reverse()
print("\nReversed order:")
print(places)
# Change the order of list back to original
places.reverse()
print("\nBack to original order:")
print(places)
# Change list to alphabetical order using sort()
places.sort()
print("\nSorted in alphabetical order:")
print(places)
# Change list to reverse alphabetical order using sort()
places.sort(reverse=True)
print("\nSorted in reverse alphabetical order:")
print(places)