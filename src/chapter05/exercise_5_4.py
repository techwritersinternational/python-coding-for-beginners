home_planet = "Earth"  # You can change this to test different scenarios

if home_planet == "Mars":
    print("Welcome, Martian delegates! Please proceed to the Red Room.")
else:
    if home_planet == "Earth":
        print("Welcome, Earth delegates! Please proceed to the Blue Room.")
    else:
        if home_planet == "Venus":
            print("Welcome, Venusian delegates! Please proceed to the Green Room.")
        else:
            print("Welcome, delegates! Please check in at the front desk for directions.")
