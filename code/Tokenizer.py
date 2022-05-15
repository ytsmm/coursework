import nltk

def Tokenizer(word_data):
    token_text = nltk.word_tokenize(word_data)
    # token_text - массив строковых данных, в котором хранятся токены статьи
    return token_text