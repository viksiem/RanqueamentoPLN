import preprocessing as pp


def _absolut_freq(terms_plus_frequencies, term):
    most = []

    for n in range(len(terms_plus_frequencies)):
        for i in range(len(terms_plus_frequencies[n])):
            if term == terms_plus_frequencies[n][i][0]:
                most.append(list((n+1, terms_plus_frequencies[n][i][1])))
            else:
                continue
                #most.append(list((n+1, 0)))

    return most


def _process_new_words(terms):
    foreign_words = pp._read_file(terms)
    foreign_words = pp._seg_into_senteces(foreign_words)
    foreign_words = pp._seg_into_words(foreign_words)
    return foreign_words

