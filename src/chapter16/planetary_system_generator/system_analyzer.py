from collections import Counter

def analyze_system(system):
    """Analyze a single planetary system and return key statistics."""
    stats = {
        "star_type": system.star.type.name,
        "star_mass": system.star.mass,
        "star_temperature": system.star.temperature,
        "planet_count": len(system.planets),
        "habitable_planet_count": sum(1 for planet in system.planets if planet.habitable),
        "total_moon_count": sum(len(planet.moons) for planet in system.planets),
        "largest_planet_size": max(planet.size for planet in system.planets) if system.planets else 0,
    }
    return stats

def analyze_multiple_systems(systems):
    """Analyze multiple planetary systems and return aggregate statistics."""
    all_stats = [analyze_system(system) for system in systems]
    
    aggregate_stats = {
        "total_systems": len(systems),
        "star_type_distribution": Counter(stat["star_type"] for stat in all_stats),
        "avg_planets_per_system": sum(stat["planet_count"] for stat in all_stats) / len(systems),
        "avg_habitable_planets_per_system": sum(stat["habitable_planet_count"] for stat in all_stats) / len(systems),
        "avg_moons_per_system": sum(stat["total_moon_count"] for stat in all_stats) / len(systems),
        "largest_planet_overall": max(stat["largest_planet_size"] for stat in all_stats),
    }
    
    return aggregate_stats

def print_analysis(stats):
    """Print the analysis results in a readable format."""
    print("\nAggregate System Analysis:")
    print(f"Total Systems Analyzed: {stats['total_systems']}")
    print("\nStar Type Distribution:")
    for star_type, count in stats['star_type_distribution'].items():
        percentage = (count / stats['total_systems']) * 100
        print(f"  {star_type}: {count} ({percentage:.2f}%)")
    print(f"\nAverage Planets per System: {stats['avg_planets_per_system']:.2f}")
    print(f"Average Habitable Planets per System: {stats['avg_habitable_planets_per_system']:.2f}")
    print(f"Average Moons per System: {stats['avg_moons_per_system']:.2f}")
    print(f"Largest Planet (in Earth radii): {stats['largest_planet_overall']:.2f}")

def search_planets(systems, criteria):
    """
    Search for planets meeting specific criteria across all systems.
    
    :param systems: List of PlanetarySystem objects
    :param criteria: Function that takes a planet and returns True if it meets the criteria
    :return: List of tuples (system_name, planet_name) for matching planets
    """
    matching_planets = []
    for system in systems:
        for planet in system.planets:
            if criteria(planet):
                matching_planets.append((system.name, planet.name))
    return matching_planets

# Example search criteria
def is_large_habitable(planet):
    return planet.habitable and planet.size > 1.5

def is_hot_jupiter(planet):
    return planet.size > 8 and planet.orbital_period < 0.1