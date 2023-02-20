import numpy as np
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
from sklearn.cluster import AgglomerativeClustering
from sklearn.metrics import silhouette_score
import scipy.cluster.hierarchy as shc
import writerJson
import clusterKeywords


def Clusterization(X, doi):
    clusAgg = []
    clusManh = []
    clusKmeans = []
    k = []
    for i in range(2, 11):
        Agg = AgglomerativeClustering(n_clusters=i)
        Manh = AgglomerativeClustering(n_clusters=i, affinity='manhattan', linkage='complete')
        Kmeans = KMeans(n_clusters=i)
        clusAgg.append(Agg)
        clusManh.append(Manh)
        clusKmeans.append(Kmeans)
        k.append(i)

    ssAgg = []
    ssManh = []
    ssKmeans = []
    for i in range(9):
        ssAgg.append(silhouette_score(X, clusAgg[i].fit_predict(X)))
        ssManh.append(silhouette_score(X, clusManh[i].fit_predict(X)))
        ssKmeans.append(silhouette_score(X, clusKmeans[i].fit_predict(X)))
    print(ssAgg)
    print(ssManh)
    print(ssKmeans)

    plt.bar(k, ssAgg)
    plt.xlabel('Agg', fontsize=20)
    plt.ylabel('S(i)', fontsize=20)
    plt.show()

    plt.bar(k, ssManh)
    plt.xlabel('Manh', fontsize=20)
    plt.ylabel('S(i)', fontsize=20)
    plt.show()

    plt.bar(k, ssKmeans)
    plt.xlabel('Kmeans', fontsize=20)
    plt.ylabel('S(i)', fontsize=20)
    plt.show()

    nAgg = k[np.argmax(ssAgg)]
    model = AgglomerativeClustering(affinity='euclidean', n_clusters=nAgg, linkage='ward').fit(X)
    # plt.figure(figsize=(8, 8))
    Dendrogram = shc.dendrogram((shc.linkage(X, method='ward')), labels=doi, orientation='left', leaf_font_size=8)
    # plt.show()
    plt.figure(figsize=(6, 6))
    plt.scatter(X['X'], X['Y'], c=clusAgg[nAgg - 2].fit_predict(X), cmap='rainbow')
    plt.xlabel('Agg', fontsize=20)
    plt.ylabel(nAgg, fontsize=15)
    plt.show()
    labels = model.labels_
    print(model.labels_)

    nManh = k[np.argmax(ssManh)]
    model = AgglomerativeClustering(affinity='manhattan', n_clusters=nManh, linkage='complete').fit(X)
    plt.figure(figsize=(6, 6))
    plt.scatter(X['X'], X['Y'], c=clusAgg[nManh - 2].fit_predict(X), cmap='rainbow')
    plt.xlabel('Manh', fontsize=20)
    plt.ylabel(nManh, fontsize=15)
    plt.show()
    print(model.labels_)

    nKmeans = k[np.argmax(ssKmeans)]
    model = KMeans(n_clusters=nKmeans).fit(X)
    plt.figure(figsize=(6, 6))
    plt.scatter(X['X'], X['Y'], c=clusAgg[nKmeans - 2].fit_predict(X), cmap='rainbow')
    plt.xlabel('Kmeans', fontsize=20)
    plt.ylabel(nKmeans, fontsize=15)
    plt.show()
    print(model.labels_)

    return labels, nAgg
