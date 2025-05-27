import random
import time

def generate_initial_seed():
    """Generate an initial seed based on the current time."""
    return int(time.time() * 1000)  # Convert to milliseconds for more variation

def tribonacci_sequence(n, seed):
    """Generate a Tribonacci sequence of length n, starting with the given seed."""
    sequence = [seed, seed + 1, seed + 2]
    for i in range(3, n):
        sequence.append(sum(sequence[-3:]))
    return sequence

def generate_next_seed(previous_seed):
    """Generate the next seed value based on the previous seed."""
    sequence = tribonacci_sequence(10, previous_seed)
    return sequence[-1] % (2**32)  # Ensure the seed is within 32-bit integer range

# Example usage
if __name__ == "__main__":
    initial_seed = generate_initial_seed()
    print(f"Initial seed: {initial_seed}")
    
    next_seed = generate_initial_seed()
    #next_seed = generate_next_seed(initial_seed)
    print(f"Next seed: {next_seed}")
    
    another_seed  = generate_initial_seed()
    #another_seed = generate_next_seed(next_seed)
    print(f"Another seed: {another_seed}")