import json
from datetime import datetime

class ExplorationTracker:
   def __init__(self, filename="exploration_data.json"):
       self.filename = filename
       self.data = self.load_data()

   def load_data(self):
       """Load exploration data from JSON file."""
       try:
           with open(self.filename, 'r') as file:
               return json.load(file)
       except FileNotFoundError:
           # Return empty structure if file doesn't exist
           return {
               "explorers": {},
               "last_updated": None
           }

   def save_data(self):
       """Save current exploration data to JSON file."""
       self.data["last_updated"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
       try:
           with open(self.filename, 'w') as file:
               json.dump(self.data, file, indent=4)
           print("Data saved successfully!")
       except Exception as e:
           print(f"Error saving data: {str(e)}")

   def record_visit(self):
       """Record a new planet visit."""
       print("\nRecording New Planet Visit")
       print("-" * 50)

       # Get explorer information
       explorer = input("Explorer name: ").strip()
       if not explorer:
           print("Error: Explorer name cannot be empty")
           return

       # Get planet information
       planet = input("Planet name: ").strip()
       if not planet:
           print("Error: Planet name cannot be empty")
           return

       # Get visit details
       date = datetime.now().strftime("%Y-%m-%d")
       notes = input("Visit notes (optional): ").strip()

       # Create visit record
       visit = {
           "date": date,
           "planet": planet,
           "notes": notes
       }

       # Add to data structure
       if explorer not in self.data["explorers"]:
           self.data["explorers"][explorer] = []
       self.data["explorers"][explorer].append(visit)

       # Save updated data
       self.save_data()
       print(f"\nVisit to {planet} recorded for {explorer}!")

   def display_catalog(self):
       """Display the exploration catalog."""
       print("\nGalactic Exploration Catalog")
       print("=" * 50)

       if not self.data["explorers"]:
           print("No exploration data recorded yet.")
           return

       if self.data["last_updated"]:
           print(f"Last Updated: {self.data['last_updated']}\n")

       for explorer, visits in self.data["explorers"].items():
           print(f"\nExplorer: {explorer}")
           print("-" * len(f"Explorer: {explorer}"))
           
           for visit in visits:
               print(f"\nPlanet: {visit['planet']}")
               print(f"Date: {visit['date']}")
               if visit['notes']:
                   print(f"Notes: {visit['notes']}")


tracker = ExplorationTracker()

while True:
    print("\nGalactic Explorers Guild - Exploration Tracker")
    print("1. Record new planet visit")
    print("2. View exploration catalog")
    print("3. Exit")

    choice = input("\nSelect option (1-3): ").strip()

    if choice == '1':
        tracker.record_visit()
    elif choice == '2':
        tracker.display_catalog()
    elif choice == '3':
        print("\nExiting program. Safe travels!")
        break
    else:
        print("Invalid option. Please try again.")

