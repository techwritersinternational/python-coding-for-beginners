class MiningShip:
   def __init__(self, name):
       self.name = name
       self.hull_integrity = 100
       self.asteroid_strikes = 0
       print(f"Mining ship {self.name} launched. Hull integrity: {self.hull_integrity}%")
   
   def asteroid_strike(self, asteroid_mass):
       self.asteroid_strikes += 1
       damage = asteroid_mass * 5  # More mass = more damage
       
       print(f"\nAlert! Asteroid strike detected!")
       print(f"Mass: {asteroid_mass} tons")
       
       self.update_hull_integrity(-damage)
   
   def update_hull_integrity(self, change):
       self.hull_integrity += change
       
       # Keep hull integrity between 0 and 100
       self.hull_integrity = max(0, min(100, self.hull_integrity))
       
       if change < 0:
           print(f"Hull damage sustained: {change}%")
       else:
           print(f"Hull repaired: +{change}%")
           
       print(f"Hull integrity: {self.hull_integrity}%")
       
       if self.hull_integrity <= 0:
           print("CRITICAL: Hull breach!")
       elif self.hull_integrity < 25:
           print("WARNING: Hull integrity critical!")
       elif self.hull_integrity < 50:
           print("CAUTION: Hull integrity low.")
   
   def print_status(self):
       print(f"\n=== {self.name} Status Report ===")
       print(f"Asteroid strikes sustained: {self.asteroid_strikes}")
       print(f"Current hull integrity: {self.hull_integrity}%")
       
       if self.hull_integrity == 100:
           print("Ship status: Excellent")
       elif self.hull_integrity >= 75:
           print("Ship status: Good")
       elif self.hull_integrity >= 50:
           print("Ship status: Fair")
       elif self.hull_integrity >= 25:
           print("Ship status: Poor")
       else:
           print("Ship status: Critical")

# Create the Brown Dwarf
brown_dwarf = MiningShip("Brown Dwarf")

# Simulate asteroid field
print("\nEntering asteroid field...")
brown_dwarf.asteroid_strike(3)  # Small asteroid
brown_dwarf.asteroid_strike(8)  # Medium asteroid
brown_dwarf.asteroid_strike(2)  # Small asteroid

# Print status after asteroid field
brown_dwarf.print_status()

# Repair ship
print("\nDocking for repairs...")
repair_needed = 100 - brown_dwarf.hull_integrity
brown_dwarf.update_hull_integrity(repair_needed)

# Print final status
brown_dwarf.print_status()