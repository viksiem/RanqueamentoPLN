from nltk.corpus import stopwords
from nltk.tokenize import sent_tokenize
from nltk.tokenize import word_tokenize
from nltk import pos_tag
from nltk.stem.snowball import SnowballStemmer
import string
import os
from collections import Counter
import math
import pandas as pd

#TODO metodo pra fazer lista de todos os termos
#TODO adicionar nas stopwords palavras como background, conclusions
#TODO utilizar panda para montar e printar matriz
#TODO gerar matriz de frequencia!

stopwords_list = stopwords.words('english')
punctuation = string.punctuation
stemmer = SnowballStemmer('english')
os.chdir('C:\Users\meiski\Desktop\RanqueamentoPLN\corpus')


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


def tags (doc):
    postag = pos_tag(doc)
    return postag


def reduce_tostem(doc):
    doc_stems = [stemmer.stem(w) for w in doc]
    return doc_stems


def count_frequencies(doc):
    terms_plus_freq = Counter(doc).most_common()
    return terms_plus_freq


# CALCULA O DF DE TODOS OS TERMOS
def doc_frequency(terms_of_all, docterms):
    df = [0] * len(terms_of_all)
    k = 0
    for t in terms_of_all:
        for d in range(len(docterms)):
            if t in docterms[d]:
                df[k] += 1
            else:
                df[k] += 0
        k += 1
    return df


def log_tf(doc_frequency):
    for n in range(len(doc_frequency)):
        doc_frequency[n] = list(doc_frequency[n])
        doc_frequency[n][1] = (float("%.3f" %(1 + math.log(doc_frequency[n][1], 10))))

    return doc_frequency


def idf(_df):
    _idf = []
    for p in range(1202):
        _idf.append(float("%.3f" % (math.log(20/_df[p], 10))))
    return _idf


def tf_idf(_df, _idf):
    _tf_idf = []
    for i in range(len(_idf)):
        _tf_idf.append(float("%.3f" % (_df[i] * _idf[i])))
    return _tf_idf


#REALIZA TOD@ O PREPROCESSAMENTO DO CORPUS
docs_terms = []
terms_plus_logfreq=[]
for i in range(20):
    path_file = os.path.join(os.getcwd(), (str(i+1)))
    document = read_file(path_file)
    document_sentences = seg_into_senteces(document)
    document_words = seg_into_words(document_sentences)
    final_words = remove_stopwords(document_words)
    terms_of_eachdoc = remove_punctuation(final_words)
    docs_terms.append(reduce_tostem(terms_of_eachdoc))
    terms_plus_frequencies = count_frequencies(docs_terms[i])
    terms_plus_logfreq.append(log_tf(terms_plus_frequencies))

#COLOCA TODOS OS TERMOS EM UM VETOR SEM DUPLICATAS
terms = []
for i in range(len(docs_terms)):
    #terms_plus_frequencies = Counter(docs_terms[i]).most_common()
    #print terms_plus_frequencies
    for j in range(len(terms_plus_frequencies[i])):
        terms.append(terms_plus_frequencies[j][0])
final_terms = list(set(terms))
DF = doc_frequency(final_terms,docs_terms)
IDF = idf(DF)
TFIDF = tf_idf(DF, IDF)

'''dataframe_tf_idf = pd.DataFrame({'Termos':terms})
print data_frame'''