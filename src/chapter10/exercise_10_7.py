from datetime import datetime
import os

def create_placeholder_manifest(flight_number):
   """Create placeholder manifest when original is missing."""
   return {
       'flight_number': flight_number,
       'status': 'MANIFEST MISSING',
       'passengers': [],
       'warning': 'Original manifest unavailable - please verify with flight control',
       'timestamp': datetime.now()
   }

def read_manifest(flight_number):
   """Read and process a flight manifest."""
   filename = f"flight_{flight_number}_manifest.txt"
   manifest = {
       'flight_number': flight_number,
       'status': 'ACTIVE',
       'passengers': [],
       'timestamp': datetime.now()
   }
   
   try:
       with open(filename, 'r') as file:
           manifest['passengers'] = [line.strip() for line in file if line.strip()]
       log_event(f"Successfully read manifest for flight {flight_number}")
       
   except FileNotFoundError:
       manifest = create_placeholder_manifest(flight_number)
       log_event(f"Manifest not found for flight {flight_number}", level="WARNING")
       
   except Exception as e:
       log_event(f"Error processing manifest for flight {flight_number}: {str(e)}", 
                level="ERROR")
  
   return manifest

def display_manifest(manifest):
   """Display manifest information."""
   print(f"\nFlight {manifest['flight_number']} Manifest")
   print("-" * 50)
   print(f"Status: {manifest['status']}")
   print(f"Time: {manifest['timestamp'].strftime('%Y-%m-%d %H:%M:%S')}")
   
   if 'warning' in manifest:
       print(f"\nWARNING: {manifest['warning']}")
   
   if manifest['passengers']:
       print("\nPassengers:")
       for passenger in manifest['passengers']:
           print(f"{passenger}")
       print(f"\nTotal passengers: {len(manifest['passengers'])}")
   else:
       print("\nNo passenger information available")

def log_event(message, level="INFO"):
   """Log events to file."""
   timestamp = datetime.now()
   with open('manifest_log.txt', 'a') as log:
       log.write(f"{timestamp} - {level}: {message}\n")


# Example usage with test files
# Create a test manifest file
with open("flight_123_manifest.txt", "w") as f:
    f.write("John Smith - Mars Colony\n")
    f.write("Sarah Chen - Europa Station\n")
    f.write("Alex Patel - Lunar Base\n")

"""Main program loop."""
print("Space Station Manifest System")
print("Enter 'q' to quit\n")

while True:
    flight = input("Enter flight number to view manifest: ").strip().lower()
    
    if flight == 'q':
        print("\nExiting system. Goodbye!")
        break
        
    if not flight.isdigit():
        print("Please enter a valid flight number")
        continue
        
    try:
        manifest = read_manifest(flight)
        display_manifest(manifest)
    except Exception as e:
        print("\nAn unexpected error occurred")
        log_event(f"Unexpected error: {str(e)}", level="ERROR")

