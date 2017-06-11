from nltk.corpus import stopwords
from nltk.tokenize import sent_tokenize
from nltk.tokenize import word_tokenize
from nltk import pos_tag
from nltk.stem.snowball import SnowballStemmer
import string
import os
from collections import Counter
import math
import numpy
#import pandas as pd

# TODO adicionar nas stopwords palavras como background, conclusions

stopwords_list = stopwords.words('english')
punctuation = string.punctuation
stemmer = SnowballStemmer('english')
os.chdir('/home/meiski/PycharmProjects/RanqueamentoPLN/corpus')


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


def log_tf(doc_frequency):
    #print doc_frequency
    #print 'len(doc_frequency)', len(doc_frequency)
    for n in range(len(doc_frequency)):
        doc_frequency[n] = list(doc_frequency[n])
        #print 'doc_frequency[n]: ', doc_frequency[n]
        doc_frequency[n][1] = 1 + math.log(doc_frequency[n][1], 10)
        #print 'doc_terms[n][1]: ', doc_frequency[n][1]

    return doc_frequency


def count_frequencies(doc):
    terms_plus_freq = Counter(doc).most_common()
    return terms_plus_freq


docs_terms = []
for i in range(20):
    path_file = os.path.join(os.getcwd(), (str(i+1)))
    document = read_file(path_file)
    document_sentences = seg_into_senteces(document)
    document_words = seg_into_words(document_sentences)
    final_words = remove_stopwords(document_words)
    punctuation_free = remove_punctuation(final_words)
    docs_terms.append(reduce_tostem(punctuation_free))
    terms_plus_frequencies = count_frequencies(docs_terms[i])
    print 'terms_plus_frequencies',terms_plus_frequencies

#TODO metodo pra fazer lista de todos os termos
#def list_of_all_terms():
#terms =[]



terms =[]
for i in range(len(docs_terms)):
    terms_plus_frequencies = Counter(docs_terms[i]).most_common()
    #tf_ponderada = doc_terms
    #tf_ponderada[i] = log_tf(doc_terms)
    #print 'print tf_ponderada[i]: ',tf_ponderada[i]
    #print 'print tf_ponderada: ',tf_ponderada
    for j in range(len(terms_plus_frequencies)):
        terms.append(terms_plus_frequencies[j][0])
final_terms = list(set(terms))




#TODO utilizar panda para printar matriz
##############################################
#REMEMBER: Index begins in 0
#matriz = numpy.arange(1202*21).reshape(1202,21)
#i popula os termos
#for i in range(len(final_terms)):
 #   print 'final_terms ', i,': ', final_terms[i]
 #   print 'matriz[i][1]: ',matriz[i][1]
 #   matriz[i][1] = final_terms[i]
 #   print 'matriz[',i,'][1]', matriz[i][1]
##############################################