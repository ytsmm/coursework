from sklearn.cluster import AgglomerativeClustering
from sklearn.metrics import silhouette_score
import numpy as np
"""
Функция вычисляет оптимальное число кластеров
@:param type: list, X - вещественный массив весов слов
@:return type: int, clusNumber - целочисленный параметр, равный числу класте-ров
"""
def ClusterNumber(X, count):
    clusters = []
    if count < 9:
        for i in range(2, count):
            clusters.append(i)
    for i in range(2, 11):
        clusters.append(i)
    sc_scores = []
    for n_cluster in clusters:
        model = AgglomerativeClustering(affinity='euclidean', n_clusters=n_cluster, linkage='ward').fit(X)
        label = model.labels_
        sc_score = silhouette_score(X, label, metric='euclidean')
        sc_scores.append(sc_score)
    clusNumber = clusters[np.argmax(sc_scores)]
    return clusNumber


"""
Функция выполняет иерархическую кластеризацию данных
@:param type: list, X - вещественный массив весов слов
@:param type: int, number - число кластеров
@:return type: list, labels - целочисленный массив номеров кластеров
"""
def Clusterizator(X, number):
    model = AgglomerativeClustering(affinity='euclidean', n_clusters=number, linkage='ward')
    model.fit(X)
    labels = model.labels_
    return labels