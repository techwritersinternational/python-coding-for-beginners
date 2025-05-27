def spacecraft_status(**systems):
    print("Spacecraft Systems Status:")
    for system, status in systems.items():
        print(f"  {system.replace('_', ' ').title()}: {status}")

