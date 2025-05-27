from datetime import datetime, timedelta

# Get the current date and time
mission_start = datetime.now()
print(f"Mission started at: {mission_start}")

# Calculate a future date
mission_duration = timedelta(days=-365)
mission_end = mission_start + mission_duration
print(f"Estimated mission completion: {mission_end}")

# Format a date as a string
formatted_date = mission_end.strftime("%Y-%m-%d %H:%M:%S")
print(f"Mission end date (formatted): {formatted_date}")