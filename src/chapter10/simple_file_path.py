# Open a file named 'example.txt' in the current directory
with open('example.txt', 'r') as file:
    contents = file.read()
    print(contents)