# Read all lines into memory and reverse
def reverse_log(filename):
   print("Reading all lines and reversing\n")
   with open(filename, 'r') as log_file:
       lines = log_file.readlines()
       
   for line in reversed(lines):
       print(line.strip())

input_file = 'spaceship_log.txt'

# Reverse the log
reverse_log(input_file)
