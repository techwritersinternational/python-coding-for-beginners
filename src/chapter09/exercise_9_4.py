class MiningShip:
   def __init__(self, name, max_crew):
       """Initialize mining ship with name and crew capacity."""
       self.name = name
       self.max_crew = max_crew
       self.crew = []
       print(f"Mining ship {self.name} initialized. Maximum crew: {max_crew}")
   
   def add_crew(self, name, role="Crew"):
       """Add a crew member if there's space available."""
       if len(self.crew) >= self.max_crew:
           print(f"Cannot add {name}. {self.name} is at maximum crew capacity.")
           return False
       
       crew_member = {"name": name, "role": role}
       self.crew.append(crew_member)
           
       print(f"{name} has joined {self.name} as {role}")
       return True
   
   def remove_crew(self, name):
       """Remove a crew member from the ship."""
       for crew_member in self.crew:
           if crew_member["name"] == name:
               self.crew.remove(crew_member)
               print(f"Removed {name} from {self.name}.")
               return True
       
       print(f"{name} is not a crew member of {self.name}.")
       return False
   
   def list_crew(self):
       """Display all crew members and their roles."""
       print(f"\nCrew of {self.name}:")
       print(f"Current crew: {len(self.crew)}/{self.max_crew}")
       
       if not self.crew:
           print("No crew members aboard.")
           return
           
       for crew_member in self.crew:
           print(f"- {crew_member['name']}: {crew_member['role']}")
           

# Create the Brown Dwarf
brown_dwarf = MiningShip("Brown Dwarf", 4)

# Add crew members
brown_dwarf.add_crew("Sarah Chen", "Captain")
brown_dwarf.add_crew("Marcus Rodriguez", "Mining Engineer")
brown_dwarf.add_crew("Alex Patel", "Navigation Officer")
brown_dwarf.list_crew()

# Try to add more than capacity
brown_dwarf.add_crew("Jamie Wong", "Security Officer")
brown_dwarf.add_crew("Chris Bailey", "Engineer")  # Should fail

# Remove a crew member
brown_dwarf.remove_crew("Marcus Rodriguez")

# Try to remove non-existent crew member
brown_dwarf.remove_crew("Non Existent")

# Add new crew member to empty slot
brown_dwarf.add_crew("Val Thompson", "Mining Engineer")

# List final crew
brown_dwarf.list_crew()