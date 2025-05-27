from datetime import datetime, timedelta

class MarsDate:
   # Mars day (sol) is approximately 24 hours and 37 minutes
   SECONDS_PER_SOL = 24 * 60 * 60 + 37 * 60
   # Mars year is approximately 687 Earth days
   EARTH_DAYS_PER_MARS_YEAR = 687
   # Reference date: Mars Science Laboratory landing (Curiosity)
   REFERENCE_DATE = datetime(2012, 8, 6)
   

   def __init__(self, earth_date=None):
       if earth_date is None:
           earth_date = datetime.now()
       self.earth_date = earth_date
       self.sol = self.calculate_sol()
       self.mars_year = self.calculate_mars_year()
       
   def calculate_sol(self):
       """Calculate Mars sol since the start of this Mars year."""
       time_diff = self.earth_date - self.REFERENCE_DATE
       total_seconds = time_diff.total_seconds()
       sols = (total_seconds / self.SECONDS_PER_SOL) % self.EARTH_DAYS_PER_MARS_YEAR
       return int(sols)
   
   def calculate_mars_year(self):
       """Calculate Mars year number."""
       days_since_reference = (self.earth_date - self.REFERENCE_DATE).days
       return 1 + int(days_since_reference / self.EARTH_DAYS_PER_MARS_YEAR)
   
   def sols_between(date1, date2):
       """Calculate number of sols between two Earth dates."""
       if not isinstance(date1, datetime) or not isinstance(date2, datetime):
           raise ValueError("Both dates must be datetime objects")
       
       mars_date1 = MarsDate(date1)
       mars_date2 = MarsDate(date2)
       return abs(mars_date2.sol - mars_date1.sol)
   
   def add_sols(self, num_sols):
       """Add a number of sols to the current date."""
       additional_seconds = num_sols * self.SECONDS_PER_SOL
       new_earth_date = self.earth_date + timedelta(seconds=additional_seconds)
       return MarsDate(new_earth_date)
      
   def detailed_str(self):
       """Return detailed string with both Earth and Mars dates."""
       return f"Earth Date: {self.earth_date.strftime('%Y-%m-%d %H:%M:%S')}\n" \
              f"Mars Date: Year {self.mars_year}, Sol {self.sol}"

# Test the class
print("Testing MarsDate class...")

# Test current date
print("\nCurrent date on Mars:")
current_mars = MarsDate()
print(current_mars.detailed_str())

# Test specific date
print("\nSpecific date (Perseverance landing):")
perseverance_landing = MarsDate(datetime(2021, 2, 18))
print(perseverance_landing.detailed_str())

# Test sols between dates
curiosity_landing = datetime(2012, 8, 6)
perseverance_landing = datetime(2021, 2, 18)
sols = MarsDate.sols_between(curiosity_landing, perseverance_landing)
print(f"\nSols between Curiosity and Perseverance landings: {sols}")

# Test adding sols
print("\nAdding 100 sols to current date:")
future_date = current_mars.add_sols(100)
print(future_date.detailed_str())