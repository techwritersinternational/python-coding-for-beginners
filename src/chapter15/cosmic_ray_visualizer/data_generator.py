import numpy as np
from datetime import timedelta, datetime

def generate_cosmic_ray_data(num_events, start_time, duration_days):
    """
    Generate simulated cosmic ray detection events.    
    """
    events = []
    end_time = start_time + timedelta(days=duration_days)
    
    for _ in range(num_events):
        event = {
            'timestamp': generate_timestamp(start_time, end_time),
            'energy': generate_energy(),
            'direction': generate_direction(),
            'particle_type': generate_particle_type()
        }
        events.append(event)
    
    return events

def generate_timestamp(start_time, end_time):
    """Generate a random timestamp within the given range."""
    seconds_in_time_period = int((end_time - start_time).total_seconds())
    return start_time + timedelta(
        seconds=np.random.randint(0, seconds_in_time_period)
    )

def generate_energy():
    """Generate a random energy value following a power-law distribution."""
    return np.random.pareto(a=2.5) * 1e9  # Energy in eV

def generate_direction():
    """Generate a random direction in 3D space."""
    phi = np.random.uniform(0, 2*np.pi)
    cos_theta = np.random.uniform(-1, 1)
    theta = np.arccos(cos_theta)
    return (theta, phi)

def generate_particle_type():
    """Generate a random particle type based on cosmic ray composition."""
    particle_types = ['proton', 'helium', 'carbon', 'oxygen', 'iron']
    probabilities = [0.90, 0.09, 0.004, 0.004, 0.002]  # Simplified composition
    return np.random.choice(particle_types, p=probabilities)

if __name__ == "__main__":
    # Example usage
    start_time = datetime(2025, 1, 1)
    events = generate_cosmic_ray_data(1000, start_time, 30)
    
    # Print the first few events
    for event in events[:5]:
        print(event)