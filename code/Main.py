import Morph_Analyzer
import Vectorizer
import Clusterizator
import codecs
import pandas as pd

datafile = "articles.csv"
file = codecs.open(datafile, "r", "cp1251")

for line in file:
    line = line.rstrip('\n')
    myDoi, myData = Morph_Analyzer.Morphy(line)

for i in range(len(myData)):
    if myData[i] is None:
        myData[i] = ''
    else:
        myData[i] = ' '.join(myData[i])

myVect = Vectorizer.Vectorizing(myData)
myClus = Clusterizator.Clusterization(myVect.toarray())


Res = pd.Series(myClus, index=myDoi)
Res = pd.DataFrame({'doi': myDoi, 'cluster': myClus})
Res.to_csv("base.csv", sep=";", index=False)
file.close()


