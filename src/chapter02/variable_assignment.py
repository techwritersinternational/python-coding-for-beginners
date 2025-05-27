x = 5
y = x
print(id(x))  # Outputs an integer (memory address)
print(id(y))  # Outputs the same integer as above

y = 10
print(id(x))  # Same as before
print(id(y))  # Different integer (new memory address)

word = "Programming"
print(word[0:4])  # Outputs: Prog
print(word[5:])   # Outputs: amming


print("He said, \"Hello!\"")  # Outputs: He said, "Hello!"
 