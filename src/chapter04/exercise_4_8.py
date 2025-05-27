# Create an empty list to store the cubes
cubes = []

# Calculate the first 10 cubes and add them to the list
for number in range(1, 11):
    cube = number ** 3
    cubes.append(cube)

# Print each cube in the list
for cube in cubes:
    print(cube)