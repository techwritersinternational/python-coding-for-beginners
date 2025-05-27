import json
import csv
from datetime import datetime

class FlightTracker:
   def __init__(self, json_file="flight_data.json"):
       self.json_file = json_file
       self.flights = self.load_data()
       
   def load_data(self):
       """Load flight data from JSON file."""
       try:
           with open(self.json_file, 'r') as file:
               return json.load(file)
       except FileNotFoundError:
           return {"flights": {}, "last_id": 0}
       
   def save_data(self):
       """Save flight data to JSON file."""
       try:
           with open(self.json_file, 'w') as file:
               json.dump(self.flights, file, indent=4)
           print("Flight data saved successfully!")
       except Exception as e:
           print(f"Error saving data: {str(e)}")
   
   def generate_flight_id(self):
       """Generate unique flight ID."""
       self.flights["last_id"] += 1
       return f"ITA{self.flights['last_id']:04d}"
   
   def add_flight(self):
       """Add a new flight to the database."""
       print("\nAdding New Flight")
       print("-" * 50)
       
       try:
           # Get flight details
           origin = input("Origin: ").strip()
           if not origin:
               print("Error: Origin cannot be empty")
               return
               
           destination = input("Destination: ").strip()
           if not destination:
               print("Error: Destination cannot be empty")
               return
               
           departure = input("Departure time (YYYY-MM-DD HH:MM): ").strip()
           try:
               departure_time = datetime.strptime(departure, "%Y-%m-%d %H:%M")
           except ValueError:
               print("Error: Invalid departure time format")
               return
               
           arrival = input("Arrival time (YYYY-MM-DD HH:MM): ").strip()
           try:
               arrival_time = datetime.strptime(arrival, "%Y-%m-%d %H:%M")
           except ValueError:
               print("Error: Invalid arrival time format")
               return
               
           if arrival_time <= departure_time:
               print("Error: Arrival time must be after departure time")
               return
               
           passengers = int(input("Number of passengers: ").strip())
           if passengers < 0:
               print("Error: Invalid passenger count")
               return

           
           # Generate unique ID and create flight record
           flight_id = self.generate_flight_id()
           
           self.flights["flights"][flight_id] = {
               "origin": origin,
               "destination": destination,
               "departure": departure,
               "arrival": arrival,
               "passengers": passengers
           }
           
           # Save updated data
           self.save_data()
           print(f"\nFlight {flight_id} has been added to the database!")
           
       except Exception as e:
           print(f"Error adding flight: {str(e)}")
   
   def view_flights(self):
       """Display all flights in the database."""
       print("\nFlight Database")
       print("=" * 50)
       
       if not self.flights["flights"]:
           print("No flights in database.")
           return
       
       for flight_id, data in sorted(self.flights["flights"].items()):
           print(f"\nFlight ID: {flight_id}")
           print(f"Route: {data['origin']} → {data['destination']}")
           print(f"Departure: {data['departure']}")
           print(f"Arrival: {data['arrival']}")
           print(f"Passengers: {data['passengers']}")
   
   def export_csv(self, filename="flight_summary.csv"):
       """Export flight summary to CSV."""
       try:
           if not self.flights["flights"]:
               print("No flights to export.")
               return
               
           fieldnames = ['Flight ID', 'Origin', 'Destination', 'Passengers']
           
           with open(filename, 'w', newline='') as file:
               writer = csv.writer(file)
               writer.writerow(fieldnames)
            
               for flight_id, data in self.flights["flights"].items():
                   writer.writerow([
                       flight_id,
                       data['origin'],
                       data['destination'],
                       data['passengers']
                   ])
                   
           print(f"\nFlight summary exported to {filename}")
           
       except Exception as e:
           print(f"Error exporting data: {str(e)}")


tracker = FlightTracker()

while True:
    print("\nInterstellar Transport Authority - Flight Tracker")
    print("1. Add new flight")
    print("2. View flights")
    print("3. Export summary to CSV")
    print("4. Exit")
    
    choice = input("\nSelect option (1-4): ").strip()
    
    if choice == '1':
        tracker.add_flight()
    elif choice == '2':
        tracker.view_flights()
    elif choice == '3':
        tracker.export_csv()
    elif choice == '4':
        print("\nExiting system. Safe travels!")
        break
    else:
        print("Invalid option. Please try again.")
