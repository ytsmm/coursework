from nltk.corpus import stopwords

punctuation = ['(', ')', '?', ':', ';', ',', '.', '!', '/', '"', "'", "-", "--", "''", "``", "&", "“", "вђ", "$", "+", "%", "x", "'s"]
stop_words = set(stopwords.words('english'))


def Normalizer(line):
    norm_line = []
    for word in line:
        if word not in punctuation and word.lower() not in stop_words and not any(map(str.isdigit, word)):
            norm_line.append(word.lower())
    return norm_line
