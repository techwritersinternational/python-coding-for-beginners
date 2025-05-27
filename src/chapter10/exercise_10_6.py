import os

def process_ansible_files(expected_files):
   """Process ansible communication files."""
   
   print("Processing ansible communications...")
   print("-" * 50)
   
   # Track success and failures
   processed = []
   failed = []
   
   # Process each expected file
   for filename in expected_files:
       try:
           # Ensure filename has .txt extension
           if not filename.endswith('.txt'):
               filename = filename + '.txt'
           
           # Try to read and print file contents
           print(f"\nReading ansible unit: {filename}")
           print("-" * 25)
           
           with open(filename, 'r') as file:
               contents = file.read()
               print(contents)
               processed.append(filename)
               
       except FileNotFoundError:
           error_msg = f"Could not find file: {filename}"
           print(error_msg)
           failed.append((filename, error_msg))
           
       except PermissionError:
           error_msg = f"Permission denied: {filename}"
           print(error_msg)
           failed.append((filename, error_msg))
           
       except Exception as e:
           error_msg = f"Error processing {filename}: {str(e)}"
           print(error_msg)
           failed.append((filename, error_msg))
   
   # Print summary
   print("\nProcessing complete")
   print("-" * 50)
   print(f"Successfully processed: {len(processed)}")
   print(f"Failed to process: {len(failed)}")
   
   if failed:
       print("\nErrors encountered:")
       for filename, error in failed:
           print(f"- {error}")


# Create some test files
with open("ansible1.txt", "w") as f:
    f.write("Status: Online\nLocation: Deep Space\n")

with open("ansible2.txt", "w") as f:
    f.write("Status: Active\nLocation: Mars Orbit\n")

# List of expected files (including some that don't exist)
expected_files = [
    "ansible1.txt",
    "ansible2.txt",
    "ansible3",  # Missing .txt extension
    "ansible4.txt"  # Doesn't exist
]

# Process the files
process_ansible_files(expected_files)

# Clean up test files
os.remove("ansible1.txt")
os.remove("ansible2.txt")