import Tokenizer
import Normalizer
import Lemmatizer

myData = []
myID = []


def Morphy(line):
    myID, token_line = Tokenizer.Tokenizer(line)
    norm_line = Normalizer.Normalizer(token_line)
    lem_line = Lemmatizer.Lemmatizer(norm_line)
    myData.append(lem_line)
    return myID, myData
