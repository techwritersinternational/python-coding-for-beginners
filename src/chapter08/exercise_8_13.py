def assemble_droid(class_letters, serial_number, *components):
    if len(class_letters) != 2:
       return "Error: Droid class must be exactly 2 letters."
   
    if not str(serial_number).isdigit():
       return "Error: Serial number must be numeric."
   
    droid_name = f"{class_letters}-{serial_number}"

    if not components:
       return "Error: No components provided for droid assembly."
         
    # Determine droid category
    if any("manipulator arm" in str(c).lower() for c in components):
       droid_type = "Worker Droid"
    elif any("drill" in str(c).lower() for c in components):
       droid_type = "Mining Droid"
    elif any("speaker" in str(c).lower() for c in components):
       droid_type = "Communication Droid"
    else:
       droid_type = "General Purpose Droid"
      
    final_components = {droid_name: {"Droid Type": droid_type, "Components": components}}

    return final_components

# Test the function with different configurations
print(assemble_droid("MD", "7425",
   "Quantum Processing Unit",
   "Manipulator Arm Mark II",
   "Self-Repair Module"
))

print("\n" + "="*50 + "\n")

print(assemble_droid("CD", "2319",
   "Advanced Speaker Array",
   "Universal Translator",
   "Holographic Projector"
))

print("\n" + "="*50 + "\n")

print(assemble_droid("WD", "8547",
   "Heavy Duty Drill",
   "Mineral Analyzer",
   "Reinforced Chassis"
))

print("\n" + "="*50 + "\n")