from crew_members import CrewMember, Captain

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

