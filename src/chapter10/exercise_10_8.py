import os
from collections import Counter

class CorpusAnalyzer:
   def __init__(self, search_terms):
       self.search_terms = [term.lower() for term in search_terms]
       self.results = {
           'files_processed': 0,
           'total_words': 0,
           'term_counts': Counter(),
           'longest_file': ('', 0),
           'shortest_file': ('', float('inf')),
           'file_details': []
       }

   def analyze_corpus(self, directory):
       """Analyze all text files in the given directory."""
       print(f"Analyzing corpus in: {directory}")
       print("-" * 50)
       
       try:
           # Get list of text files
           files = [file for file in os.listdir(directory) 
                   if file.endswith('.txt')]
                    
           # Process each file
           for filename in files:
               self.process_file(os.path.join(directory, filename))
           
           # Generate and print report
           self.generate_report()
           
       except Exception as e:
           print(f"Error analyzing corpus: {str(e)}")
   
   def process_file(self, filepath):
       """Process a single file in the corpus."""
       try:
           with open(filepath, 'r', encoding='utf-8') as file:
               content = file.read().lower()
               words = content.split()
               word_count = len(words)
               
               # Update statistics
               filename = os.path.basename(filepath)
               self.results['files_processed'] += 1
               self.results['total_words'] += word_count
               
               # Check if it's longest or shortest file
               if word_count > self.results['longest_file'][1]:
                   self.results['longest_file'] = (filename, word_count)
               if word_count < self.results['shortest_file'][1]:
                   self.results['shortest_file'] = (filename, word_count)
               
               # Count search terms
               term_counts = Counter()
               for term in self.search_terms:
                   term_counts[term] = content.count(term)
               
               # Update overall term counts
               self.results['term_counts'].update(term_counts)
               
               # Store file details
               self.results['file_details'].append({
                   'name': filename,
                   'word_count': word_count,
                   'term_counts': dict(term_counts)
               })
               
       except Exception as e:
           print(f"Error processing {filepath}: {str(e)}")
   
   def generate_report(self):
       """Generate and print analysis report."""
       print("\nCorpus Analysis Report")
       print("=" * 50)
       
       # General statistics
       print("\nGeneral Statistics:")
       print(f"Files processed: {self.results['files_processed']}")
       print(f"Total words: {self.results['total_words']:,}")
       avg_words = self.results['total_words'] / self.results['files_processed']
       print(f"Average words per file: {avg_words:,.1f}")
       
       # Document length information
       print("\nDocument Lengths:")
       longest = self.results['longest_file']
       shortest = self.results['shortest_file']
       print(f"Longest: {longest[0]} ({longest[1]:,} words)")
       print(f"Shortest: {shortest[0]} ({shortest[1]:,} words)")
       
       # Search term frequencies
       print("\nSearch Term Frequencies:")
       for term, count in self.results['term_counts'].most_common():
           print(f"'{term}': {count:,} occurrences")
       
       # Individual file details
       print("\nIndividual File Analysis:")
       print("-" * 50)
       for file_info in self.results['file_details']:
           print(f"\n{file_info['name']}:")
           print(f"Word count: {file_info['word_count']:,}")
           print("Term counts:")
           for term, count in file_info['term_counts'].items():
               if count > 0:
                   print(f"  - '{term}': {count}")


# Create analyzer with search terms
search_terms = ["alien", "spacecraft", "rocket", "technology"]
analyzer = CorpusAnalyzer(search_terms)

# Analyze the corpus
analyzer.analyze_corpus("scifi_corpus")