def launch_rocket(destination, fuel_type="hydrogen"):
    print(f"Launching rocket to {destination} using {fuel_type} fuel.")

launch_rocket("Venus")  # Uses default fuel_type
launch_rocket("Jupiter", "plasma")  # Overrides default fuel_type