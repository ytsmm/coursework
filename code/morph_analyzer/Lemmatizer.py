from nltk.stem import WordNetLemmatizer

lemmatizer = WordNetLemmatizer()

def Lemmatizer(line):
    if bool(line):
        lem_line = []
        for word in line:
            lem_line.append(lemmatizer.lemmatize(word))
        return lem_line
