class Exoplanet:
    def __init__(self, name, host_star, mass, radius, orbital_period, equilibrium_temp, distance, discovery_year):
        self.name = name if name else "Unknown"
        self.host_star = host_star if host_star else "Unknown"
        self.mass = float(mass) if mass is not None else None
        self.radius = float(radius) if radius is not None else None
        self.orbital_period = float(orbital_period) if orbital_period is not None else None
        self.equilibrium_temp = float(equilibrium_temp) if equilibrium_temp is not None else None
        self.distance = float(distance) if distance is not None else None
        self.discovery_year = int(discovery_year) if discovery_year is not None else None

    def __str__(self):
        return f"{self.name} - a planet orbiting {self.host_star}"
    
    def surface_gravity(self):
        if self.mass is None or self.radius is None:
            return None
        try:
            mass_kg = self.mass * 1.898e27
            radius_m = self.radius * 6.371e6
            G = 6.67430e-11
            return G * mass_kg / (radius_m ** 2)
        except ZeroDivisionError:
            return None

    def is_potentially_habitable(self):
        """
        Check if the planet is potentially habitable based on its equilibrium temperature.
        We'll use a simple range of 200K to 400K as potentially habitable.
        """
        if self.equilibrium_temp is None:
            return "Unknown"
        
        if 200 <= self.equilibrium_temp <= 400:
            return "Potentially Habitable"
        elif self.equilibrium_temp < 200:
            return "Too Cold"
        else:
            return "Too Hot"

    def earth_years_per_orbit(self):
        """Calculate the number of Earth years for one orbit of this exoplanet."""
        if self.orbital_period is None:
            return None
        return self.orbital_period / 365.25

    def to_dict(self):
        """Convert the Exoplanet object to a dictionary."""
        return {
            'name': self.name,
            'host_star': self.host_star,
            'mass': self.mass,
            'radius': self.radius,
            'orbital_period': self.orbital_period,
            'equilibrium_temp': self.equilibrium_temp,
            'distance': self.distance,
            'discovery_year': self.discovery_year,
            'surface_gravity': self.surface_gravity(),
            'habitability': self.is_potentially_habitable(),
            'earth_years_per_orbit': self.earth_years_per_orbit()
        }