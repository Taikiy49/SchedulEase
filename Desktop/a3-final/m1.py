import os
import json
import spacy
from bs4 import BeautifulSoup
from collections import defaultdict

# Load spaCy for tokenization and lemmatization
print("Loading the spaCy model...")
nlp = spacy.load("en_core_web_sm")
print("spaCy model loaded.")

class SearchEngine:
    def __init__(self, dataset_path):
        self.dataset_path = dataset_path
        self.inverted_index = defaultdict(list)
        self.doc_freq = defaultdict(int)
        self.total_docs = 0
        self.index_file = "inverted_index.json"

    def parse_html(self, html_content):
        soup = BeautifulSoup(html_content, 'html.parser')
        # Extract important tags to capture key information
        important_tags = ['title', 'h1', 'h2', 'h3', 'b', 'strong']
        words = []
        for tag in important_tags:
            for element in soup.find_all(tag):
                words.extend([token.lemma_.lower() for token in nlp(element.get_text()) if token.is_alpha])
        # Include all text from the page
        words.extend([token.lemma_.lower() for token in nlp(soup.get_text()) if token.is_alpha])
        return words

    def build_index(self):
        for domain in os.listdir(self.dataset_path):
            domain_path = os.path.join(self.dataset_path, domain)
            if os.path.isdir(domain_path):
                for filename in os.listdir(domain_path):
                    file_path = os.path.join(domain_path, filename)
                    print(f"Processing file: {file_path}")
                    with open(file_path, 'r', encoding='utf-8') as file:
                        data = json.load(file)
                        words = self.parse_html(data['content'])
                        doc_id = data['url']
                        # this counts the term frequencies for tf-idf computation later
                        word_freq = defaultdict(int)
                        for word in words:
                            word_freq[word] += 1
                        # Populate the inverted index
                        for word, freq in word_freq.items():
                            self.inverted_index[word].append((doc_id, freq))
                            self.doc_freq[word] += 1
                        self.total_docs += 1
        self.save_index()

    def save_index(self):
        with open(self.index_file, 'w', encoding='utf-8') as file:
            json.dump({
                'index': {key: val for key, val in self.inverted_index.items()},
                'doc_freq': dict(self.doc_freq),
                'total_docs': self.total_docs
            }, file)
        print(f"Index saved to {self.index_file}")

if __name__ == "__main__":
    dataset_path = 'test-directory'  # Ensure this directory exists with your dataset
    engine = SearchEngine(dataset_path)
    engine.build_index()

    # Compute and print analytics for your report
    num_docs = engine.total_docs
    num_unique_words = len(engine.inverted_index)
    index_size_bytes = os.path.getsize(engine.index_file)
    index_size_kb = index_size_bytes / 1024

    print("\n--- Index Analytics ---")
    print(f"Number of Indexed Documents: {num_docs}")
    print(f"Number of Unique Words: {num_unique_words}")
    print(f"Total Index Size (KB): {index_size_kb:.2f}")
