from itertools import repeat


def absolut_freq(list_of_docs, term):
    most = []
    for n in range(len(list_of_docs)):
        for i in range(len(list_of_docs[n])):
            if term == list_of_docs[n][i][0]:
                most.append(list_of_docs[n][i][1])
                #print most
            else:
                continue

    return most