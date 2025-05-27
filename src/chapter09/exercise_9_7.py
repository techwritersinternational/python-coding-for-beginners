class CrewMember:
   def __init__(self, name, specialization, years_experience):
       self.name = name
       self.specialization = specialization
       self.years_experience = years_experience


class Engineer(CrewMember):
   def __init__(self, name, years_experience, engineering_type):
       super().__init__(name, "Engineer", years_experience)
       self.engineering_type = engineering_type       


class Miner(CrewMember):
   def __init__(self, name, years_experience, mining_specialty):
       super().__init__(name, "Miner", years_experience)
       self.mining_specialty = mining_specialty
       

class Captain(CrewMember):
   def __init__(self, name, years_experience, command_rating):
       super().__init__(name, "Captain", years_experience)
       self.command_rating = command_rating
       

class MiningShip:
   def __init__(self, name):
       self.name = name
       self.captain = None
       self.crew = []
       print(f"Mining vessel {self.name} commissioned.")
   
   def assign_captain(self, captain):
       if isinstance(captain, Captain):
           self.captain = captain
           print(f"{captain.name} assigned as captain of {self.name}")
       else:
           print("Error: Must assign a Captain instance as captain")
   
   def add_crew_member(self, crew_member):
       if isinstance(crew_member, CrewMember):
           self.crew.append(crew_member)
           print(f"{crew_member.name} joined the crew of {self.name}")
       else:
           print("Error: Must add a CrewMember instance to crew")
   
   def list_crew(self):
       print(f"\nCrew Manifest of {self.name}:")
       if self.captain:
           print(f"Command: {self.captain.name}")
       else:
           print("No captain assigned")
       
       if self.crew:
           print("\nCrew Members:")
           for member in self.crew:
               print(f"- {member.name}")
       else:
           print("No crew members assigned")

# Create crew members
captain = Captain("Sarah Chen", 15, "A+")
engineer1 = Engineer("Marcus Rodriguez", 8, "Propulsion")
engineer2 = Engineer("Alex Patel", 5, "Systems")
miner1 = Miner("Jamie Wong", 12, "Deep Core")
miner2 = Miner("Val Thompson", 7, "Asteroid")

# Create mining ship
brown_dwarf = MiningShip("Brown Dwarf")

# Assign captain and crew
brown_dwarf.assign_captain(captain)
brown_dwarf.add_crew_member(engineer1)
brown_dwarf.add_crew_member(engineer2)
brown_dwarf.add_crew_member(miner1)
brown_dwarf.add_crew_member(miner2)

# Display crew manifest
brown_dwarf.list_crew()