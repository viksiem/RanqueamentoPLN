from nltk.corpus import stopwords
from nltk.tokenize import sent_tokenize
from nltk.tokenize import word_tokenize
from nltk.stem.snowball import SnowballStemmer
import string
import os
from collections import Counter
import math
from itertools import repeat

_punctuation = string.punctuation
_stemmer = SnowballStemmer('english')
_stopwords_list = stopwords.words('english')


# no win: os.chdir('C:\Users\meiski\Desktop\RanqueamentoPLN\corpus')
os.chdir('/home/meiski/PycharmProjects/RanqueamentoPLN/corpus')
_LOG_BASE = 10


# ref: https://wiki.python.org.br/TudoSobrePythoneUnicode
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


def add_stopwords():
    _stopwords_list.append('true')
    _stopwords_list.append('without')
    _stopwords_list.append('low')
    _stopwords_list.append('moreover')
    _stopwords_list.append('include')
    _stopwords_list.append('including')
    _stopwords_list.append('de')
    _stopwords_list.append('mixture')
    _stopwords_list.append('annotation')


def remove_stopwords(doc):
    add_stopwords()
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
    _docfrequency = []
    for n in range(len(_doc_frequency)):
        _docfrequency.append((float("%.3f" % (1 + math.log(_doc_frequency[n][1], _LOG_BASE)))))
    return _docfrequency


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


def tf_idf(log, _idf, _docterms, _final_terms):
    _tf_idf = [[] for j in repeat(None, len(_final_terms))]
    for i, term in enumerate(_final_terms):
        for n, doc in enumerate(_docterms):

    #VAI TER QUE PERCORRER O LOG TMB
            if term in doc:
                logindex = log.index(term)
                print logindex
                _tf_idf[i].insert(n, float("%.3f" % (log[logindex] * _idf[i])))
                #print '     _idf[i]: ',_idf[i]
                #print '     _df[i]: ', _df[i]
                #print '_df[i] * _idf[i]: ',_tf_idf[i]
            else:
                print i, n
                _tf_idf[i].insert(n, 0)

    return _tf_idf