import os
import json
import math
import spacy
from collections import defaultdict
from bs4 import BeautifulSoup

# for this m2 we are also going to continue using the spaCy model
# i like this one better than nltk because for some reason my nltk is not working properly
print("Loading the spaCy model...")
nlp = spacy.load("en_core_web_sm")
print("spaCy model loaded.")

class SearchEngine:
    def __init__(self, dataset_path=None):
        # in m2 we only need to load the pre-built index, so dataset_path is not going to be used
        self.inverted_index = defaultdict(list) # inverted index
        self.doc_freq = defaultdict(int) # document frequency
        self.total_docs = 0 # total number of documents
        self.index_file = "inverted_index.json" # index file (make sure we're using the same invertex_index json we have multiple)

    def load_index(self):
        if os.path.exists(self.index_file):
            with open(self.index_file, 'r', encoding='utf-8') as file: # open the index file
                data = json.load(file)
                self.inverted_index = defaultdict(list, data['index']) # load the inverted index
                self.doc_freq = defaultdict(int, data['doc_freq']) # load the document frequency
                self.total_docs = data['total_docs'] # load the total number of documents
            print(f"Index loaded from {self.index_file}")
        else:
            print("No index file found. Please build the index first (run m1.py).")

    def tf_idf(self, term, doc_id): # tf-idf function is good because it helps us rank the documents
        # what it does is it calculates the term frequency and the inverse document frequency
        # then it multiplies the two values to get the tf-idf score
        postings = dict(self.inverted_index.get(term, []))
        tf = postings.get(doc_id, 0)
        if tf == 0:
            return 0
        idf = math.log((self.total_docs + 1) / (self.doc_freq.get(term, 1) + 1)) + 1 # this is the formula for idf
        return tf * idf

    def search(self, query):
        query_terms = [token.lemma_.lower() for token in nlp(query) if token.is_alpha] # tokenize and lemmatize the query
        doc_scores = defaultdict(float) # document scores
        doc_sets = []
        for term in query_terms:
            docs = set(doc_id for doc_id, _ in self.inverted_index.get(term, [])) # get the documents for each term
            doc_sets.append(docs)
        common_docs = set.intersection(*doc_sets) if doc_sets else set() # get the common documents

        for doc_id in common_docs:
            for term in query_terms:
                doc_scores[doc_id] += self.tf_idf(term, doc_id) # calculate the tf-idf score for each document

        ranked_docs = sorted(doc_scores.items(), key=lambda x: x[1], reverse=True) # sort the documents by score
        return ranked_docs[:5]

if __name__ == "__main__":
    engine = SearchEngine()
    engine.load_index()
    queries = [
        "Iftekhar Ahmed",
        "machine learning",
        "ACM",
        "master of software engineering"
    ]

    print("\n--- Search Results (Top 5 URLs for each query) ---")
    for query in queries:
        results = engine.search(query)
        print(f"\nQuery: '{query}'")
        if results:
            for rank, (url, score) in enumerate(results, start=1):
                print(f"{rank}. URL: {url} (Score: {score:.4f})")
        else:
            print("No results found.")
