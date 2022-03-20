from sklearn.feature_extraction.text import TfidfVectorizer


def Vectorizing(text):
    tfidf_vector = TfidfVectorizer()
    tfidf = tfidf_vector.fit_transform(text)
    print(tfidf_vector.vocabulary_)
    fn = tfidf_vector.get_feature_names()
    print(len(fn))
    for col in tfidf.nonzero()[1]:
        print(fn[col], " ", tfidf[0, col])
    return tfidf
