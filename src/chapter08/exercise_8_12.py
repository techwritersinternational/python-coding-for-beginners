def name_droid(class_letters, serial_number, **parts):
   if len(class_letters) != 2:
       return "Error: Droid class must be exactly 2 letters."
   
   if not str(serial_number).isdigit():
       return "Error: Serial number must be numeric."
   
   droid_name = f"{class_letters}-{serial_number}"
   
   report = f"=== DROID {droid_name} SPECIFICATION REPORT ===\n"
   
   if parts:
       report += "\nInstalled Components:\n"
       for part, part_number in parts.items():
           report += f"{part.title().replace("_", " ")} (part no. {part_number})\n"
   else:
       report += "\nNo components specified.\n"
   
   return report

# Test the function with different configurations
print(name_droid("MD", "7425",
   drill=1564,
   mineral_analyzer=564,
   chassis=867865
))

print(name_droid("CD", "2319",
   synthesizer=5453,
   translation_matrix=23,
   holographic_display=3434
))

print(name_droid("WD", "8547",
   manipulator_arm=9787,
   welding_tool=4322,
   balance_stabilizer=2156
))

# Test error cases
print(name_droid("M", "123"))  # Too few letters
print(name_droid("MDR", "123"))  # Too many letters
print(name_droid("MD", "ABC"))  # Non-numeric serial