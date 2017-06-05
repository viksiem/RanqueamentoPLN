from operator import itemgetter
from nltk.corpus import stopwords
from nltk.tokenize import sent_tokenize
from nltk.tokenize import word_tokenize
from nltk.stem.snowball import SnowballStemmer
import string
import os
from collections import Counter
import matriz_incidencia as mi

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
    punctuation_free = [w for w in final_words if not w in punctuation]
    return punctuation_free


def reduce_tostem(doc):
    doc_stems = [stemmer.stem(w) for w in punctuation_free]
    return doc_stems


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

w, h = 20, 59;
matrix = [[0 for x in range(w)] for y in range(h)]
for i in range(0, 20):
    print i
    doc_terms = Counter(final_docs[i]).most_common()
    for p in range(0,59):
        mi.MatrizIncidencia.receive_data(doc_terms[p][0], doc_terms[p][1])
    print matrix

#    matriz = [len(doc_terms)][20]
    #print doc_terms[59] #59 eh o tamanho do menor abstract
#    matriz[i][i]