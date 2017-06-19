
def absolut_freq(list_of_tuples, term):
    return next(i for i in range(len(list_of_tuples)) for x in list_of_tuples[i] if term in x)