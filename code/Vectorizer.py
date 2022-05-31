from sklearn.feature_extraction.text import TfidfVectorizer
"""
Функция преобразует слова к числовому типу с помощью метода tfidf
@:param type: list text - двумерный массив текстов статей, прошедших морфологическую обработку
@:return type: {csr_matrix} tfidf - разреженная матрица весов слов; type: list{str}, allWords - строковый массив терминов
"""
def Vectorizing(text):
    vectorizer = TfidfVectorizer()
    tfidf = vectorizer.fit_transform(text)
    allWords = vectorizer.get_feature_names()
    return tfidf, allWords
