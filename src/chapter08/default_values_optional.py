def launch_rocket(destination, fuel_type="hydrogen", launch_delay=None):
    if launch_delay:
        print(f"Launching rocket in {launch_delay} minutes to {destination} using {fuel_type} fuel.")
    else:
        print(f"Launching rocket to {destination} using {fuel_type} fuel.")

launch_rocket("Venus")  # Uses default fuel_type
launch_rocket("Jupiter", "plasma")  # Overrides default fuel_type
launch_rocket("Jupiter", "plasma", 60)  # Overrides default fuel_type and adds a launch delay