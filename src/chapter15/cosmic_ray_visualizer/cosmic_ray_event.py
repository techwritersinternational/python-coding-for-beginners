import numpy as np
from datetime import datetime

class CosmicRayEvent:
    def __init__(self, timestamp, energy, direction, particle_type):
        self.timestamp = timestamp
        self.energy = energy
        self.direction = direction
        self.particle_type = particle_type


    def from_dict(self, event_dict):
        self.timestamp=event_dict['timestamp'],
        self.energy=event_dict['energy'],
        self.direction=event_dict['direction'],
        self.particle_type=event_dict['particle_type']


    def __str__(self):
        return f"CosmicRayEvent(timestamp={self.timestamp}, energy={self.energy:.2e} eV, " \
               f"direction={self.direction}, particle_type={self.particle_type})"

    def to_dict(self):
        """Convert the event to a dictionary."""
        return {
            'timestamp': self.timestamp,
            'energy': self.energy,
            'direction': self.direction,
            'particle_type': self.particle_type
        }

    def get_direction_cartesian(self):
        """Convert spherical coordinates to cartesian."""
        theta, phi = self.direction
        x = np.sin(theta) * np.cos(phi)
        y = np.sin(theta) * np.sin(phi)
        z = np.cos(theta)
        return (x, y, z)

    def get_energy_gev(self):
        """Convert energy from eV to GeV."""
        return self.energy / 1e9

    def time_since_start(self, start_time):
        """Calculate time elapsed since the start of the observation."""
        return (self.timestamp - start_time).total_seconds()