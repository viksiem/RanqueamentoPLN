from nltk.corpus import stopwords
from nltk.tokenize import sent_tokenize
from nltk.tokenize import word_tokenize
from nltk.stem.snowball import SnowballStemmer
import string
import os
from collections import Counter
import math

# TODO metodo pra fazer lista de todos os termos
# TODO adicionar nas stopwords palavras como background, conclusions
# TODO utilizar panda para montar e printar matriz
# TODO gerar matriz de frequencia!

stopwords_list = stopwords.words('english')
punctuation = string.punctuation
stemmer = SnowballStemmer('english')

# para o win: os.chdir('C:\Users\meiski\Desktop\RanqueamentoPLN\corpus')
os.chdir('/home/meiski/PycharmProjects/RanqueamentoPLN/corpus')
LOG_BASE = 10


# https://wiki.python.org.br/TudoSobrePythoneUnicode
def read_file(i_file):
    i_file = open(i_file)
    data_file = i_file.read()
    data_file = unicode(data_file, 'utf-8')
    return data_file


def seg_into_senteces(doc):
    sentences = sent_tokenize(doc)
    return sentences


def seg_into_words(doc):
    words = []
    for d in doc:
        words += word_tokenize(d)
    return words


def remove_stopwords(doc):
    finalwords = [w for w in doc if not w.lower() in stopwords_list]
    return finalwords


def remove_punctuation(doc):
    punctuation_free = [w for w in doc if not w in punctuation]
    return punctuation_free


def reduce_tostem(doc):
    doc_stems = [stemmer.stem(w) for w in doc]
    return doc_stems


def count_frequencies(doc):
    terms_plus_freq = Counter(doc).most_common()
    return terms_plus_freq


# CALCULA O DF DE TODOS OS TERMOS
# --OK
def doc_frequency(_terms_of_all, _docterms):  # docterms = 20, terms of all = 1202
    df = []
    for t in _terms_of_all:  # t = algum termo
        tmp = 0
        for d in range(len(_docterms)):
            if t in _docterms[d]:
                tmp += 1
            else:
                tmp += 0
        # end for
        df.append(tmp)
    # end for

    return df


def log_tf(_doc_frequency):
    for n in range(len(_doc_frequency)):
        _doc_frequency[n] = list(_doc_frequency[n])
        _doc_frequency[n][1] = (float("%.3f" % (1 + math.log(_doc_frequency[n][1], LOG_BASE))))
    return _doc_frequency


def idf(_df, n_docs):
    _idf = []
    for p in range(len(_df)):
        _idf.append(float("%.3f" % (math.log(n_docs / _df[p], LOG_BASE))))
    return _idf


def tf_idf(_df, _idf):
    _tf_idf = []
    for i in range(len(_idf)):
        _tf_idf.append(float("%.3f" % (_df[i] * _idf[i])))
    return _tf_idf


# REALIZA TOD@ O PREPROCESSAMENTO DO CORPUS
   # terms_plus_frequencies.append(count_frequencies(docs_terms[i]))
   # terms_plus_logfreq.append(log_tf(terms_plus_frequencies[i]))


''' # COLOCA TODOS OS TERMOS EM UM VETOR SEM DUPLICATAS
terms = []
for i in range(len(docs_terms)):

    for j in range(len(terms_plus_logfreq[i])):
        terms.append(terms_plus_logfreq[i][j][0])

final_terms = list(set(terms))
DF = doc_frequency(final_terms, docs_terms)
IDF = idf(DF, len(docs_terms))
TFIDF = tf_idf(DF, IDF)'''