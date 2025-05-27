import random
import math

import os

from seed_generator import generate_initial_seed, generate_next_seed
from planetary_system import generate_planetary_system

from system_analyzer import analyze_multiple_systems, print_analysis, search_planets, is_large_habitable, is_hot_jupiter


def generate_multiple_systems(num_systems):
    """Generate a specified number of planetary systems."""
    systems = []
    seed = generate_initial_seed()
    for i in range(num_systems):
        try:
            system = generate_planetary_system(seed)
            systems.append(system)
        except ValueError as e:
            print(f"Warning: Failed to generate system {i+1}. Reason: {str(e)}")
        seed = generate_next_seed(seed)
    return systems

def save_system_to_file(system, filename):
    """Save the text representation of a planetary system to a file."""
    with open(filename, 'w') as f:
        f.write(str(system))


def save_systems(systems, directory):
    """Save all generated systems to individual files in the specified directory."""
    if not os.path.exists(directory):
        os.makedirs(directory)
    for i, system in enumerate(systems, 1):
        filename = os.path.join(directory, f"system_{i:03d}.txt")
        save_system_to_file(system, filename)

def main():
    print("Welcome to the Procedural Planetary System Generator!")
    
    while True:
        try:
            num_systems = int(input("How many planetary systems would you like to generate? "))
            if num_systems <= 0:
                raise ValueError("Number of systems must be positive.")
            break
        except ValueError as e:
            print(f"Invalid input: {e}. Please enter a positive integer.")
    
    print(f"\nGenerating {num_systems} planetary systems...")
    systems = generate_multiple_systems(num_systems)
    
    print("\nGeneration complete!")
    
    if not systems:
        print("Warning: No valid systems were generated.")
        return
    
    print("\nAnalyzing generated systems...")
    analysis_results = analyze_multiple_systems(systems)
    print_analysis(analysis_results)

    print("\nSearching for large habitable planets...")
    large_habitable_planets = search_planets(systems, is_large_habitable)
    print(f"Found {len(large_habitable_planets)} large habitable planets:")
    for system_name, planet_name in large_habitable_planets:
        print(f"  {planet_name} in {system_name}")

    print("\nSearching for hot Jupiters...")
    hot_jupiters = search_planets(systems, is_hot_jupiter)
    print(f"Found {len(hot_jupiters)} hot Jupiters:")
    for system_name, planet_name in hot_jupiters:
        print(f"  {planet_name} in {system_name}")

    # Display a summary of generated systems
    for i, system in enumerate(systems, 1):
        print(f"\nSystem {i}: {system.name}")
        print(f"  Star: {system.star.name} (Type {system.star.type.name})")
        print(f"  Planets: {len(system.planets)}")
        habitable_planets = sum(1 for planet in system.planets if planet.habitable)
        print(f"  Habitable Planets: {habitable_planets}")
    
    # Save systems to files
    save_directory = "generated_systems"
    save_systems(systems, save_directory)
    print(f"\nDetailed system information has been saved to the '{save_directory}' directory.")
    
    print("\nThank you for using the Procedural Planetary System Generator!")

if __name__ == "__main__":
    main()