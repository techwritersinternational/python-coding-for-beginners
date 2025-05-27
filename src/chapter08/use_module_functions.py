from space_utils import calculate_fuel_efficiency, launch_spacecraft

def launch_spacecraft(*spacecraft):
    print(f"Launching {len(spacecraft)} spacecraft from local:")
    for craft in spacecraft:
        print(f"- {craft} is taking off!")

efficiency = calculate_fuel_efficiency(100, 5)
launch_spacecraft("Apollo", "Soyuz")

