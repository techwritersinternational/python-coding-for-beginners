def analyze_fleet(fleet):
    fleet_copy = fleet.copy()
    fleet_copy.sort()
    return f"Analyzed fleet (alphabetical order): {', '.join(fleet_copy)}"

spacecraft = ["Nova Horizon", "Stellar Wanderer", "Cosmic Voyager"]
result = analyze_fleet(spacecraft)
print(result)
print(spacecraft)