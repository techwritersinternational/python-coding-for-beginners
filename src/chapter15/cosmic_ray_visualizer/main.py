from datetime import datetime, timedelta
from data_generator import generate_cosmic_ray_data
from data_processor import process_cosmic_ray_data

from visualizer import create_visualizations

from data_validator import check_data_integrity

from visualizer import display_data_quality_info

from data_validator import DataValidationError

# Generate data
start_time = datetime(2025, 1, 1)
end_time = start_time + timedelta(days=30)
event_data = generate_cosmic_ray_data(10000, start_time, 30)

# Process data
processed_data = process_cosmic_ray_data(event_data, start_time, end_time)

# Print some results
print(f"Number of events after processing: {len(processed_data['events'])}")
print(f"Cosmic ray flux: {processed_data['flux']:.2e} particles/m^2/s")
print("Particle type distribution:")
for particle, count in processed_data['particle_distribution'].items():
    print(f"  {particle}: {count}")
print("Basic statistical analysis:")
for stat, value in processed_data['statistics'].items():
    print(f"  {stat}: {value}")

try:
    processed_data = process_cosmic_ray_data(event_data, start_time, end_time)
    display_data_quality_info(processed_data['data_quality'])
    # ... (continue with visualization and analysis)
except DataValidationError as e:
    print(f"Data validation error: {str(e)}")
    # Handle the error (e.g., ask user to provide new data or exit the program)