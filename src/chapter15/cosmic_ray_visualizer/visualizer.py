import matplotlib.pyplot as plt

from matplotlib.widgets import Slider, Button, RadioButtons
from datetime import timedelta, datetime

from data_processor import particle_type_distribution

from data_processor import particle_type_distribution, detect_periodic_patterns

plt.style.use('seaborn-v0_8')  # Use a more aesthetically pleasing style

def create_visualizations(processed_data):
    """
    Create and display basic visualizations for cosmic ray data.
    """
    events = processed_data['events']
    
    start_time = datetime(2025, 1, 1)
    frequencies, power = detect_periodic_patterns(events, start_time)

    # Create a figure with one subplots
    fig, (ax1) = plt.subplots(1, figsize=(12, 12))
    
    # Call individual plotting function
    plot_periodogram(ax1, frequencies, power)

    plt.tight_layout()
    plt.show()

def plot_energy_histogram(ax, events):
    """
    Create a histogram of cosmic ray energies.
    """
    energies = [event.energy for event in events]
    
    ax.hist(energies, bins=50, edgecolor='black')
    ax.set_title('Cosmic Ray Energy Distribution')
    ax.set_xlabel('Energy (eV)')
    ax.set_ylabel('Count')

def plot_time_scatter(ax, events):
    """
    Create a scatter plot of cosmic ray detection events over time.
    """
    timestamps = [event.timestamp for event in events]
    energies = [event.energy for event in events]
    
    ax.scatter(timestamps, energies, alpha=0.5)
    ax.set_title('Cosmic Ray Detections Over Time')
    ax.set_xlabel('Time')
    ax.set_ylabel('Energy (eV)')
    ax.set_yscale('log')  # Use log scale for y-axis due to wide range of energies
    
    # Rotate and align the tick labels so they look better
    fig = ax.get_figure()
    fig.autofmt_xdate()

def plot_particle_distribution(ax, particle_distribution):
    """
    Create a pie chart of particle type distribution.
    """
    labels = list(particle_distribution.keys())
    sizes = list(particle_distribution.values())
    
    ax.pie(sizes, labels=labels, autopct='%1.1f%%')
    ax.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle
    ax.set_title('Cosmic Ray Particle Type Distribution')

def interactive_dashboard(processed_data):
    """
    Create an interactive dashboard for exploring cosmic ray data.
    
    :param processed_data: Dictionary containing processed cosmic ray data
    """
    events = processed_data['events']
    
    # Create the main figure and subplots
    fig, (ax1, ax2, ax3) = plt.subplots(1, 3, figsize=(18, 9))
    
    # Initial plots
    energy_hist = plot_energy_histogram(ax1, events)
    time_scatter = plot_time_scatter(ax2, events)
    particle_pie = plot_particle_distribution(ax3, processed_data['particle_distribution'])
    
    # Add time slider for filtering
    ax_time = plt.axes((0.1, 0.07, 0.65, 0.03))
    
    time_slider = Slider(ax_time, 'Time Window (days)', 1, 30, valinit=30, valstep=1)
    
    # Add a reset button
    reset_button_ax = plt.axes((0.8, 0.07, 0.1, 0.04))
    reset_button = Button(reset_button_ax, 'Reset', color='lightgoldenrodyellow', hovercolor='0.975')
    
    # Add radio buttons for particle type selection
    particle_types = list(processed_data['particle_distribution'].keys())
    radio_ax = plt.axes((0.8, 0.3, 0.15, 0.15))
    radio_buttons = RadioButtons(radio_ax, ['All'] + particle_types)
    
    def update(val):
        time_window = time_slider.val
        selected_particle = radio_buttons.value_selected
        
        filtered_events = [e for e in events if e.timestamp >= events[-1].timestamp - timedelta(days=time_window)]
        
        if selected_particle != 'All':
            filtered_events = [e for e in filtered_events if e.particle_type == selected_particle]
        
        update_plots(filtered_events)
    
    def update_plots(filtered_events):
        ax1.clear()
        ax2.clear()
        ax3.clear()
        
        plot_energy_histogram(ax1, filtered_events)
        plot_time_scatter(ax2, filtered_events)
        plot_particle_distribution(ax3, particle_type_distribution(filtered_events))
        
        fig.canvas.draw_idle()
    
    def reset(event):
        time_slider.reset()
        radio_buttons.set_active(0)
        update(None)
    
    time_slider.on_changed(update)
    radio_buttons.on_clicked(update)
    reset_button.on_clicked(reset)
    
    plt.show()

def plot_periodogram(ax, frequencies, power):
    """
    Create a plot of the Lomb-Scargle periodogram.

    :param ax: Matplotlib axis object
    :param frequencies: Array of frequencies
    :param power: Array of power spectrum values
    """
    ax.plot(frequencies, power)
    ax.set_title('Periodogram of Cosmic Ray Energies')
    ax.set_xlabel('Frequency (Hz)')
    ax.set_ylabel('Power')
    ax.set_xscale('log')
    ax.set_yscale('log')

def display_data_quality_info(data_quality):
    """
    Display data quality information to the user.

    :param data_quality: Dictionary containing data quality information
    """
    integrity_results = data_quality['integrity_results']
    missing_intervals = data_quality['missing_intervals']

    print("Data Quality Report:")
    print(f"Total events: {integrity_results['total_events']}")
    print(f"Valid events: {integrity_results['valid_events']}")
    print(f"Error count: {integrity_results['error_count']}")
    print(f"Chronological order: {'Yes' if integrity_results['is_chronological'] else 'No'}")
    print(f"Duplicate events: {integrity_results['duplicate_count']}")

    if integrity_results['error_count'] > 0:
        print("\nError log:")
        for error in integrity_results['error_log'][:5]:  # Display first 5 errors
            print(error)
        if len(integrity_results['error_log']) > 5:
            print(f"... and {len(integrity_results['error_log']) - 5} more errors")

    if missing_intervals:
        print("\nMissing data intervals:")
        for start, end in missing_intervals[:5]:  # Display first 5 missing intervals
            print(f"From {start} to {end}")
        if len(missing_intervals) > 5:
            print(f"... and {len(missing_intervals) - 5} more missing intervals")

