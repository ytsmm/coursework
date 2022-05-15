from sklearn.cluster import AgglomerativeClustering
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
from sklearn import metrics

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA
from sklearn.cluster import AgglomerativeClustering
from sklearn.preprocessing import StandardScaler, normalize
from sklearn.metrics import silhouette_score
import scipy.cluster.hierarchy as shc

def Clus(X):
    labels = []
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)

    # Normalizing the data so that the data approximately
    # follows a Gaussian distribution
    X_normalized = normalize(X_scaled)

    # Converting the numpy array into a pandas DataFrame
    X_normalized = pd.DataFrame(X_normalized)
    pca = PCA(n_components=2)
    X_principal = pca.fit_transform(X_normalized)
    X_principal = pd.DataFrame(X_principal)
    X_principal.columns = ['P1', 'P2']
    plt.figure(figsize=(8, 8))
    Dendrogram = shc.dendrogram((shc.linkage(X_principal, method='ward')))

    # ac2 = AgglomerativeClustering(n_clusters=2, affinity='euclidean', linkage='ward')
    # ac3 = AgglomerativeClustering(n_clusters=3, affinity='euclidean', linkage='ward')
    ac4 = AgglomerativeClustering(n_clusters=4, affinity='euclidean', linkage='ward')
    # ac5 = AgglomerativeClustering(n_clusters=5, affinity='euclidean', linkage='ward')
    # ac6 = AgglomerativeClustering(n_clusters=6, affinity='euclidean', linkage='ward')
    # ac7 = AgglomerativeClustering(n_clusters=7, affinity='euclidean', linkage='ward')
    # ac8 = AgglomerativeClustering(n_clusters=8, affinity='euclidean', linkage='ward')
    # ac9 = AgglomerativeClustering(n_clusters=9, affinity='euclidean', linkage='ward')
    # ac10 = AgglomerativeClustering(n_clusters=10, affinity='euclidean', linkage='ward')
    # ac11 = AgglomerativeClustering(n_clusters=11, affinity='euclidean', linkage='ward')
    # ac12 = AgglomerativeClustering(n_clusters=12, affinity='euclidean', linkage='ward')
    # ac13 = AgglomerativeClustering(n_clusters=13, affinity='euclidean', linkage='ward')

    # plt.figure(figsize=(6, 6))
    # plt.scatter(X_principal['P1'], X_principal['P2'],
    #             c=ac2.fit_predict(X_principal), cmap='rainbow')
    # # plt.show()
    #
    # plt.figure(figsize=(6, 6))
    # plt.scatter(X_principal['P1'], X_principal['P2'],
    #             c=ac3.fit_predict(X_principal), cmap='rainbow')
    # # plt.show()

    plt.figure(figsize=(6, 6))
    plt.scatter(X_principal['P1'], X_principal['P2'],
                c=ac4.fit_predict(X_principal), cmap='rainbow')
    # plt.show()

    # plt.figure(figsize=(6, 6))
    # plt.scatter(X_principal['P1'], X_principal['P2'],
    #             c=ac5.fit_predict(X_principal), cmap='rainbow')
    # # plt.show()
    #
    # plt.figure(figsize=(6, 6))
    # plt.scatter(X_principal['P1'], X_principal['P2'],
    #             c=ac6.fit_predict(X_principal), cmap='rainbow')
    # # plt.show()
    #
    # plt.figure(figsize=(6, 6))
    # plt.scatter(X_principal['P1'], X_principal['P2'],
    #             c=ac7.fit_predict(X_principal), cmap='rainbow')
    # # plt.show()
    #
    # plt.figure(figsize=(6, 6))
    # plt.scatter(X_principal['P1'], X_principal['P2'],
    #             c=ac8.fit_predict(X_principal), cmap='rainbow')
    # # plt.show()


    k = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

    # Appending the silhouette scores of the different models to the list
    silhouette_scores = []

    # silhouette_scores.append(
    #     silhouette_score(X_principal, ac2.fit_predict(X_principal)))
    # silhouette_scores.append(
    #     silhouette_score(X_principal, ac3.fit_predict(X_principal)))
    # silhouette_scores.append(
    silhouette_score(X_principal, ac4.fit_predict(X_principal))
    silhouette_scores.append(silhouette_score(X_principal, ac4.fit_predict(X_principal)))
    # silhouette_scores.append(
    #     silhouette_score(X_principal, ac6.fit_predict(X_principal)))
    # silhouette_scores.append(
    #     silhouette_score(X_principal, ac7.fit_predict(X_principal)))
    # silhouette_scores.append(
    #     silhouette_score(X_principal, ac8.fit_predict(X_principal)))
    # silhouette_scores.append(
    #     silhouette_score(X_principal, ac9.fit_predict(X_principal)))
    # silhouette_scores.append(
    #     silhouette_score(X_principal, ac10.fit_predict(X_principal)))
    # silhouette_scores.append(
    #     silhouette_score(X_principal, ac11.fit_predict(X_principal)))
    # silhouette_scores.append(
    #     silhouette_score(X_principal, ac12.fit_predict(X_principal)))
    # silhouette_scores.append(
    #     silhouette_score(X_principal, ac13.fit_predict(X_principal)))
    plt.show()
    return labels

from scipy.cluster.hierarchy import linkage, dendrogram

def ClusterNumber(X):
    labels = []
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)
    X_normalized = normalize(X_scaled)
    X_normalized = pd.DataFrame(X_normalized)
    pca = PCA(n_components=2)
    X_principal = pca.fit_transform(X_normalized)
    X_principal = pd.DataFrame(X_principal)
    X_principal.columns = ['P1', 'P2']
    plt.figure(figsize=(8, 8))
    Dendrogram = shc.dendrogram((shc.linkage(X_principal, method='ward')))
    plt.show()

def Clusterizator(X, number):
    # X - массив векторизованных данных
    model = AgglomerativeClustering(affinity='euclidean', n_clusters=number,linkage='ward')
    model.fit(X)
    labels = model.labels_
    # labels - массив целочисленных данных, содержащий номера кластеров
    return labels

def ClusterNumber(X):
    clusters = [2, 3, 4, 5, 6, 7, 8]
    sc_scores = []
    for n_cluster in clusters:
        model = AgglomerativeClustering(affinity='euclidean', n_clusters=n_cluster, linkage='ward').fit(X)
        label = model.labels_
        sc_score = silhouette_score(X, label, metric='euclidean')
        sc_scores.append(sc_score)
        # km = KMeans(n_clusters=n_cluster).fit(X)
        # model = AgglomerativeClustering(affinity='euclidean', n_clusters=n_cluster, linkage='ward').fit(X)
    return clusters[np.argmax(sc_scores)]