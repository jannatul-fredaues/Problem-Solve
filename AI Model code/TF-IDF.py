import math
from collections import Counter

def compute_tf(doc):
    words = doc.lower().split()
    counts = Counter(words)
    return {word: count / len(words) for word, count in counts.items()}

def compute_idf(corpus):
    n_docs = len(corpus)
    idf_dict = Counter()
    for doc in corpus:
        unique_words = set(doc.lower().split())
        for word in unique_words:
            idf_dict[word] += 1
    
    # Adding 1 to denominator to avoid division by zero (smoothing)
    return {word: math.log(n_docs / count) for word, count in idf_dict.items()}

# Example usage
corpus = ["The cat sat", "The dog sat"]
tf_scores = [compute_tf(doc) for doc in corpus]
idf_scores = compute_idf(corpus)

# Final TF-IDF for first document
tfidf_doc1 = {word: tf * idf_scores[word] for word, tf in tf_scores[0].items()}
print(tfidf_doc1)
