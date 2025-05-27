with open('spaceship_log.txt', 'r') as log_file:
    for line in log_file:
        print(f"Extracted line: {line.strip()}")  # strip() removes leading/trailing whitespace