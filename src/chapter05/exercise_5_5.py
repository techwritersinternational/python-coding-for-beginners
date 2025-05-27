current_region = "Nebula"  # Can be "Nebula", "Asteroid Belt", "Solar System", or "Deep Space"
fuel_level = 65  # Percentage of fuel remaining
shield_strength = 80  # Percentage of shield strength remaining

if current_region == "Nebula":
    print("You're navigating through a colorful nebula. Sensor reliability reduced.")
    if fuel_level < 50:
        print("Warning: Fuel levels low. Nebula interference may affect fuel efficiency.")
elif current_region == "Asteroid Belt":
    print("You're in a dense asteroid belt. Stay alert for potential collisions.")
    if shield_strength < 70:
        print("Caution: Shield strength suboptimal. Consider upgrading shields before proceeding.")
elif current_region == "Solar System":
    print("You're in a solar system. Watch for gravitational effects from nearby planets.")
    if fuel_level < 80:
        print("Advice: Consider refueling at a nearby space station.")
else:
    print("You're in deep space. Long-range scanners activated.")
    if fuel_level < 30:
        print("Alert: Fuel critically low. Engage emergency power saving measures.")
