from nltk.corpus import stopwords

html = ["--", "/p", "em", "/em", "'s", "br", "''", "/span", "/div", "span", "``", "div", "p", "/sub", "sub",
        "n/a", "font-size", "layoutarea", "page", "column", "in", "a", "situ", "in-situ"]
stop_words = stopwords.words('english')
for el in html:
    stop_words.append(el)

def Normalizer(word_data):
    # word_data - строка с данными о статье
    norm_line = []
    for word in word_data:
        if len(word) == 1:
            if not (33 <= ord(word) <= 64) and not (91 <= ord(word) <= 96) and not (123 <= ord(word) <= 126):
                norm_line.append(word.lower())
        else:
            if word.lower() not in stop_words and not any(map(str.isdigit, word)) and word.lower() not in html:
                if word.find('=') != -1 or word.find('//') != -1 or word.find('.') != -1:
                    continue
                #if word.find('.') != -1:
                    #word = word.replace('.', ' ')
                norm_line.append(word.lower())
                #print(word)
    # norm_line - массив строковых данных, содержащий только слова
    return norm_line
