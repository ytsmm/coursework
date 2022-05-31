import nltk
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer


"""
Функция запускает процесс морфологической обработки
@:param type: {str} title - строка с названием статьи, {str} abstract - строка с аннотацией статьи
@:return type: {str} lem_line - строка, прошедшая морфологическую обработку
"""
def Morph_Analyzer(title, abstract):
    line = title + " " + abstract
    token_line = Tokenizer(line)
    norm_line = Normalizer(token_line)
    lem_line = Lemmatizer(norm_line)
    return lem_line

"""
Функция разбивает строку на отдельные слова
@:param type: {str}, line - строка с названием и аннотацией статьи
@:return type: list{str}, token_line - строковый массив токенов
"""
def Tokenizer(line):
    token_line = nltk.word_tokenize(line)
    return token_line


html = ["--", "/p", "em", "/em", "'s", "br", "''", "/span", "/div", "span", "``", "div", "p", "/sub", "sub",
        "n/a", "font-size", "layoutarea", "page", "column", "in", "a", "situ", "in-situ"]
stop_words = stopwords.words('english')
for el in html:
    stop_words.append(el)

"""
Функция исключает шумовые слова и знаки препинания
@:param type: list{str}, line - строковый массив токенов
@:return type: list{str}, norm_line - строковый массив, прошедший нормализацию
"""
def Normalizer(line):
    norm_line = []
    for word in line:
        if len(word) == 1:
            continue
        else:
            if word.lower() not in stop_words and not any(map(str.isdigit, word)) and word.lower() not in html:
                if word.find('=') != -1 or word.find('//') != -1 or word.find('.') != -1:
                    continue
                norm_line.append(word.lower())
    return norm_line


lemmatizer = WordNetLemmatizer()
"""
Функция приводит слова к инфинитивной форме
@:param type: list{str}, line - строковый массив слов
@:return type: list{str}, lem_line - строковый массив инфинитивов
"""
def Lemmatizer(line):
    lem_line = []
    for word in line:
        lem_line.append(lemmatizer.lemmatize(word))
    return lem_line
