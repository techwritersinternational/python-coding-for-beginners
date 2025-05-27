def spacecraft_status(**systems):
    print("Spacecraft Systems Status:")
    for system, status in systems.items():
        print(f"  {system.replace('_', ' ').title()}: {status}")

spacecraft_status(life_support="Optimal", propulsion="85% efficiency", navigation="Online")
