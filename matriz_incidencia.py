import os
import pandas as pd
import preprocessing as pp

docs_terms =[]
terms = []
#terms_plus_frequencies = []
#terms_plus_logfreq = []
for i in range(20):
    path_file = os.path.join(os.getcwd(), (str(i + 1)))
    document = pp.read_file(path_file)
    document_sentences = pp.seg_into_senteces(document)
    document_words = pp.seg_into_words(document_sentences)
    words = pp.remove_stopwords(document_words)
    terms_of_eachdoc = pp.remove_punctuation(words)
    docs_terms.append(pp.reduce_tostem(terms_of_eachdoc))
    for j in range(len(docs_terms[i])):
        terms.append(docs_terms[i][j])

final_terms = list(set(terms))

# dataframe_tf_idf = pd.DataFrame({'Termos':final_terms})
# TODO matriz: https://stackoverflow.com/questions/12555323/adding-new-column-to-existing-dataframe-in-python-pandas
