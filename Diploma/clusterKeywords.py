import math
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer


def tfidf(vocab, keywords, labels, n):
    texts = []
    for i in range(n):
        text = ''
        for j in range(len(labels)):
            if labels[j] == i:
                text = " ".join([text, keywords[j]])
        texts.append(text)
    vectorizer = TfidfVectorizer()
    vectors = vectorizer.fit_transform(texts)
    feature_names = vectorizer.get_feature_names()
    dense = vectors.todense()
    denselist = dense.tolist()
    # for i in range(len(denselist)):
    #     for j in range(len(denselist[i])):
    #         if denselist[i][j] != 0:
    #             denselist[i][j] = 1/denselist[i][j]

    df = pd.DataFrame(denselist, columns=feature_names)
    print(df)

    maxes = []
    for i in denselist:
        words = feature_names.copy()
        line = i
        # maxI = []
        maxTerms = []
        while len(maxTerms) < 10:
            # iTerms = {feature_names[line.index(max(line)) + j]: max(line)}
            maxValue = max(line)
            print(maxValue)
            term = words[line.index(maxValue)]
            print(term)
            maxTerms.append(vocab[term])
            line.remove(maxValue)
            words.remove(term)
            # maxI.append(iTerms)
        maxes.append(maxTerms)
    return maxes


def mainKeys(keywords, labels, n, vocabulary):
    texts = []
    for i in range(n):
        text = []
        for j in range(len(labels)):
            if labels[j] == i:
                text.extend(keywords[j])
        texts.append(text)
    result = []
    terms = []
    for text in texts:
        for word in text:
            if word not in terms:
                terms.append(word)
    for text in texts:
        textRes = []
        for t in terms:
            textRes.append(func(t, text, texts))
        result.append(textRes)
    df = pd.DataFrame(result, columns=terms)
    print(df.to_string())

    maxes = []
    for i in result:
        words = terms.copy()
        line = i
        maxTerms = []
        while len(maxTerms) < 10:
            maxValue = max(line)
            term = words[line.index(maxValue)]
            maxTerms.append(term)
            line.remove(maxValue)
            words.remove(term)
        maxes.append(maxTerms)

    while True:
        words = []
        for m in maxes:
            for word in m:
                words.append(word)  # все ключевые слова
        dup = [x for i, x in enumerate(words) if i != words.index(x)]
        dup = set(dup)
        print(dup)
        y = 0
        for d in dup:
            y = 1
            for k in range(len(result)):
                ind = terms.index(d)
                result[k].pop(ind)
            terms.remove(d)
        if y == 1:
            maxes = []
            for i in result:
                words = terms.copy()
                line = i
                maxTerms = []
                while len(maxTerms) < 10:
                    maxValue = max(line)
                    print(maxValue)
                    term = words[line.index(maxValue)]
                    maxTerms.append(term)
                    line.remove(maxValue)
                    words.remove(term)
                maxes.append(maxTerms)
        else:
            break
    return maxes


def main(vocabulary, keywords, labels, n):
    texts = []
    for i in range(n):
        text = []
        for j in range(len(labels)):
            if labels[j] == i:
                text.extend(keywords[j])
        texts.append(text)
    result = []
    terms = []
    for text in texts:
        for word in text:
            if word not in terms:
                terms.append(word)
    for text in texts:
        textRes = []
        for t in terms:
            textRes.append(func(t, text, texts))
        result.append(textRes)
    df = pd.DataFrame(result, columns=terms)
    print(df.to_string())

    maxes = []
    for i in result:
        t = terms.copy()
        line = i.copy()
        maxes.append(top(t, line, vocabulary))

    while True:
        words = []
        for m in maxes:
            for word in m:
                words.append(word)  # все ключевые слова
        dup = [x for i, x in enumerate(words) if i != words.index(x)]
        dup = list(set(dup))
        y = 0
        for d in dup:
            y = 1
            ind = terms.index(d.lower())
            for k in range(len(result)):
                result[k].pop(ind)
            terms.remove(d.lower())
        if y == 1:
            maxes = []
            for i in result:
                line = i.copy()
                w = terms.copy()
                maxes.append(top(w, line, vocabulary))
        else:
            break
    return maxes


def top(words, line, vocabulary):
    maxTerms = []
    while len(maxTerms) < 10:
        maxValue = max(line)
        term = words[line.index(maxValue)]
        # if vocabulary[term] not in maxTerms:
            # print(term, vocabulary[term])
        if term not in maxTerms:
            # maxTerms.append(vocabulary[term])
            maxTerms.append(vocabulary[term])
        line.remove(maxValue)
        words.remove(term)
    return maxTerms


def func(word, sentence, docs):
    # Получаем число слов вхождений слов / на длину документа, а именно TF
    tf = sentence.count(word) / len(sentence)
    # Получаем IDF
    idf = math.log1p(len(docs) / sum([1 for doc in docs if word in doc]))
    # return round(tf * idf, 4)
    # print(word, 'tf:', tf, 'idf:', idf, 'tfidf:', tf*idf)
    return tf * idf

# def clusterKeywords(labels, keywords, n):
#     clusterKeys = []
#     for i in range(n):
#         # print(i)
#         allWords = []
#         countWords = {}
#         for j in range(len(labels)):
#             # print(keywords[j])
#             if labels[j] == i:
#                 for k in keywords[j]:
#                     allWords.append(k)
#         for word in allWords:
#             # print(word)
#             countWords[word] = allWords.count(word)
#         countWords = OrderedDict(sorted(countWords.items(), key=lambda x: -x[1]))
#         # print(countWords)
#         count = 0
#         keys = []
#         for word in countWords:
#             if count < 10:
#                 keys.append(word)
#                 # print(word)
#                 count += 1
#         keys = ', '.join(keys)
#         clusterKeys.append(keys)
#     return clusterKeys
