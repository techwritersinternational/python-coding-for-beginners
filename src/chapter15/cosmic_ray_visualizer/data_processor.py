from collections import Counter
import numpy as np
from scipy.signal import lombscargle

from cosmic_ray_event import CosmicRayEvent
from data_validator import check_data_integrity, handle_missing_data, DataValidationError

def read_cosmic_ray_data(event_data):
    """
    Read and parse simulated cosmic ray data.
    """
    # Convert to CosmicRayEvent objects
    events = []
    for event in event_data:
        events.append(
            CosmicRayEvent(
                event['timestamp'], 
                event['energy'], 
                event['direction'], 
                event['particle_type']
            )
        )
    
    return events



def remove_outliers(events, energy_threshold=1e15):
    """
    Remove events with unrealistically high energies.    
    """
    return [event for event in events if event.energy <= energy_threshold]

def normalize_energies(events):
    """
    Normalize event energies to a 0-1 scale.
    """
    energies = [event.energy for event in events]
    min_energy = min(energies)
    max_energy = max(energies)
    
    for event in events:
        event.normalized_energy = (event.energy - min_energy) / (max_energy - min_energy)
    
    return events

def calculate_flux(events, duration_seconds, detector_area=1.0):
    """
    Calculate cosmic ray flux (particles per m^2 per second).
    """
    return len(events) / (duration_seconds * detector_area)

def particle_type_distribution(events):
    """
    Calculate the distribution of particle types.
    """
    return Counter(event.particle_type for event in events)

def process_cosmic_ray_data(event_data, start_time, end_time):
    """
    Process cosmic ray data: validate, clean, normalize, and perform analyses.

    :param event_data: List of dictionaries containing event data
    :param start_time: Start time of the observation
    :param end_time: End time of the observation
    :param space_weather_data: Dictionary of simulated space weather data
    :return: Dictionary containing processed data, analysis results, and data quality information
    """
    # Check data integrity
    integrity_results = check_data_integrity(event_data)

    if integrity_results['valid_events'] == 0:
        raise DataValidationError("No valid events found in the dataset")

    # Handle missing data
    processed_data, missing_intervals = handle_missing_data(event_data, start_time, end_time)

    # Read and parse data
    events = read_cosmic_ray_data(processed_data)
    
    # Clean data
    events = remove_outliers(events)
    
    # Normalize energies
    events = normalize_energies(events)
    
    # Calculate derived quantities
    duration_seconds = (end_time - start_time).total_seconds()
    flux = calculate_flux(events, duration_seconds)
    particle_distribution = particle_type_distribution(events)
    stats = implement_basic_statistical_analysis(events)
    frequencies, power = detect_periodic_patterns(events, start_time)

    return {
        'events': events,
        'flux': flux,
        'particle_distribution': particle_distribution,
        'statistics': stats,
        'periodogram': (frequencies, power),
        'data_quality': {
            'integrity_results': integrity_results,
            'missing_intervals': missing_intervals
        }
    }

def implement_basic_statistical_analysis(events):
    """
    Perform basic statistical analysis on cosmic ray events.

    :param events: List of CosmicRayEvent objects
    :return: Dictionary containing statistical measures
    """
    energies = np.array([event.energy for event in events])

    return {
        'mean_energy': np.mean(energies),
        'median_energy': np.median(energies),
        'std_energy': np.std(energies),
        'min_energy': np.min(energies),
        'max_energy': np.max(energies)
    }

def detect_periodic_patterns(events, start_time):
    """
    Detect periodic patterns in cosmic ray events using Lomb-Scargle periodogram.

    :param events: List of CosmicRayEvent objects
    :param start_time: Start time of the observation
    :return: Tuple of (frequencies, power spectrum)
    """
    times = np.array([(event.timestamp - start_time).total_seconds() for event in events])
    energies = np.array([event.energy for event in events])

    frequencies = np.linspace(0.1, 10, 1000)  # Adjust frequency range as needed
    power = lombscargle(times, energies, frequencies)

    return frequencies, power
