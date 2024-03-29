from collections import OrderedDict
import os
from sklearn.cluster import KMeans
from sklearn.neighbors import KNeighborsClassifier
import matplotlib.pyplot as plt

import cluster as clus
import pandas as pd
import numpy as np
import preprocessing as pp

MOST_RELEVANT = 15
DOC_NEWWORDS = 'foreign_words.txt'
DATA_CSV = 'termos relevantes.csv'
docs_terms = []
terms = []
terms_plus_frequencies = []
log_terms = []
log_freq = []
tf = []

for i in range(20):
    path_file = os.path.join(os.getcwd(), (str(i + 1)))

    document = pp.read_file(path_file)

    document_sentences = pp.seg_into_senteces(document)

    document_words = pp.seg_into_words(document_sentences)

    words = pp.remove_stopwords(document_words)

    terms_of_eachdoc = pp.remove_punctuation(words)

    docs_terms.append(pp.reduce_tostem(terms_of_eachdoc))

    terms_plus_frequencies.append(pp.count_frequencies(docs_terms[i]))

    log_terms.append(pp.tlog_tf(terms_plus_frequencies[i]))

    log_freq.append(pp.flog_tf(terms_plus_frequencies[i]))


    for j in range(len(terms_plus_frequencies[i])):
        terms.append(terms_plus_frequencies[i][j][0])

final_terms = list(OrderedDict.fromkeys(terms))

DF = pp.doc_frequency(final_terms, docs_terms)
IDF = pp.idf(DF, len(docs_terms))
TF_IDF = pp.tf_idf(log_terms, log_freq, IDF, docs_terms, final_terms)

df_tfidf = pd.DataFrame(TF_IDF)
df_tfidf['Sum TF-IDF'] = df_tfidf.sum(axis=1)
list_of_sum = df_tfidf['Sum TF-IDF'].tolist()


# Encontra os termos mais relevantes e gera matriz de frequencia absoluta
most_relevant = []          # os mais relevantes
most_pafreq = []            # os mais relevantes com a freq absoluta

for t in range(MOST_RELEVANT):
    most_relevant.append(list_of_sum.index(max(list_of_sum)))
    '''print 'Most relevant', t+1, ':', final_terms[most_relevant[t]], list_of_sum[most_relevant[t]]'''

    most_pafreq.append(clus.absolut_freq(terms_plus_frequencies, final_terms[most_relevant[t]]))
    commum = pd.DataFrame({final_terms[most_relevant[t]]: most_pafreq[t]})
    '''print commum'''

    list_of_sum.pop(most_relevant[t])
    final_terms.pop(most_relevant[t])


#Processa os novos termos
foreign_words = clus.process_new_words(DOC_NEWWORDS)
for i, w in enumerate(foreign_words):
    if w in final_terms:
        words_plus_frequencies = clus.absolut_freq(terms_plus_frequencies, w)
        '''print w, words_plus_frequencies'''

# Clusteriza os documentos
#data = pd.read_csv(DATA_CSV)
#data.as_matrix()
#model = KMeans(n_clusters=7).fit_predict(data)

#model.fit(data)

