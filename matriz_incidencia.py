import os
import part2 as pt2
import pandas as pd
import preprocessing as pp

MOST_RELEVANT = 15
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

final_terms = list(set(terms))
DF = pp.doc_frequency(final_terms, docs_terms)
IDF = pp.idf(DF, len(docs_terms))
TF_IDF = pp.tf_idf(log_terms, log_freq, IDF, docs_terms, final_terms)

df_tfidf = pd.DataFrame(TF_IDF)

df_tfidf['Sum TF-IDF'] = df_tfidf.sum(axis=1)
#print df_tfidf

list_of_sum = df_tfidf['Sum TF-IDF'].tolist()

most_relevant = []
most_pafreq = []  # os mais relevantes com a freq absoluta
for t in range(MOST_RELEVANT):
    most_relevant.append(list_of_sum.index(max(list_of_sum)))
    list_of_sum.pop(most_relevant[t])
    print 'Most relevant', t+1, ':', final_terms[most_relevant[t]]
    most_pafreq.append(pt2.absolut_freq(terms_plus_frequencies, final_terms[most_relevant[t]]))
    commum = pd.DataFrame({final_terms[most_relevant[t]]: most_pafreq[t]})
    '''print commum'''
