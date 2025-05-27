class SentientStellarObject:
   """Base class for all sentient stellar objects."""
   
   def __init__(self, name, consciousness_level, primary_thought):
       self.name = name
       self.consciousness_level = consciousness_level  # 1-10
       self.primary_thought = primary_thought
       self.children = []  # for orbiting bodies
       
   def broadcast_thought(self):
       print(f"{self.name} contemplates: {self.primary_thought}")
       
   def add_orbiting_body(self, body):
       self.children.append(body)
       print(f"{body.name} now orbits {self.name}")
       
   def list_children(self):
       if not self.children:
           print(f"{self.name} has no orbiting bodies.")
       else:
           print(f"\nBodies orbiting {self.name}:")
           for child in self.children:
               print(f"- {child.name}")


class SentientStar(SentientStellarObject):
   def __init__(self, name, consciousness_level, primary_thought, stellar_type):
       super().__init__(name, consciousness_level, primary_thought)
       self.stellar_type = stellar_type
       

class SentientPlanet(SentientStellarObject):
   def __init__(self, name, consciousness_level, primary_thought, biosphere_type):
       super().__init__(name, consciousness_level, primary_thought)
       self.biosphere_type = biosphere_type
       

class SentientMoon(SentientStellarObject):
   def __init__(self, name, consciousness_level, primary_thought, surface_type):
       super().__init__(name, consciousness_level, primary_thought)
       self.surface_type = surface_type
       

# Create instances
prajna = SentientStar("Prajna", 10, 
   "I warm all my children with eternal fire.", 
   "Yellow Dwarf")

chaitanya = SentientPlanet("Chaitanya", 8, 
   "My forests dream of reaching the stars.", 
   "Living Forest")

tejas = SentientMoon("Tejas", 6, 
   "I reflect on the beauty of my planet.", 
   "Crystalline")

# Set up orbital relationships
prajna.add_orbiting_body(chaitanya)
chaitanya.add_orbiting_body(tejas)

# Have each object broadcast its thoughts
print("\nThoughts of the stellar objects:")
prajna.broadcast_thought()
chaitanya.broadcast_thought()
tejas.broadcast_thought()

# List orbital relationships
print("\nOrbital relationships:")
prajna.list_children()
chaitanya.list_children()
tejas.list_children()