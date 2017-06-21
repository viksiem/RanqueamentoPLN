from random import randint
from pandas import DataFrame, Series

df = DataFrame(columns=('lib', 'qty1', 'qty2'))
for i in range(5):
    df.loc[i] = [randint(-1, 1) for n in range(3)]

data = [[33, 33,33,33],[22,22,22,22],[11,11,11,11],[44,44,44,44]]
dft = DataFrame(data)
#print dft

d = {'one' : Series([1., 2., 3.], index=['a', 'b', 'c']),
    'two' : Series([1., 2., 3., 4.], index=['a', 'b', 'c', 'd'])}
df = DataFrame(d)
print df
print "DF", type(df['one']), "\n", df['one']
dfList = df['one'].tolist()
print "DF list", dfList, type(dfList)