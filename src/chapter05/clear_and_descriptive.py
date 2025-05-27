# filename: clear_and_descriptive.py
# Less readable
a = 6
b = 9
c = 1

if a > 5 and b < 10 and c != 0:
    print("Validated")

# More readable
lower_limit = 6
upper_limit = 9
payment = 1

is_in_range = lower_limit > 5 and upper_limit < 10
is_valid = payment != 0
if is_in_range and is_valid:
    print("Validated")

condition1 = True
condition2 = True
condition3 = True

# Avoid this
if condition1:
    if condition2:
        if condition3:
            # do something
            print()

# Prefer this
if condition1 and condition2 and condition3:
    # do something
    print()