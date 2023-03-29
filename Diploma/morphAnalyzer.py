from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from nltk.tokenize import word_tokenize
import gensim.downloader as api
import string
import csv
import nltk
import re

corpus = api.load("glove-wiki-gigaword-50")
"""
Функция запускает процесс морфологической обработки
@:param type: {str} title - строка с названием статьи, {str} abstract - строка с аннотацией статьи
@:return type: {str} lem_line - строка, прошедшая морфологическую обработку
"""


def preprocessor(keywords):
    optData = []
    for line in keywords:
        # line = normalizer(line)
        # optData.append(' '.join(line))
        optData.append(normalizer(line))
    # data = []
    # for i in range(len(title)):
    #     dataLine = [title[i], authors[i], doi[i], optData[i]]
    #     data.append(dataLine)
    # csvWriter(data, file)
    for i in range(len(optData)):
        optData[i] = list(set(optData[i]))
    return optData, corpus


def preprocessorKeys(keywords):
    vocabulary = {}
    optData = []
    for line in keywords:
        line, vocab = normalizerKeys(line)
        optData.append(line)
        vocabulary.update(vocab)
    return optData, vocabulary


def csvWriter(data, file):
    with open(file, 'w', encoding="utf-8", newline='') as file:
        writer = csv.writer(file, delimiter=";")
        writer.writerows(data)

punctuation = string.punctuation
stop_words = stopwords.words('english')
stop_words.extend(punctuation)
stop_words.extend(
    ["'s", "’s", 'although', "a's", "able", "about", "above", "according", "accordingly", "across", "actually", "after",
     "afterwards", "again", "against", "ain't", "all", "allow", "allows", "almost", "alone", "along", "already", "also",
     "although", "always", "am", "among", "amongst", "an", "and", "another", "any", "anybody", "anyhow", "anyone",
     "anything", "anyway", "anyways", "anywhere", "apart", "appear", "appreciate", "appropriate", "are", "aren't",
     "around", "as", "aside", "ask", "asking", "associated", "at", "available", "away", "awfully", "be", "became",
     "because", "become", "becomes", "becoming", "been", "before", "beforehand", "behind", "being", "believe", "below",
     "beside", "besides", "best", "better", "between", "beyond", "both", "brief", "but", "by", "c'mon", "c's", "came",
     "can", "can't", "cannot", "cant", "cause", "causes", "certain", "certainly", "changes", "clearly", "co", "com",
     "come", "comes", "concerning", "consequently", "consider", "considering", "contain", "containing", "contains",
     "corresponding", "could", "couldn't", "course", "currently", "definitely", "described", "despite", "did", "didn't",
     "different", "do", "does", "doesn't", "doing", "don't", "done", "down", "downwards", "during", "each", "edu", "eg",
     "eight", "either", "else", "elsewhere", "enough", "entirely", "especially", "et", "etc", "even", "ever", "every",
     "everybody", "everyone", "everything", "everywhere", "ex", "exactly", "example", "except", "far", "few", "fifth",
     "first", "five", "followed", "following", "follows", "for", "former", "formerly", "forth", "four", "from",
     "further", "furthermore", "get", "gets", "getting", "given", "gives", "go", "goes", "going", "gone", "got",
     "gotten", "greetings", "had", "hadn't", "happens", "hardly", "has", "hasn't", "have", "haven't", "having", "he",
     "he's", "hello", "help", "hence", "her", "here", "here's", "hereafter", "hereby", "herein", "hereupon", "hers",
     "herself", "hi", "him", "himself", "his", "hither", "hopefully", "how", "howbeit", "however", "i'd", "i'll", "i'm",
     "i've", "ie", "if", "ignored", "immediate", "in", "inasmuch", "inc", "indeed", "indicate", "indicated",
     "indicates", "inner", "insofar", "instead", "into", "inward", "is", "isn't", "it", "it'd", "it'll", "it's", "its",
     "itself", "just", "keep", "keeps", "kept", "know", "known", "knows", "last", "lately", "later", "latter",
     "latterly", "least", "less", "lest", "let", "let's", "like", "liked", "likely", "little", "look", "looking",
     "looks", "ltd", "mainly", "many", "may", "maybe", "me", "mean", "meanwhile", "merely", "might", "more", "moreover",
     "most", "mostly", "much", "must", "my", "myself", "name", "namely", "nd", "near", "nearly", "necessary", "need",
     "needs", "neither", "never", "nevertheless", "new", "next", "nine", "no", "nobody", "non", "none", "noone", "nor",
     "normally", "not", "nothing", "novel", "now", "nowhere", "obviously", "of", "off", "often", "oh", "ok", "okay",
     "old", "on", "once", "one", "ones", "only", "onto", "or", "other", "others", "otherwise", "ought", "our", "ours",
     "ourselves", "out", "outside", "over", "overall", "own", "particular", "particularly", "per", "perhaps", "placed",
     "please", "plus", "possible", "presumably", "probably", "provides", "que", "quite", "qv", "rather", "rd", "re",
     "really", "reasonably", "regarding", "regardless", "regards", "relatively", "respectively", "right", "said",
     "same", "saw", "say", "saying", "says", "second", "secondly", "see", "seeing", "seem", "seemed", "seeming",
     "seems", "seen", "self", "selves", "sensible", "sent", "serious", "seriously", "seven", "several", "shall", "she",
     "should", "shouldn't", "since", "six", "so", "some", "somebody", "somehow", "someone", "something", "sometime",
     "sometimes", "somewhat", "somewhere", "soon", "sorry", "specified", "specify", "specifying", "still", "sub",
     "such", "sup", "sure", "t's", "take", "taken", "tell", "tends", "th", "than", "thank", "thanks", "thanx", "that",
     "that's", "thats", "the", "their", "theirs", "them", "themselves", "then", "thence", "there", "there's",
     "thereafter", "thereby", "therefore", "therein", "theres", "thereupon", "these", "they", "they'd", "they'll",
     "they're", "they've", "think", "third", "this", "thorough", "thoroughly", "those", "though", "three", "through",
     "throughout", "thru", "thus", "to", "together", "too", "took", "toward", "towards", "tried", "tries", "truly",
     "try", "trying", "twice", "two", "un", "under", "unfortunately", "unless", "unlikely", "until", "unto", "up",
     "upon", "us", "use", "used", "useful", "uses", "using", "usually", "value", "various", "very", "via", "viz", "vs",
     "want", "wants", "was", "wasn't", "way", "we", "we'd", "we'll", "we're", "we've", "welcome", "well", "went",
     "were", "weren't", "what", "what's", "whatever", "when", "whence", "whenever", "where", "where's", "whereafter",
     "whereas", "whereby", "wherein", "whereupon", "wherever", "whether", "which", "while", "whither", "who", "who's",
     "whoever", "whole", "whom", "whose", "why", "will", "willing", "wish", "with", "within", "without", "won't",
     "wonder", "would", "wouldn't", "yes", "yet", "you", "you'd", "you'll", "you're", "you've", "your", "yours",
     "yourself", "yourselves", "zero", "``", "--", "e.g", "and/or", "lu", "lo"])

lemmatizer = WordNetLemmatizer()
"""
Функция исключает шумовые слова и знаки препинания
@:param type: list{str}, line - строковый массив токенов
@:return type: list{str}, norm_line - строковый массив, прошедший нормализацию
"""


# def normalizerKeys(line):
    # line = line.lower()
    # nlp = spacy.load('en_core_web_sm')
    # doc = nlp(line)
    # line = nltk.word_tokenize(line)
    # return normLine


def normalizer(line):
    normLine = []
    line = nltk.word_tokenize(line)
    symbols = ['-', '/', '+']
    for token in line:
        if token not in punctuation:
            for symbol in symbols:
                if symbol in token:
                    words = token.split(symbol)
                    for word in words:
                        lem = lemma(word)
                        if lem != 1:
                            normLine.append(lem)
            lem = lemma(token)
            if lem != 1:
                normLine.append(lem)
    return normLine


def normalizerKeys(line):
    vocab = {}
    normLine = []
    line = nltk.word_tokenize(line)
    symbols = ['-', '/', '+']
    for token in line:
        if token not in punctuation:
            for symbol in symbols:
                if symbol in token:
                    words = token.split(symbol)
                    for word in words:
                        lem = lemmaKeys(word, token, vocab)
                        if lem != 1:
                            normLine.append(lem)
            lem = lemmaKeys(token, token, vocab)
            if lem != 1:
                normLine.append(lem)
    return normLine, vocab


def lemma(token):
    lem = lemmatizer.lemmatize(token.lower(), 'v')
    lem = lemmatizer.lemmatize(lem, 'n')
    lem = lemmatizer.lemmatize(lem, 'r')
    lem = lemmatizer.lemmatize(lem, 's')
    lem = lemmatizer.lemmatize(lem, 'a')
    if lem in corpus and len(lem) > 1 and (re.search(r'[A-z]+', lem) is not None) and lem not in stop_words:
        return lem
    else:
        return 1


def lemmaKeys(token, word, vocab):
    lem = lemmatizer.lemmatize(token.lower(), 'v')
    lem = lemmatizer.lemmatize(lem, 'n')
    lem = lemmatizer.lemmatize(lem, 'r')
    lem = lemmatizer.lemmatize(lem, 's')
    lem = lemmatizer.lemmatize(lem, 'a')
    if lem in corpus and len(lem) > 1 and not lem.isdigit() and lem not in stop_words and lem not in punctuation:
        if token not in vocab:
            vocab[lem] = word
        return lem
    else:
        return 1


def tokenKeys(keys):
    newKeys = []
    for i in range(len(keys)):
        newKeys.append([])
        keys[i] = keys[i].replace('\n', ' ')
        keys[i] = keys[i].lower()
        k = word_tokenize(keys[i])
        for j in range(len(k)):
            r = lemmatizer.lemmatize(k[j], 'n')
            if r not in punctuation and k[j] not in stop_words:
                newKeys[i].append(r)
        # newKeys[i] = ''.join(newKeys[i])
    return newKeys


# ss = "This method enables us to compute instances up to L (2,21) using both CPU and GPU computational power with load balancing"
# ss = word_tokenize(ss)
# m = []
# for s in ss:
#     if s not in punctuation:
#         lem = lemmatizer.lemmatize(s.lower(), 'v')
#         lem = lemmatizer.lemmatize(lem, 'n')
#         lem = lemmatizer.lemmatize(lem, 'r')
#         lem = lemmatizer.lemmatize(lem, 's')
#         lem = lemmatizer.lemmatize(lem, 'a')
#         if len(lem) > 1 and (re.search(r'[A-z]+', lem) is not None) and lem not in stop_words:
#             m.append(lem)
# print(m)