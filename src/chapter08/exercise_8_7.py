def record_malfunction(system_name, severity, description, timestamp):
   severity = severity.lower()
   
   # Define suggested actions based on severity
   actions = {
       "low": "Monitor the situation",
       "warning": "Perform diagnostic checks",
       "critical": "Initiate emergency protocols"
   }
   
   if severity not in actions:
       return {
           "error": "Invalid severity level. Must be 'low', 'warning', or 'critical'."
       }
   
   malfunction_record = {
       "system": system_name,
       "severity": severity,
       "description": description,
       "timestamp": timestamp,
       "suggested_action": actions[severity]
   }
   
   return malfunction_record

# Test the function
malfunction1 = record_malfunction(
   "Life Support",
   "warning",
   "Oxygen recycling efficiency decreased by 15%",
   "2024-02-15 14:30:00"
)

malfunction2 = record_malfunction(
   "Main Reactor",
   "critical",
   "Coolant pressure dropping rapidly",
   "2024-02-15 14:35:00"
)

malfunction3 = record_malfunction(
   "Communication Array",
   "low",
   "Intermittent signal interference detected",
   "2024-02-15 14:40:00"
)

# Print the results
for malfunction in [malfunction1, malfunction2, malfunction3]:
   print("\nMalfunction Record:")
   for key, value in malfunction.items():
       print(f"{key.title()}: {value}")