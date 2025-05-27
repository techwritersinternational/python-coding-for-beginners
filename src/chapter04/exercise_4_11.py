# Start with the list of musicians
my_musicians = ['Nicki Minaj', 'Adele', 'Taylor Swift', 'Lady Gaga']
# Make a copy of the list
friend_musicians = my_musicians[:]
# Add a new musician to the original list
my_musicians.append('Ava Max')
# Add a different musician to the friend's list
friend_musicians.append('Ariana Grande')
# Print my favorite musicians
print("My favorite musicians are:")
for musician in my_musicians:
   print(musician)
# Print my friend's favorite musicians
print("\nMy friend's favorite musicians are:")
for musician in friend_musicians:
   print(musician)