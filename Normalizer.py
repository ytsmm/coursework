from nltk.corpus import stopwords

punctuation = ['(', ')', '?', ':', ';', ',', '.', '!', '/', '"', "'", "-", "--", "''", "``", "&", "“", "вђ", "$"]
stop_words = set(stopwords.words('english'))


def Normalizer(line):
    norm_line = []
    for word in line:
        try:
            int(word)
        except ValueError:
            if word not in punctuation and word.lower() not in stop_words and word != "N/A" and word != "в" and word != "вђ":
                norm_line.append(word.lower())
    return norm_line
