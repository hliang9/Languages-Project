import sys
import gensim
from gensim import corpora
import pickle
import random
from nltk.corpus import stopwords
stop_words = stopwords.words('english')

tokens = []
with open(sys.argv[1]) as reader:
    for line in reader: 
        if random.randint(0, 15) == 1:
            line_tokens = [token for token in line.split(' ') if len(token) > 2 and token not in stop_words]
            tokens.append(line_tokens)
    dictionary = corpora.Dictionary(tokens)
    corpus = [dictionary.doc2bow(text_lst) for text_lst in tokens]
    pickle.dump(corpus, open('corpus.pkl', 'wb'))
    dictionary.save('dictionary.gensim')
