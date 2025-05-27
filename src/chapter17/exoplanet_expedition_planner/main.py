from config import NASA_API_KEY, BASE_URL

import urllib.parse

import requests

from exoplanet import Exoplanet

import math

from requests.exceptions import RequestException, Timeout, TooManyRedirects

def construct_query_url(select_fields, where_conditions=None, order_by=None):
    base_query = f"select {','.join(select_fields)} from ps"
    
    if where_conditions:
        base_query += f" where {' and '.join(where_conditions)}"
    
    if order_by:
        base_query += f" order by {order_by}"
     
    encoded_query = urllib.parse.quote(base_query)
    return f"{BASE_URL}?query={encoded_query}" \
        f"&format=json&api_key={NASA_API_KEY}"

def fetch_exoplanet_data(url, max_retries=3):
    for attempt in range(max_retries):
        try:
            response = requests.get(url, timeout=10)
            response.raise_for_status()
            return response.json()
        except Timeout:
            print(f"Request timed out. Attempt {attempt + 1} of {max_retries}")
        except TooManyRedirects:
            print("Too many redirects. Please check the URL.")
            return None
        except RequestException as e:
            print(f"An error occurred while fetching data: {e}")
            if attempt == max_retries - 1:
                print("Max retries reached. Unable to fetch data.")
                return None
    return None


def get_exoplanet_data(select_fields, where_conditions=None, order_by=None):
    url = construct_query_url(select_fields, where_conditions, order_by)
    json_data = fetch_exoplanet_data(url)
    return parse_exoplanet_data(json_data)


def parse_exoplanet_data(json_data):
    if not json_data:
        return []
    
    exoplanets = []
    for row in json_data:
        exoplanet = Exoplanet(
            name=row.get('pl_name'),
            host_star=row.get('hostname'),
            mass=row.get('pl_bmassj'),
            radius=row.get('pl_rade'),
            orbital_period=row.get('pl_orbper'),
            equilibrium_temp=row.get('pl_eqt'),
            distance=row.get('sy_dist'),
            discovery_year=row.get('disc_year')
        )
        exoplanets.append(exoplanet)
    
    return exoplanets


def search_exoplanets(mass_min=None, mass_max=None, radius_min=None, radius_max=None, 
                      temp_min=None, temp_max=None, distance_max=None, 
                      discovery_year_min=None, order_by=None):
    select_fields = ['pl_name', 'hostname', 'pl_bmassj', 'pl_rade', 'pl_orbper', 'pl_eqt', 'sy_dist', 'disc_year']
    conditions = []

    if mass_min is not None:
        conditions.append(f'pl_bmassj >= {mass_min}')
    if mass_max is not None:
        conditions.append(f'pl_bmassj <= {mass_max}')
    if radius_min is not None:
        conditions.append(f'pl_rade >= {radius_min}')
    if radius_max is not None:
        conditions.append(f'pl_rade <= {radius_max}')
    if temp_min is not None:
        conditions.append(f'pl_eqt >= {temp_min}')
    if temp_max is not None:
        conditions.append(f'pl_eqt <= {temp_max}')
    if distance_max is not None:
        conditions.append(f'sy_dist <= {distance_max}')
    if discovery_year_min is not None:
        conditions.append(f'disc_year >= {discovery_year_min}')

    return get_exoplanet_data(select_fields, conditions, order_by)

def display_exoplanet_results(exoplanets):
    if not exoplanets:
        print("No exoplanets found matching the criteria.")
        return

    print(f"\nFound {len(exoplanets)} exoplanets:\n")
    for planet in exoplanets:
        print(f"Name: {planet.name}")
        print(f"Host Star: {planet.host_star}")
        print(f"Mass: {planet.mass:.2f} Jupiter masses" if planet.mass else "Mass: Unknown")
        print(f"Radius: {planet.radius:.2f} Earth radii" if planet.radius else "Radius: Unknown")
        print(f"Orbital Period: {planet.orbital_period:.2f} days" if planet.orbital_period else "Orbital Period: Unknown")
        print(f"Equilibrium Temperature: {planet.equilibrium_temp:.2f} K" if planet.equilibrium_temp else "Equilibrium Temperature: Unknown")
        print(f"Distance: {planet.distance:.2f} parsecs" if planet.distance else "Distance: Unknown")
        print(f"Discovery Year: {planet.discovery_year}")
        print(f"Surface Gravity: {planet.surface_gravity():.2f} m/s^2" if planet.surface_gravity() else "Surface Gravity: Unknown")
        print(f"Habitability: {planet.is_potentially_habitable()}")
        print(f"Earth Years per Orbit: {planet.earth_years_per_orbit():.2f}" if planet.earth_years_per_orbit() else "Earth Years per Orbit: Unknown")
        print("-" * 50)

def main_search():
    print("Welcome to the Exoplanet Search!")
    
    mass_min = float(input("Minimum mass (Jupiter masses, or press Enter to skip): ") or 0)
    mass_max = float(input("Maximum mass (Jupiter masses, or press Enter to skip): ") or 1000)
    radius_min = float(input("Minimum radius (Earth radii, or press Enter to skip): ") or 0)
    radius_max = float(input("Maximum radius (Earth radii, or press Enter to skip): ") or 1000)
    temp_min = float(input("Minimum temperature (Kelvin, or press Enter to skip): ") or 0)
    temp_max = float(input("Maximum temperature (Kelvin, or press Enter to skip): ") or 10000)
    distance_max = float(input("Maximum distance (parsecs, or press Enter to skip): ") or 1000000)
    discovery_year_min = int(input("Minimum discovery year (or press Enter to skip): ") or 1990)

    search_params = {
        'mass_min': mass_min, 'mass_max': mass_max,
        'radius_min': radius_min, 'radius_max': radius_max,
        'temp_min': temp_min, 'temp_max': temp_max,
        'distance_max': distance_max,
        'discovery_year_min': discovery_year_min,
        'order_by': 'pl_bmassj desc'
    }

    results = search_exoplanets(mass_min=search_params['mass_min'], mass_max=search_params['mass_max'],
        radius_min=search_params['radius_min'], radius_max=search_params['radius_max'], temp_min=search_params['temp_min'], temp_max=search_params['temp_max'], distance_max=search_params['distance_max'], discovery_year_min=search_params['discovery_year_min'], order_by=search_params['order_by'])

    display_exoplanet_results(results)

    if results:
        while True:
            choice = input("\nEnter the number of the exoplanet you'd like to plan a mission to (or 'q' to quit): ")
            if choice.lower() == 'q':
                break
            try:
                index = int(choice) - 1
                if 0 <= index < len(results):
                    mission_profile = plan_mission(results[index])
                    # Here you could save the mission profile to a file if desired
                else:
                    print("Invalid selection. Please try again.")
            except ValueError:
                print("Invalid input. Please enter a number or 'q' to quit.")



def calculate_travel_time(distance_parsecs, speed_fraction_of_c):
    """
    Calculate travel time to an exoplanet.
    
    :param distance_parsecs: Distance to the exoplanet in parsecs
    :param speed_fraction_of_c: Speed of the spacecraft as a fraction of the speed of light
    :return: Travel time in years
    """
    light_year_in_km = 9.461e12  # km in a light year
    parsec_in_light_years = 3.26156  # light years in a parsec
    
    distance_km = distance_parsecs * parsec_in_light_years * light_year_in_km
    speed_km_per_year = speed_fraction_of_c * light_year_in_km
    
    travel_time_years = distance_km / speed_km_per_year
    
    return travel_time_years

def estimate_resources(travel_time_years, crew_size):
    """
    Estimate resource requirements for the mission.
    """
    food_per_person_per_year = 500  # kg
    water_per_person_per_year = 1000  # kg
    oxygen_per_person_per_year = 300  # kg
    
    total_food = math.ceil(food_per_person_per_year * crew_size * travel_time_years)
    total_water = math.ceil(water_per_person_per_year * crew_size * travel_time_years)
    total_oxygen = math.ceil(oxygen_per_person_per_year * crew_size * travel_time_years)
    
    return {
        "food_kg": total_food,
        "water_kg": total_water,
        "oxygen_kg": total_oxygen
    }


def generate_mission_profile(exoplanet, speed_fraction_of_c, crew_size):
    """
    Generate a basic mission profile for an exoplanet expedition.
    """
    if exoplanet.distance is None:
        return {"error": "Distance to exoplanet is unknown"}
    
    travel_time = calculate_travel_time(exoplanet.distance, speed_fraction_of_c)
    resources = estimate_resources(travel_time, crew_size)
    
    return {
        "destination": exoplanet.name,
        "distance_parsecs": exoplanet.distance,
        "travel_time_years": travel_time,
        "spacecraft_speed": f"{speed_fraction_of_c:.2f}c",
        "crew_size": crew_size,
        "resources_required": resources,
        "exoplanet_data": exoplanet.to_dict()
    }


def plan_mission(exoplanet):
    print(f"\nPlanning mission to {exoplanet.name}")
    
    speed_fraction_of_c = float(input("Enter spacecraft speed as a fraction of light speed (e.g., 0.1 for 10% of light speed): "))
    crew_size = int(input("Enter the number of crew members: "))
    
    mission_profile = generate_mission_profile(exoplanet, speed_fraction_of_c, crew_size)
    
    print("\nMission Profile:")
    print(f"Destination: {mission_profile['destination']}")
    print(f"Distance: {mission_profile['distance_parsecs']:.2f} parsecs")
    print(f"Travel Time: {mission_profile['travel_time_years']:.2f} years")
    print(f"Spacecraft Speed: {mission_profile['spacecraft_speed']}")
    print(f"Crew Size: {mission_profile['crew_size']}")
    print("\nResource Requirements:")
    print(f"Food: {mission_profile['resources_required']['food_kg']:,} kg")
    print(f"Water: {mission_profile['resources_required']['water_kg']:,} kg")
    print(f"Oxygen: {mission_profile['resources_required']['oxygen_kg']:,} kg")
    
    return mission_profile

if __name__ == "__main__":
    main_search()

