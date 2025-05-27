def create_log_entry(stardate, location, mission_status):
   log_entry = f"Captain's Log, Stardate {stardate}.\n"
   log_entry += f"Location: {location}.\n"
   log_entry += f"Mission Status: {mission_status}.\n"
   
   return log_entry

print("Welcome to the Captain's Log Entry System")
print("Enter 'q' at any prompt to finish logging entries")
   
all_entries = []
   
while True:
    print("\nNew Log Entry:")
    stardate = input("Stardate: ")
    if stardate.lower() == 'q':
        break
        
    location = input("Current Location: ")
    if location.lower() == 'q':
        break
        
    mission_status = input("Mission Status: ")
    if mission_status.lower() == 'q':
        break
    
    log_entry = create_log_entry(stardate, location, mission_status)
    all_entries.append(log_entry)
    
    print("\nLog Entry Created:")
    print(log_entry)
    
    continue_logging = input("\nCreate another log entry? (y/n): ")
    if continue_logging.lower() != 'y':
        break

if all_entries:
    print("\nAll Log Entries:")
    for entry in all_entries:
        print(entry)

print("\nLog entry system terminated.")

