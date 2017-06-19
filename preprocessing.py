from nltk.corpus import stopwords
from nltk.tokenize import sent_tokenize
from nltk.tokenize import word_tokenize
from nltk.stem.snowball import SnowballStemmer
import string
import os
from collections import Counter
import math
from itertools import repeat


_stopwords_list = stopwords.words('english')
_punctuation = string.punctuation
_stemmer = SnowballStemmer('english')

# no win: os.chdir('C:\Users\meiski\Desktop\RanqueamentoPLN\corpus')
os.chdir('/home/meiski/PycharmProjects/RanqueamentoPLN/corpus')
_LOG_BASE = 10


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
    finalwords = [w for w in doc if not w.lower() in _stopwords_list]
    return finalwords


def remove_punctuation(doc):
    punctuation_free = [w for w in doc if not w in _punctuation]
    return punctuation_free


def reduce_tostem(doc):
    doc_stems = [_stemmer.stem(w) for w in doc]
    return doc_stems


def count_frequencies(doc):
    terms_plus_freq = Counter(doc).most_common()
    return terms_plus_freq


def log_tf(_doc_frequency):
    for n in range(len(_doc_frequency)):
        _doc_frequency[n] = list(_doc_frequency[n])
        _doc_frequency[n][1] = (float("%.3f" % (1 + math.log(_doc_frequency[n][1], _LOG_BASE))))
    return _doc_frequency


# CALCULA O DF DE TODOS OS TERMOS
def doc_frequency(_terms_of_all, _docterms):  # docterms = 20, terms of all = 1202
    df = []
    for t in _terms_of_all:  # t = algum termo
        tmp = 0
        for d in range(len(_docterms)):
            if t in _docterms[d]:
                tmp += 1
            else:
                tmp += 0

        df.append(tmp)

    return df


def idf(_df, n_docs):
    _idf = []
    for p in range(len(_df)):
        _idf.append(float("%.3f" % (math.log(n_docs / _df[p], _LOG_BASE))))
    return _idf


def tf_idf(_df, _idf, _docterms, _final_terms):
    _tf_idf = [[] for j in repeat(None, len(_final_terms))]
    for i, term in enumerate(_final_terms):
        for n, doc in enumerate(_docterms):

            if term in doc:
                _tf_idf[i].append(float("%.3f" % (_df[i] * _idf[i])))
            else:
                _tf_idf[i].append(0)

    return _tf_idf