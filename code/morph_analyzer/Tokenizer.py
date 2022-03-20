import nltk

index = []
def Tokenizer(word_data):
    token_text = nltk.word_tokenize(word_data)
    index.append(token_text.pop(0))
    return index, token_text