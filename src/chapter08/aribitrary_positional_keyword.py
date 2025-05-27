def space_mission(mission_name, *astronauts, **mission_details):
    print(f"Mission: {mission_name}")
    print("Crew:")
    for astronaut in astronauts:
        print(f"  - {astronaut}")
    print("Mission Details:")
    for detail, value in mission_details.items():
        print(f"  {detail.replace('_', ' ').title()}: {value}")

space_mission("Nova Expedition", "Zara Starling", "Kai Nebula",
   duration="6 months", destination="Mars", vehicle="Stellar Phoenix")