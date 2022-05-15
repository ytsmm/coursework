import Tokenizer
import Normalizer
import Lemmatizer

myData = []
myID = []


def Morph_Analyzator(title, abstract):
    line = title + " " + abstract
    # line - строка с данными о статье
    token_line = Tokenizer.Tokenizer(line)
    norm_line = Normalizer.Normalizer(token_line)
    lem_line = Lemmatizer.Lemmatizer(norm_line)
    myData.append(lem_line)
    # myData - массив строковых данных, в котором хранятся токены статей
    return myData
