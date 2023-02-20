from collections import OrderedDict


def clusterKeywords(labels, keywords, n):
    clusterKeys = []
    for i in range(n):
        print(i)
        allWords = []
        countWords = {}
        for j in range(len(labels)):
            print(keywords[j])
            if labels[j] == i:
                for k in keywords[j]:
                    allWords.append(k)
        for word in allWords:
            # print(word)
            countWords[word] = allWords.count(word)
        countWords = OrderedDict(sorted(countWords.items(), key=lambda x: -x[1]))
        # print(countWords)
        count = 0
        keys = []
        for word in countWords:
            if count < 10:
                keys.append(word)
                # print(word)
                count += 1
        keys = ', '.join(keys)
        clusterKeys.append(keys)
    return clusterKeys
