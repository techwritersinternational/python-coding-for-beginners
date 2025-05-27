import os

def analyze_files(directory):
    word_count = 0
    for filename in os.listdir(directory):
        if filename.endswith('.txt'):
            filepath = os.path.join(directory, filename)
            with open(filepath, 'r') as file:
                for line in file:
                    # Split into words and count non-empty strings
                    words = [word for word in line.split() if word]
                    word_count += len(words)
    return word_count


# Usage
result = analyze_files('src/chapter10/')
print(result)