from nltk.corpus import stopwords
import pickle
import os
import random
from collections import Counter
import numpy as np
import sys

num_topics = 500
stop_words = stopwords.words('english')
        
word_counts = Counter()
documents = []

DIRECTORY = 'topicmodel_pickle'

for line in open("all_text_v1_v2_nopunct.txt"):
    #line = line.lower()
    if random.randint(0, 15) == 1:
        line_tokens = [token for token in line.split(' ') if len(token) > 2 and token not in stop_words]
        word_counts.update(line_tokens)
        doc_topic_counts = np.zeros(num_topics, dtype=int)
        documents.append({ "original": line, "token_strings": line_tokens, "topic_counts": doc_topic_counts })

# Get vocabulary
vocabulary = list(word_counts.keys())
word_ids = { w: i for (i, w) in enumerate(vocabulary) }

## With the vocabulary, go back and create arrays of numeric word IDs
for document in documents:
    tokens = document["token_strings"]
    doc_topic_counts = document["topic_counts"]
    
    doc_tokens = np.ndarray(len(tokens), dtype=int)
    doc_topics = np.ndarray(len(tokens), dtype=int)
    topic_changes = np.zeros(len(tokens), dtype=int)
    
    for i, w in enumerate(tokens):
        doc_tokens[i] = word_ids[w]
        ## topics will be initialized by the model
    
    document["doc_tokens"] = doc_tokens
    document["doc_topics"] = doc_topics
    document["topic_changes"] = topic_changes

pickle.dump(word_counts, open(os.path.join(DIRECTORY,'word_counts.pkl'), 'wb'))
pickle.dump(documents, open(os.path.join(DIRECTORY, 'documents.pkl'), 'wb'))
pickle.dump(word_ids, open(os.path.join(DIRECTORY, 'word_ids.pkl'), 'wb'))
pickle.dump(vocabulary, open(os.path.join(DIRECTORY,'vocabulary.pkl'), 'wb'))