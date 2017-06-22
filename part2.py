
def absolut_freq(terms_plus_frequencies, term):
    most = []

    for n in range(len(terms_plus_frequencies)):
        #print 'n: ', n

        for i in range(len(terms_plus_frequencies[n])):

            if term == terms_plus_frequencies[n][i][0]:
                most.append(list((n+1, terms_plus_frequencies[n][i][1])))

            else:
                continue
                #most.append(list((n+1, 0)))
       # print most

    return most