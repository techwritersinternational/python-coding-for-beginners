def display_station_name(name):
    print(f"Space Station: {name}")

def display_staffing_level(current_staff, max_staff):
    print(f"Current Staffing: {current_staff}/{max_staff}")

def display_shuttle_status(status):
    print(f"Shuttle Status: {status}")

def display_oxygen_level(level):
    print(f"Oxygen Level: {level}%")

def display_station_info(name, current_staff, max_staff, shuttle_status, oxygen_level):
    print("=== Space Station Information Board ===")
    display_station_name(name)
    display_staffing_level(current_staff, max_staff)
    display_shuttle_status(shuttle_status)
    display_oxygen_level(oxygen_level)
    print("======================================")

# Test the functions
station_name = "Artemis Alpha"
current_staff = 5
max_staff = 7
shuttle_status = "Docked"
oxygen_level = 98

display_station_info(station_name, current_staff, max_staff, shuttle_status, oxygen_level)