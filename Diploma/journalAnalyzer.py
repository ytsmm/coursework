import os
import csv
import downloading
import morphAnalyzer
import vectorizer
import clusterizator
import clusterKeywords
import writerJson
import pandas as pd


def Analyzer():
    file = "articleData.csv"
    if not os.path.exists(file):
        print('Parsing')
        downloading.parser()

    data = pd.read_csv('articleData.csv', sep=';')
    title = data['Title'].to_numpy()
    authors = data['Authors'].to_numpy()
    doi = data['Doi'].to_numpy()
    keys = data['Keywords'].to_numpy()
    words = data[['Title', 'Keywords', 'Abstract']].agg(''.join, axis=1).to_numpy()

    vocabulary = {}
    for i in range(len(keys)):
        words[i].split(', ')
        for word in keys[i].split(', '):
            vocabulary[word.lower()] = word
        keys[i] = keys[i].lower().split(', ')

    keywords, model = morphAnalyzer.preprocessor(words)

    vectors = vectorizer.vectorizeApi(keywords, model)
    labels, n, size = clusterizator.clusterization(vectors)
    # clusterKeys = clusterKeywords.mainKeys(key, labels, n, vocabulary)
    clusterKeys = clusterKeywords.main(vocabulary, keys, labels, n)
    writerJson.writerJson(doi, keys, title, authors, vectors, labels, n, clusterKeys, size)


Analyzer()
