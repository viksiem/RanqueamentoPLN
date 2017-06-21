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


os.chdir('C:\Users\meiski\Desktop\RanqueamentoPLN\corpus')
#os.chdir('/home/meiski/PycharmProjects/RanqueamentoPLN/corpus')
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
   # _stopwords_list.append('variants')
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


def flog_tf(_doc_frequency):
    f_docfrequency = []
    for n in range(len(_doc_frequency)):
        f_docfrequency.append(float("%.3f" % (1 + math.log(_doc_frequency[n][1], _LOG_BASE))))
    return f_docfrequency


def tlog_tf(_doc_frequency):
    t_docfrequency = []
    for n in range(len(_doc_frequency)):
        t_docfrequency.append(_doc_frequency[n][0])
    return t_docfrequency


def doc_frequency(_terms_of_all, _docterms):  # docterms = 20, terms of all = 1194
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


#_tf_idf = [[TERMO1[DOC1, DOC2, ...,DOC20], TERMO2[DOC1, DOC2, ...,DOC20]]
def tf_idf(_log_terms, _log_freq, _idf, _docterms, _final_terms):
    bydocTFIDF =[]
    _tf_idf = [] #for j in repeat(None, len(_final_terms))]
    for i, term in enumerate(_final_terms):
        for n, doc in enumerate(_docterms):
            if term in doc:
                termindex = _log_terms[n].index(term)
                bydocTFIDF.append(float("%.3f" % (_log_freq[n][termindex] * _idf[i])))

            else:
                bydocTFIDF.append(0)
        tmp = list(bydocTFIDF)
        _tf_idf.append(tmp)
        del bydocTFIDF[:]

    return _tf_idf
