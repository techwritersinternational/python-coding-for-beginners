fuel_level = 100
weather = "Clear"
crew_ready = True

if fuel_level <= 90:
    print("Insufficient fuel. Launch aborted.")
elif weather != "Clear":
    print("Weather not suitable. Launch aborted.")
elif not crew_ready:
    print("Crew not ready. Launch aborted.")
else:
    print("Launch is go!")

spacecraft_velocity = 13
escape_velocity = 11.186
fuel_remaining = 50
engine_overheating = False
crew_secured = True

is_velocity_sufficient = spacecraft_velocity > escape_velocity
has_adequate_fuel = fuel_remaining > 20
engine_safe = not engine_overheating

if is_velocity_sufficient and has_adequate_fuel and engine_safe and crew_secured:
   print("Initiate lunar injection")

astronauts = ["Bob", "Alice", "Charlie"]
if astronauts and astronauts[0] == "Bob":
    print("Bob is the mission commander.")
    print(astronauts[3])