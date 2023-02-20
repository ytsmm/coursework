import csv
import numpy as np
import gensim.downloader as api
from nltk.corpus import stopwords
import pandas as pd
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler, normalize
from nltk.stem import WordNetLemmatizer
import Clusterizator
import writerJson
import clusterKeywords
import Morph_Analyzer

# Word embedding corpus
word2vec = api.load("glove-wiki-gigaword-50")
# word2vec = api.load("glove-twitter-200")
# word2vec = api.load("word2vec-google-news-300")
# Getting article data
# print(word2vec.most_similar(positive=["covid"]))

key = []
doi = []
title = []
authors = []
file = 'articleData.csv'
with open(file, encoding='utf-8') as csvfile:
    filereader = csv.reader(csvfile, delimiter=';')
    info = ''
    for row in filereader:
        title.append(row[0])
        authors.append(row[1])
        doi.append(row[2])
        info = row[0] + row[3] + row[4]
        key.append(info)


# Normalizing keywords
keywords = []
stop_words = stopwords.words('english')
for line in key:
    keyLine = []
    keyLine = Morph_Analyzer.Morph_Analyzer(line, word2vec)
    # print(keyLine)
    # print(type(keyLine))
    keyLine = list(set(keyLine))
    #print(sorted(keyLine))
    # keywords.append(sorted(keyLine))
    keywords.append(keyLine)


# Vectoring
def vectorizeApi(list_of_docs, model):
    features = []
    vectorKeywords = []
    for tokens in list_of_docs:
        zero_vector = np.zeros(model.vector_size)
        vectors = []
        # print(tokens)
        for token in tokens:
            if token in model:
                # print(token)
                try:
                    vectors.append(model[token])
                except KeyError:
                    continue
        if vectors:
            vectors = np.asarray(vectors)
            avg_vec = vectors.mean(axis=0)
            features.append(avg_vec)
        else:
            features.append(zero_vector)
    return features


def pcaModule(X):
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)
    X_normalized = normalize(X_scaled)
    X_normalized = pd.DataFrame(X_normalized)
    # print(X_normalized)
    pca = PCA(n_components=2)
    X_principal = pca.fit_transform(X_normalized)
    X_principal = pd.DataFrame(X_principal)
    # print(X_principal)
    X_principal.columns = ['X', 'Y']
    return X_principal


vectorized_docs = vectorizeApi(keywords, model=word2vec)
X = pcaModule(vectorized_docs)
labels, n = Clusterizator.Clusterization(X, title)
clusterKeys = clusterKeywords.clusterKeywords(labels, keywords, n)
writerJson.writerJson(doi, key, title, authors, X, labels, n, clusterKeys)

