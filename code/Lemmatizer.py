from nltk.stem import WordNetLemmatizer
lemmatizer = WordNetLemmatizer()


def Lemmatizer(word_data):
    # word_data - строка с данными о статье
    if bool(word_data):
        lem_line = []
        for word in word_data:
            lem_line.append(lemmatizer.lemmatize(word))
    # lem_line - массив строковых данных, содержащий лемматизированные слова статей
    return lem_line
