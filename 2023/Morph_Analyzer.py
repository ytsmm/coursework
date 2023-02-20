import nltk
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer


"""
Функция запускает процесс морфологической обработки
@:param type: {str} title - строка с названием статьи, {str} abstract - строка с аннотацией статьи
@:return type: {str} lem_line - строка, прошедшая морфологическую обработку
"""
def Morph_Analyzer(data, corpus):
    token_line = Tokenizer(data)
    # print(token_line)
    norm_line = Normalizer(token_line, corpus)
    # print(norm_line)
    return norm_line

"""
Функция разбивает строку на отдельные слова
@:param type: {str}, line - строка с названием и аннотацией статьи
@:return type: list{str}, token_line - строковый массив токенов
"""
def Tokenizer(line):
    token_line = nltk.word_tokenize(line)
    return token_line


lemmatizer = WordNetLemmatizer()
stop_words = stopwords.words('english')
"""
Функция исключает шумовые слова и знаки препинания
@:param type: list{str}, line - строковый массив токенов
@:return type: list{str}, norm_line - строковый массив, прошедший нормализацию
"""
def Normalizer(line, corpus):
    norm_line = []
    for word in line:
        word = word.lower()
        word = lemmatizer.lemmatize(word).lower()
        if word not in stop_words and len(word) > 1:
            if word in corpus:
                norm_line.append(word)
            # else:
            #     for w in word:
            #         if 32 <= ord(w) <= 44 or 58 <= ord(w) <= 64 or 123 <= ord(w) <= 126:
            #             word = word.replace(w, '')
            #             if word in corpus:
            #                 norm_line.append(word)
            #         if ord(w) == 45:
            #             print(word)
            #             if word not in corpus:
            #                 word = word.replace(w, ' ')
            #                 word = Tokenizer(word)
            #                 for term in word:
            #                     if term in corpus and not term.isdigit():
            #                         norm_line.append(term)
    return norm_line


lemmatizer = WordNetLemmatizer()
"""
Функция приводит слова к инфинитивной форме
@:param type: list{str}, line - строковый массив слов
@:return type: list{str}, lem_line - строковый массив инфинитивов
"""
def Lemmatizer(line):
    word = lemmatizer.lemmatize(line)
    return word

