import preprocessing
from collections import Counter

# TODO atributos DF, IDF, TFXIDT


class MatrizIncidencia(object):
    def __init__(self, term,freq):
        self.term = term
        self.freq = freq

    def receive_data(term,freq):

        print term, freq

