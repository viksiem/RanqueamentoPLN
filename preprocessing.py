from nltk.corpus import stopwords
from nltk.tokenize import sent_tokenize
from nltk.tokenize import word_tokenize
from nltk import pos_tag, WordNetLemmatizer
from nltk.stem.snowball import SnowballStemmer
import string
import os
#from operator import itemgetter
from collections import Counter
import pandas as pd

# TODO adicionar nas stopwords palavras como background, conclusions

stopwords_list = stopwords.words('english')
punctuation = string.punctuation
stemmer = SnowballStemmer('english')
lemmatizer = WordNetLemmatizer()
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


#def lemmas(doc):
 #   lemmas = []
  #  for w in doc:
   #     if w[1].startswith('J'):
    #        pos = wordnet.ADJ
     #   elif w[1].startswith('V'):
      #      pos = wordnet.VERB
       # elif w[1].startswith('N'):
       #     pos = wordnet.NOUN
      #  elif w[1].startswith('R'):
     #       pos = wordnet.ADV
    #    else:
   #         pos = wordnet.NOUN
  #      lemmas.append(lemmatizer.lemmatize(w[0], pos))
 #   return lemmas


final_docs = []
for i in os.listdir(os.getcwd()):
    path_file = os.path.join(os.getcwd(), i)
    document = read_file(path_file)
    document_sentences = seg_into_senteces(document)
    document_words = seg_into_words(document_sentences)
    final_words = remove_stopwords(document_words)
    punctuation_free = remove_punctuation(final_words)
    stems = reduce_tostem(punctuation_free)
    #with_tag = tags(stems)
    #tfidf_vectorizer = TfidfVectorizer(tokenizer=lemmas(with_tag))
    #tfs = tfidf_vectorizer.fit_transform(np.array(document_sentences))
    #print(tfs.shape)
    final_docs.append(stems)

terms =[]
for i in range(len(final_docs)):
    print 'I: ', i
    print 'final_docs[',i,'] ',final_docs[i], 'len(final_docs): ',len(final_docs)
    doc_terms = Counter(final_docs[i]).most_common()
    print 'doc_terms',doc_terms

    #printa e etribui todos os termos
    for j in range(len(doc_terms)):
        print 'doc_terms[',i,']',doc_terms[j]
        # doc_terms[j][0] acessa so o termo
        terms.append(doc_terms[j][0])
        print 'final_terms [',j,']: ',terms[j]
    matriz = pd.DataFrame(doc_terms)
    matriz.append(pd.DataFrame(doc_terms[0]))
print matriz

#print 'final_terms length :',len(final_terms)
#print 'final terms TOTAL: ',final_terms
final_terms = set(terms)
#print 'final_terms length sem duplicadas: ',len(final_terms)



#matriz = pd.DataFrame(final_terms,os.listdir(os.getcwd()))







    #for j in range(len(final_docs[i])):
     #   print 'J: ',j
        #doc_terms = Counter(final_docs[i]).most_common()
      #  print doc_terms[j][0], doc_terms[j][1]
    #print 'doc_terms [j]',doc_terms[j]
    #print 'doc_terms[j][j]: ',doc_terms[j][j]
    #print 'j: ',j
    #print 'doc_terms[j]: ',doc_terms[j][j]
    #for i in range(len(final_docs)):
     #   print final_docs[j][i]
      #  print doc_terms[i][0],doc_terms[i][1]
    # w, h = 20, 59;
    # matrix = [[0 for x in range(w)] for y in range(h)]
    # for i in range(0, 20):
    #   print i
    #  doc_terms = Counter(final_docs[i]).most_common()
#for p in len(doc_term[1]):
    #   p[].
    #       mi.MatrizIncidencia.receive_data(doc_terms[p][0], doc_terms[p][1])
    # print matrix

    #    matriz = [len(doc_terms)][20]
    # print doc_terms[59] #59 eh o tamanho do menor abstract
    #    matriz[i][i]

#for p in range(0,20):
#    foo ='doc'
#    doc final_docs[p]