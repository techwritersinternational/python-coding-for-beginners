from crew_members import Captain, Engineer, Miner

from spacecraft import MiningShip

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