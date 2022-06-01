import Morph_Analyzer
import Vectorizer
import Clusterizator
import KeywordsGenerator
import pandas as pd
import csv

"""
Функция запускает запускает процесс обработки данных из файла и запись результатов в файл
"""
def Analyzer():
    datafile = "articles.csv"
    doi = []
    title = []
    authors = []
    year = []
    number = []
    myData = []
    count = 0
    try:
        with open(datafile, encoding='utf-8') as csvfile:
            filereader = csv.reader(csvfile, delimiter=';')
            for row in filereader:
                if row[0] == '':
                    doi.append('NULL')
                else:
                    doi.append(row[0])
                if row[1] == '':
                    authors.append('NULL')
                else:
                    authors.append(row[1])
                if row[2] == '':
                    year.append('NULL')
                else:
                    year.append(row[2])
                if row[3] == '':
                    number.append('NULL')
                else:
                    number.append(row[3])
                title.append((row[4]))
                myData.append(Morph_Analyzer.Morph_Analyzer(row[4], row[5]))
                count += 1
    except FileNotFoundError:
        print("File doesn't exist")
        return

    for i in range(len(myData)):
        myData[i] = ' '.join(myData[i])
    # Векторизация данных
    try:
        myVect, listOfWords = Vectorizer.Vectorizing(myData)
    except:
        print("Check your file for the correct filling")
        return
    # Определение числа кластеров
    clusNumber = Clusterizator.ClusterNumber(myVect, count)
    # Кластеризация данных
    myClus = Clusterizator.Clusterizator(myVect, clusNumber)
    # Нахождения ключевых слов для кластера
    keyWords = KeywordsGenerator.KeysGenerator(myVect, myClus, listOfWords, clusNumber)
    csvfile.close()
    # Запись в файл
    Res = pd.DataFrame(
        {'authors': authors, 'year': year, 'title': title, 'number': number, 'doi': doi, 'cluster': myClus})
    Res.to_json("base.json")
    Res = pd.DataFrame({'keywords': keyWords})
    Res.to_json("keywords.json")
    print("The data is clustered successfully")