from collections import Counter

def find_hapax_legomena(filename):
    """Find words that appear exactly once in the text."""
    # Read the file
    with open(filename, 'r', encoding='utf-8') as file:
        text = file.read().lower()
    
    # Replace punctuation with spaces
    for char in '.,!?;:()[]{}"\'-_—‘“':
        text = text.replace(char, ' ')
    
    # Split into words and remove empty strings
    words = [word for word in text.split() if word]
    
    # Count word occurrences
    word_counts = Counter(words)
    
    # Find hapax legomena (words that appear once)
    hapax = [word for word, count in word_counts.items() if count == 1]
    
    # Sort alphabetically
    hapax.sort()
    
    # Print results
    print(f"\nFound {len(hapax)} hapax legomena in {filename}:")
    print("-" * 50)
    
    for word in hapax:
        print(word)

    print("-" * 50)
    print(f"Total unique words: {len(word_counts)}")
    print(f"Total hapax legomena: {len(hapax)}")
    print(f"Percentage of vocabulary: {(len(hapax) / len(word_counts)) * 100:.1f}%")
    

# Find hapax legomena
find_hapax_legomena('frankenstein.txt')