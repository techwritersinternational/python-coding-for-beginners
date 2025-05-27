"""Space-related calculation and classification functions.

This module provides various functions for space-related calculations
and classifications, including escape velocity, weight conversion,
fuel efficiency assessment, and alien species classification.
"""

import math

def calculate_escape_velocity(mass, radius):
   """Calculate the escape velocity for a celestial body.
   
   Parameters:
       mass (float): Mass of the celestial body in kilograms
       radius (float): Radius of the celestial body in meters
   
   Returns:
       float: Escape velocity in meters per second
   """
   gravitational_constant = 6.67430e-11
   return math.sqrt(2 * gravitational_constant * mass / radius)

def convert_planet_weight(weight, home_gravity=9.8, target_gravity=3.7):
   """Convert weight between planets with different gravitational fields.
   
   Parameters:
       weight (float): Weight on home planet in newtons
       home_gravity (float, optional): Gravity of home planet in m/s². Defaults to 9.8 (Earth).
       target_gravity (float, optional): Gravity of target planet in m/s². Defaults to 3.7 (Mars).
   
   Returns:
       float: Weight on target planet in newtons
   """
   return weight / home_gravity * target_gravity

def evaluate_spaceship_efficiency(distance, fuel_consumed):
   """Evaluate the fuel efficiency of a spaceship.
   
   Parameters:
       distance (float): Distance traveled in kilometers
       fuel_consumed (float): Amount of fuel consumed in liters
   
   Returns:
       str: Efficiency rating ('Poor', 'Average', 'Good', or 'Excellent')
   """
   efficiency = distance / fuel_consumed
   
   if efficiency < 10:
       return "Poor"
   elif efficiency < 20:
       return "Average"
   elif efficiency < 30:
       return "Good"
   else:
       return "Excellent"

def classify_alien_species(tentacles, eyes, limbs):
   """Classify alien species based on their physical characteristics.
   
   Parameters:
       tentacles (int): Number of tentacles
       eyes (int): Number of eyes
       limbs (int): Number of limbs
   
   Returns:
       str: Species classification ('Cephalopoid', 'Arachnoid', 'Gastropoid', or 'Humanoid')
   """
   if tentacles > 0:
       return "Cephalopoid"
   elif eyes > 2:
       return "Arachnoid"
   elif limbs == 0:
       return "Gastropoid"
   else:
       return "Humanoid"