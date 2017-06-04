import nltk
from nltk.corpus import stopwords

# TODO adicionar palavras como
def read_file():
    file = open('resultadospubmed.txt', 'r')
    data = file.read()
    print data

stopwords_list = stopwords.words('portuguese')
print (stopwords_list)




