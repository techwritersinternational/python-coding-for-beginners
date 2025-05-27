total_travelers = 100
max_group_size = 10
min_group_size = 3

print(f"Welcome! We need to split {total_travelers} travelers into groups.")

# We ask for the number of groups and check if it is a digit
num_groups = input("How many groups would you like to create? ")
if not num_groups.isdigit():
    print("Please enter a whole positive number.")
    exit()

# It is a digit, so we then check if it's a valid number
num_groups = int(num_groups)

if num_groups <= 0:
    print("Please enter a positive number of groups.")
    exit()

if total_travelers / num_groups > max_group_size:
    print(f"That would make groups too large. The maximum group size is {max_group_size}.")
    exit()

if total_travelers / num_groups < min_group_size:
    print(f"That would make groups too small. The minimum group size is {min_group_size}.")
    exit()

# We need the size of each group as if we were dealing in round numbers
base_size = total_travelers // num_groups
# We'll then be able to add the remainder to each round number as we loop over the groups
remainder = total_travelers % num_groups

# Let's do the loop and add any remainders to the groups, one at a time
print("\nGroup sizes:")
for i in range(num_groups):
    if i < remainder:
        print(f"Group {i+1}: {base_size + 1} travelers")
    else:
        print(f"Group {i+1}: {base_size} travelers")

print("\nAll travelers have been assigned to groups. Safe travels!")