import numpy as np
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
from sklearn.cluster import AgglomerativeClustering
from sklearn.metrics import silhouette_score
import scipy.cluster.hierarchy as shc


def clusterization(X):
    clusAgg = []
    clusManh = []
    clusKmeans = []
    k = []
    for i in range(2, 10):
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
    for i in range(8):
        ssAgg.append(silhouette_score(X, clusAgg[i].fit_predict(X)))
        ssManh.append(silhouette_score(X, clusManh[i].fit_predict(X)))
        ssKmeans.append(silhouette_score(X, clusKmeans[i].fit_predict(X)))
    print(ssAgg)
    print(ssManh)
    print(ssKmeans)

    plt.bar(k, ssAgg)
    plt.xlabel('Number of clusters', fontsize=16)
    plt.ylabel('S(i)', fontsize=16)
    plt.show()

    plt.bar(k, ssManh)
    plt.xlabel('Number of clusters', fontsize=16)
    plt.ylabel('S(i)', fontsize=16)
    plt.show()

    plt.bar(k, ssKmeans)
    plt.xlabel('Number of clusters', fontsize=16)
    plt.ylabel('S(i)', fontsize=16)
    plt.show()

    nAgg = k[np.argmax(ssAgg)]
    model = AgglomerativeClustering(affinity='euclidean', n_clusters=nAgg, linkage='ward').fit(X)
    plt.figure(figsize=(6, 6))
    # Dendrogram = shc.dendrogram((shc.linkage(X, method='ward')), labels=doi, orientation='left', leaf_font_size=4)
    Dendrogram = shc.dendrogram((shc.linkage(X, method='ward')), leaf_font_size=4)
    plt.show()
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
    plt.scatter(X['X'], X['Y'], c=clusManh[nManh - 2].fit_predict(X), cmap='rainbow')
    plt.xlabel('Manh', fontsize=20)
    plt.ylabel(nManh, fontsize=15)
    plt.show()
    print(model.labels_)

    nKmeans = k[np.argmax(ssKmeans)]
    model = KMeans(n_clusters=nKmeans).fit(X)
    plt.figure(figsize=(6, 6))
    plt.scatter(X['X'], X['Y'], c=clusKmeans[nKmeans - 2].fit_predict(X), cmap='rainbow')
    plt.xlabel('Kmeans', fontsize=20)
    plt.ylabel(nKmeans, fontsize=15)
    plt.show()
    print(model.labels_)

    number = []
    for i in range(nAgg):
        count = 0
        for j in labels:
            if j == i:
                count += 1
        number.append(count)

    return labels, nAgg, number
