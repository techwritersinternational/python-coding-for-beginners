from stellar_entities import Star, Planet, Moon
from space_exploration import Spacecraft

def run_space_program():
    # Create stellar objects
    print("Initializing stellar objects...")
    prajna = Star("Prajna", "Yellow Dwarf", 6000)
    chaitanya = Planet("Chaitanya", "Terrestrial")
    dharani = Planet("Dharani", "Gas Giant")
    tejas = Moon("Tejas", "Rocky")
    
    # Create spacecraft
    nova = Spacecraft("Nova Explorer", "Warp 5")
    
        
    # Begin exploration
    print(f"\nBeginning exploration mission...")
    nova.report_location()
    
    # Travel to first planet
    nova.travel_to(chaitanya)
    nova.report_location()
    
    # Travel to second planet
    nova.travel_to(dharani)
    nova.report_location()


run_space_program()