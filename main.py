import Morph_Analyzer
import Vectorizer
import Clusterization
#import Vizualizator
import codecs
import pandas as pd

datafile = "database.csv"
file = codecs.open(datafile, "r", "utf-8")

for line in file:
    line = line.rstrip('\n')
    myID, myData = Morph_Analyzer.Morphy(line)


for i in range(len(myData)):
    if myData[i] is None:
        myData[i] = ''
    else:
        myData[i] = ' '.join(myData[i])


myVect = Vectorizer.Vectorizing(myData)
myClus = Clusterization.cl(myVect.toarray())

Res = pd.DataFrame({'ID': myID, 'Cluster': myClus})
Res.to_csv("base.csv", sep=";", index=False)
file.close()
