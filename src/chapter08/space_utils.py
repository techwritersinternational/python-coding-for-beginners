def spacecraft_status(**systems):
    print("Spacecraft Systems Status:")
    for system, status in systems.items():
        print(f"  {system.replace('_', ' ').title()}: {status}")

def launch_shuttle(use_upper_deck):
    if use_upper_deck:
        print("Using the upper deck.")
    else:
        print("Using the lower deck.")

def send_message(message):
    print(f"Sending message: {message}")