import Morph_Analyzer
import Vectorizer
import Clusterizator
import Clusterization
import KeywordsGenerator
import codecs
import pandas as pd
import numpy as np
import csv

datafile = "allarticlesdata.csv"
doi = []; title = []; authors = []; year = []; number = []; i = 0;
with open(datafile, encoding='utf-8') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=';')
    for row in spamreader:
        if i == 0:
            i += 1
            continue
        doi.append(row[0])
        authors.append(row[1])
        year.append(row[2])
        number.append(row[3])
        title.append((row[4]))
        myData = Morph_Analyzer.Morph_Analyzator(row[4], row[5])
#file = codecs.open(datafile, "r", encoding='utf-8')
# f = pd.read_csv(datafile, encoding='cp1251')
# print(f)

for i in range(len(myData)):
    if myData[i] is None:
        myData[i] = ''
    else:
        myData[i] = ' '.join(myData[i])

myVect, fn = Vectorizer.Vectorizing(myData)
clusNumber = Clusterizator.ClusterNumber(myVect.toarray())
myClus = Clusterizator.Clusterizator(myVect.toarray(), clusNumber)
keyWords = KeywordsGenerator.KeysGenerator(myVect.toarray(), myClus, fn, clusNumber)
# Запись в файл
# Res = pd.Series(myClus, myDoi)
Res = pd.DataFrame({'authors': authors, 'year': year, 'title': title, 'number': number, 'doi': doi, 'cluster': myClus})
Res.to_json("base.json")
Res = pd.DataFrame({'keywords': keyWords})
Res.to_json("keywords.json")
csvfile.close()
