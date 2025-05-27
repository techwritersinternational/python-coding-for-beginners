class CrewMember:
   def __init__(self, name, rank):
       self.name = name
       self.rank = rank
       self.permissions = {'general_areas': True}
   
   def check_permission(self, permission):
       return self.permissions.get(permission, False)
   

class Engineer(CrewMember):
   def __init__(self, name):
       super().__init__(name, "Engineer")
       self.permissions.update({
           'engine_room': True,
           'maintenance': True,
           'systems_control': True
       })

class SecurityOfficer(CrewMember):
   def __init__(self, name):
       super().__init__(name, "Security Officer")
       self.permissions.update({
           'weapons': True,
           'security_office': True,
           'brig': True
       })

class Captain(CrewMember):
   def __init__(self, name):
       super().__init__(name, "Captain")
       self.permissions.update({
           'bridge': True,
           'all_areas': True,
           'override_controls': True,
           'weapons': True,
           'engine_room': True
       })

class Spaceship:
   def __init__(self, name):
       self.name = name
       self.crew = []
       print(f"Spaceship {self.name} initialized.")
   
   def add_crew_member(self, crew_member):
       self.crew.append(crew_member)
       print(f"{crew_member.name} added to crew of {self.name}")
   
   def check_access(self, crew_member, area):
       if crew_member not in self.crew:
           print(f"{crew_member.name} is not a crew member of {self.name}")
           return False
           
       has_permission = crew_member.check_permission(area)
       
       print(f"\nAccess request for {area}:")
       print(f"Crew member: {crew_member.name}")
       print(f"Access {'granted' if has_permission else 'denied'}")
       
       return has_permission

# Create the spaceship
nova = Spaceship("Nova")

# Create crew members
captain = Captain("Sarah Chen")
engineer = Engineer("Marcus Rodriguez")
security = SecurityOfficer("Alex Patel")

# Add crew to ship
nova.add_crew_member(captain)
nova.add_crew_member(engineer)
nova.add_crew_member(security)

# Test permissions
print("\nTesting access permissions:")

# Test captain's access
nova.check_access(captain, "bridge")
nova.check_access(captain, "engine_room")
nova.check_access(captain, "weapons")

# Test engineer's access
nova.check_access(engineer, "engine_room")
nova.check_access(engineer, "bridge")  # Should be denied
nova.check_access(engineer, "weapons")  # Should be denied

# Test security officer's access
nova.check_access(security, "weapons")
nova.check_access(security, "engine_room")  # Should be denied
nova.check_access(security, "brig")