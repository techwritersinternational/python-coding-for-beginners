def calculate_fuel_efficiency(distance, fuel_used, unit="km/l"):
    efficiency = distance / fuel_used
    if unit == "mpg":
        efficiency *= 2.35214  # Convert km/l to mpg
    return efficiency