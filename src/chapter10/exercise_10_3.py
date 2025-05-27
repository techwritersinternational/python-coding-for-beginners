def redact_log(input_filename, sensitive_terms):
    """Redact sensitive information from log file."""
    # Read the log file
    with open(input_filename, 'r') as log_file:
        content = log_file.read()
    
    # Perform redaction
    redacted_content = content
    for term in sensitive_terms:
        redacted_content = redacted_content.replace(term, "REDACTED")
    
    # Print original and redacted versions
    print("Original Log:")
    print("-" * 50)
    print(content)
    
    print("\nRedacted Log:")
    print("-" * 50)
    print(redacted_content)
    
    print("-" * 50)
           

# Define sensitive terms
sensitive_terms = [
   "Deep Space Relay Station Beta",
   "Europa"
]

# Process the log file
redact_log('spaceship_log.txt', sensitive_terms)