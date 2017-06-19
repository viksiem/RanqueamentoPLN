import os
import pandas as pd
import preprocessing as pp

docs_terms = []
terms = []
terms_plus_frequencies = []
terms_plus_logfreq = []
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
    terms_plus_logfreq.append(pp.log_tf(terms_plus_frequencies[i]))

    for j in range(len(docs_terms[i])):
        terms.append(docs_terms[i][j])

    final_terms = list(set(terms))

DF = pp.doc_frequency(final_terms, docs_terms)
IDF = pp.idf(DF, len(docs_terms))
TF_IDF = pp.tf_idf(DF, IDF, docs_terms, final_terms)


df_tfidf = pd.DataFrame(TF_IDF)

df_tfidf['Sum TF-IDF'] = df_tfidf.sum(axis=1)

list_of_sum = df_tfidf['Sum TF-IDF'].tolist()

for t in range(10):
    tmp_term = list_of_sum.index(max(list_of_sum))
    list_of_sum.pop(tmp_term)
    print 'Termo ', t, 'mais relevante: ', final_terms[tmp_term]

#print sorted(list_of_sum, reverse=True)
