from nltk.corpus import stopwords
from nltk.tokenize import sent_tokenize
from nltk.tokenize import word_tokenize
from nltk import pos_tag
from nltk.stem.snowball import SnowballStemmer
import string
import os
import numpy
from collections import Counter
import math
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
    print doc_frequency
    print 'len(doc_frequency)', len(doc_frequency)
    for n in range(len(doc_frequency)):
        doc_frequency[n] = list(doc_frequency[n])
        #print 'doc_frequency[n]: ', doc_frequency[n]
        doc_frequency[n][1] = 1 + math.log(doc_frequency[n][1], 10)
        #print 'doc_terms[n][1]: ', doc_frequency[n][1]

    return doc_frequency


final_docs = []
for i in os.listdir(os.getcwd()):
    path_file = os.path.join(os.getcwd(), i)
    document = read_file(path_file)
    document_sentences = seg_into_senteces(document)
    document_words = seg_into_words(document_sentences)
    final_words = remove_stopwords(document_words)
    punctuation_free = remove_punctuation(final_words)
    stems = reduce_tostem(punctuation_free)
    final_docs.append(stems)

terms =[]
for i in range(len(final_docs)):
    #print 'I: ', i
    #print 'final_docs[',i,'] ',final_docs[i], 'len(final_docs): ',len(final_docs)
    doc_terms = Counter(final_docs[i]).most_common() #final_docs[i] eh um vetor de termos do doc = doc_terms
    print 'doc_terms',doc_terms
    tf_ponderada = doc_terms
    tf_ponderada[i] = log_tf(doc_terms)
    'print tf_ponderada[i]: ',tf_ponderada[i]
    'print tf_ponderada: ',tf_ponderada

    #printa e etribui todos os termos
    for j in range(len(doc_terms)):
        #print '         len(doc_terms): ',len(doc_terms)
        #print 'doc_terms[',i,']',doc_terms[j]
        # doc_terms[j][0] acessa so o termo
        terms.append(doc_terms[j][0])
        print 'terms [',j,']: ',terms[j]

#TODO utilizar panda para printar

print 'final_terms length :',len(terms)
print 'final terms TOTAL: ',terms
final_terms = set(terms)
final_terms = list(final_terms)
print 'final_terms length sem duplicatas: ',len(final_terms)
print 'final terms TOTAL sem duplicatas: ',final_terms
print 'final terms [2]', final_terms[2]




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