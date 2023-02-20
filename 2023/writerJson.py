import json


def writerJson(doi, key, title, authors, X, labels, n, clusterKeywords):
    data = {'articles': [], 'clusters': []}
    for i in range(len(doi)):
        data['articles'].append({
            'doi': doi[i],
            'title': title[i],
            'authors': authors[i],
            'keywords': key[i],
            'axisX': str(X['X'].values[i]),
            'axisY': str(X['Y'].values[i]),
            'class': str(labels[i])
        })
    for i in range(n):
        data['clusters'].append({
            'number': i,
            'keywords': clusterKeywords[i]
        })
    data['clusterQuantity'] = n

    with open('data.json', 'w') as outfile:
        json.dump(data, outfile, indent=2)
        outfile.write('\n')

    return 1
