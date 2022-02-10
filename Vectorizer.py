import re
import string
import pandas as pd

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.cluster import KMeans


def Vectorizing(text):
    tfidf_vector = TfidfVectorizer()
    tfidf = tfidf_vector.fit_transform(text)
    return tfidf


