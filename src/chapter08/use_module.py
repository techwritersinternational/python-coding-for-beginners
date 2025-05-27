import space_utils

def launch_spacecraft(*spacecraft):
    print(f"Launching {len(spacecraft)} spacecraft from local:")
    for craft in spacecraft:
        print(f"- {craft} is taking off!")

efficiency = space_utils.calculate_fuel_efficiency(100, 5)
space_utils.launch_spacecraft("Apollo", "Soyuz")

def calculate_fuel_consumption(distance, speed):
    '''
    Calculate the fuel consumption for a spacecraft.

    Parameters:
        distance (float): The distance traveled in kilometers.
        speed (float): The average speed in km/h.

    Returns:
        fuel_consumed (float): The amount of fuel consumed in liters.
    '''
    # Function body here
    pass

calculate_fuel_consumption(1.0, 50.0)