def assemble_droid(*components):
   if not components:
       return "Error: No components provided for droid assembly."

   # Initialize the assembly report
   report = "=== DROID ASSEMBLY REPORT ===\n"
   report += f"Total components: {len(components)}\n\n"
   
   # List all components
   report += "Installed components:\n"
   for i, component in enumerate(components, 1):
       report += f"{i}. {component}\n"
      
   # Determine droid category
   if any("manipulator arm" in str(c).lower() for c in components):
       droid_type = "Worker Droid"
   elif any("drill" in str(c).lower() for c in components):
       droid_type = "Mining Droid"
   elif any("speaker" in str(c).lower() for c in components):
       droid_type = "Communication Droid"
   else:
       droid_type = "General Purpose Droid"
   
   report += f"\nDroid Category: {droid_type}"
   
   return report

# Test the function with different configurations
print(assemble_droid(
   "Quantum Processing Unit",
   "Manipulator Arm Mark II",
   "Self-Repair Module"
))

print("\n" + "="*50 + "\n")

print(assemble_droid(
   "Advanced Speaker Array",
   "Universal Translator",
   "Holographic Projector"
))

print("\n" + "="*50 + "\n")

print(assemble_droid(
   "Heavy Duty Drill",
   "Mineral Analyzer",
   "Reinforced Chassis"
))

print("\n" + "="*50 + "\n")

print(assemble_droid())  # Test with no components