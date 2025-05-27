def generate_status_report(system_name):
   systems = {
       "engine core": {
           "status": "warning",
           "temp": 1200,
           "pressure": 1.1
       },
       "life support": {
           "status": "nominal",
           "oxygen": 98,
           "co2": 0.04
       },
       "shield generator": {
           "status": "critical",
           "power": 15,
           "coverage": 60
       }
   }
   
   if system_name.lower() not in systems:
       return f"ERROR: No system found with name '{system_name}'"
   
   system = systems[system_name.lower()]
   report = f"STATUS REPORT: {system_name.title()} - "
   
   if system["status"] == "critical":
       report += "!!! CRITICAL ALERT !!! "
       
   for key, value in system.items():
       if key == "status":
           report += f"Status: {value}, "
       elif key == "temp":
           report += f"Temp: {value}°C, "
       elif key == "pressure":
           report += f"Pressure: {value} atm, "
       elif key == "oxygen":
           report += f"O2: {value}%, "
       elif key == "co2":
           report += f"CO2: {value}%, "
       elif key == "power":
           report += f"Power: {value}%, "
       elif key == "coverage":
           report += f"Coverage: {value}%, "
           
   return report.rstrip(", ")

# Test the function
print(generate_status_report("engine core"))
print(generate_status_report("life support"))
print(generate_status_report("shield generator"))
print(generate_status_report("warp drive"))