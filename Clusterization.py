from sklearn.cluster import KMeans

def Clusterizator(text):
    num_clusters = 5

    # Метод к-средних - KMeans
    from sklearn.cluster import KMeans
    km = KMeans(n_clusters=num_clusters)
    km.fit(text)
    clusters = km.labels_.tolist()
    return clusters

from scipy.cluster.hierarchy import linkage, dendrogram
import matplotlib.pyplot as plt
import pandas as pd


def clus(text):
    linked = linkage(text, 'single')

    labelList = range(1, 11)

    plt.figure(figsize=(10, 7))
    dendrogram(linked,
               orientation='top',
               labels=labelList,
               distance_sort='descending',
               show_leaf_counts=True)
    plt.show()


from sklearn.cluster import AgglomerativeClustering
import scipy.cluster.hierarchy as sch

def cl(X):
    model = AgglomerativeClustering(n_clusters=5, affinity='euclidean', linkage='ward')
    model.fit(X)
    labels = model.labels_
    return labels

