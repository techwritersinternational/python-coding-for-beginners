with open('spaceship_log.txt', 'r') as log_file:
    line_count = 0
    for line in log_file:
        line_count += 1
        
    print(f"The log contains {line_count} entries.")
