# Create the last_books dictionary
last_books = {
   'Zara': 'Ender\'s Game',
   'Yuki': 'The Martian',
   'Axel': 'Ringworld'
}

# Print sentences about each friend's last read book
print(f"Zara's last read book was '{last_books['Zara']}'.")
print(f"Yuki's last read book was '{last_books['Yuki']}'.")
print(f"Axel's last read book was '{last_books['Axel']}'.")

# Add a new friend and their last read book
last_books['Nova'] = 'Neuromancer'

# Update the 'title' for one of the existing books
last_books['Yuki'] = 'Rendezvous with Rama'

# Remove one friend and their book information
del last_books['Axel']

# Print the final dictionary
print("\nUpdated last books information:")
print(last_books)