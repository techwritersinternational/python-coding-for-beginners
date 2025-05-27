cosmic_phenomena = ['Supernova', 'Black Hole', 'Neutron Star', 'Quasar']
for phenomenon in cosmic_phenomena:
   print(phenomenon)

cosmic_phenomena = ['Supernova', 'Black Hole', 'Neutron Star', 'Quasar']
for phenomenon in cosmic_phenomena:
   print(f"{phenomenon} is an awe-inspiring sight!")
   print(f"Observing a {phenomenon.lower()} requires advanced technology.\n")

print("\nThese are all the phenomena we're looking at.")

astronauts = ['Neil', 'Helen', 'Julie', 'Tim', 'Rakesh']
print(astronauts[0:3])
print(astronauts[1:4])
print(astronauts[:4])
print(astronauts[2:])
print(astronauts[-3:])

print("Here are the first three astronauts in the list:")
for astronaut in astronauts[:3]:
    print(astronaut)

original_astronauts = ['Neil', 'Helen', 'Julie', 'Tim', 'Rakesh']
copied_astronauts = original_astronauts[:]

print(original_astronauts)
print(copied_astronauts)

original_astronauts.append('Buzz')
copied_astronauts.append('Sara')

print(original_astronauts)
print(copied_astronauts)