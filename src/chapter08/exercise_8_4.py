def configure_spacecraft(name, spacecraft_type, propulsion, solar_panels=True):
    config = {
        "name": name,
        "type": spacecraft_type,
        "propulsion": propulsion,
        "solar_panels": solar_panels
    }
    
    solar_status = "Yes" if solar_panels else "No"
    print(f"Spacecraft configured: {name} ({spacecraft_type}) with {propulsion}. Solar panels: {solar_status}")
    
# Test the function with different combinations of arguments

# All positional arguments, using default for solar_panels
configure_spacecraft("Explorer I", "Orbiter", "Ion engine")

# Mix of positional and keyword arguments, overriding solar_panels default
configure_spacecraft("Voyager III", "Deep space probe", "Nuclear thermal", solar_panels=False)

# All keyword arguments with additional customizations
configure_spacecraft(
    name="Mars Lander",
    spacecraft_type="Lander",
    propulsion="Chemical rockets"
)

# Using all default values for optional parameters and additional customization
configure_spacecraft("ISS Module", "Space station", "No engines")
