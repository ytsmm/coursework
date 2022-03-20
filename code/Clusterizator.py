from sklearn.cluster import AgglomerativeClustering
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
from sklearn import metrics

def Clusterization(X):
    scores = []
    for k in range(2, 20):
        labels = KMeans(n_clusters=k).fit(X).labels_
        score = metrics.silhouette_score(X, labels)
        scores.append(score)

    plt.plot(list(range(2, 20)), scores)
    plt.xlabel("Number of Clusters Initialized")
    plt.ylabel("Sihouette Score")
    plt.show()

    model = AgglomerativeClustering(n_clusters=6, affinity='euclidean', linkage='ward')
    model.fit(X)
    labels = model.labels_
    return labels