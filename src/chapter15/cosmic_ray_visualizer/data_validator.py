import numpy as np
from datetime import datetime, timedelta

class DataValidationError(Exception):
    """Custom exception for data validation errors."""
    pass

def validate_cosmic_ray_event(event):
    """
    Validate a single cosmic ray event.

    :param event: Dictionary representing a cosmic ray event
    :raises DataValidationError: If the event fails validation
    """
    required_keys = ['timestamp', 'energy', 'direction', 'particle_type']
    for key in required_keys:
        if key not in event:
            raise DataValidationError(f"Missing required key: {key}")

    # Validate timestamp
    if not isinstance(event['timestamp'], datetime):
        raise DataValidationError("Timestamp must be a datetime object")

    # Validate energy
    if not isinstance(event['energy'], (int, float)) or event['energy'] <= 0:
        raise DataValidationError("Energy must be a positive number")

    # Validate direction
    if not isinstance(event['direction'], tuple) or len(event['direction']) != 2:
        raise DataValidationError("Direction must be a tuple of (theta, phi)")

    theta, phi = event['direction']
    if not (0 <= theta <= np.pi) or not (0 <= phi < 2*np.pi):
        raise DataValidationError("Invalid direction angles")

    # Validate particle type
    valid_particles = ['proton', 'helium', 'carbon', 'oxygen', 'iron']
    if event['particle_type'] not in valid_particles:
        raise DataValidationError(f"Invalid particle type. Must be one of: {', '.join(valid_particles)}")

def validate_cosmic_ray_data(event_data):
    """
    Validate the entire cosmic ray dataset.

    :param event_data: List of dictionaries containing event data
    :return: Tuple of (valid_events, error_log)
    """
    valid_events = []
    error_log = []

    for i, event in enumerate(event_data):
        try:
            validate_cosmic_ray_event(event)
            valid_events.append(event)
        except DataValidationError as e:
            error_log.append(f"Error in event {i}: {str(e)}")

    return valid_events, error_log

def check_data_integrity(event_data):
    """
    Check the integrity of the cosmic ray dataset.

    :param event_data: List of dictionaries containing event data
    :return: Dictionary of integrity check results
    """
    total_events = len(event_data)
    valid_events, error_log = validate_cosmic_ray_data(event_data)
    valid_count = len(valid_events)

    # Check for chronological order
    timestamps = [event['timestamp'] for event in valid_events]
    is_chronological = all(timestamps[i] <= timestamps[i+1] for i in range(len(timestamps)-1))

    # Check for duplicate events
    unique_events = set(tuple(sorted(event.items())) for event in valid_events)
    duplicate_count = valid_count - len(unique_events)

    return {
        'total_events': total_events,
        'valid_events': valid_count,
        'error_count': total_events - valid_count,
        'is_chronological': is_chronological,
        'duplicate_count': duplicate_count,
        'error_log': error_log
    }

def handle_missing_data(event_data, start_time, end_time, expected_interval=timedelta(minutes=5)):
    """
    Detect and handle missing data points.

    :param event_data: List of dictionaries containing event data
    :param start_time: Start time of the observation period
    :param end_time: End time of the observation period
    :param expected_interval: Expected time interval between events
    :return: Tuple of (processed_data, missing_intervals)
    """
    processed_data = sorted(event_data, key=lambda x: x['timestamp'])
    missing_intervals = []

    current_time = start_time
    for event in processed_data:
        if event['timestamp'] - current_time > expected_interval:
            missing_intervals.append((current_time, event['timestamp']))
        current_time = event['timestamp'] + expected_interval

    if end_time - current_time > expected_interval:
        missing_intervals.append((current_time, end_time))

    return processed_data, missing_intervals