import os
import csv
from PyPDF2 import PdfReader
import requests
from bs4 import BeautifulSoup as bs


def normalizer(str):
    str = str.replace('ﬁ', 'fi')
    str = str.replace('ﬀ', 'ff')
    str = str.replace('ﬂ', 'fl')
    str = str.replace('ﬃ', 'ffi')
    str = str.replace('ﬃ', 'ffi')
    str = str.replace('ﬄ', 'ffl')
    str = str.replace('\x0c', 'fi')
    str = str.replace("-\n", "")
    return str


def parser():
    data = []
    tryData = []
    for filename in os.listdir("pdf"):
        print(filename)
        with open(os.path.join("pdf", filename), 'rb') as f:
            reader = PdfReader(f)
            for i in range(len(reader.pages)):
                page = reader.pages[i]
                text = page.extract_text()
                dataJournal = []
                if text.lower().find("keywords: ") != -1:
                    # Keywords
                    keywords = text[text.lower().find("keywords: ") + 10:text.lower().find(".", text.lower().find("keywords: "))]
                    keywords = normalizer(keywords)
                    # print("Keywords:", keywords)

                    # DOI
                    doi = text[text.lower().find("doi: ") + 5:text.lower().find("doi: ") + 23].replace('\x0c', 'fi')
                    doi = normalizer(doi)
                    doi = 'https://doi.org/' + doi
                    # print("DOI:", doi)

                    # Open link by DOI
                    r = requests.get('https://doi.org/' + doi)
                    soup = bs(r.text, "html.parser")

                    # Title
                    title = soup.find('h2', class_='page_title').text
                    title = title.replace("\n", "")
                    title = title.replace("\t", "")
                    title = normalizer(title)
                    # print("Title:", title)

                    # Authors
                    authorsSpan = soup.find_all('span', class_='name')
                    authors = []
                    for author in authorsSpan:
                        author = author.text
                        author = author.replace("\n", "")
                        author = author.replace("\t", "")
                        author = normalizer(author)
                        authors.append(author)
                    authors = ', '.join(authors)
                    # print("Authors: ", authors)

                    abstract = soup.find('section', class_='item abstract').text
                    abstract = abstract.replace("\n", "")
                    abstract = abstract.replace("\t", "")
                    abstract = normalizer(abstract)
                    abstract = abstract[8:]

                    dataJournal.append(title)
                    dataJournal.append(authors)
                    dataJournal.append(doi)
                    dataJournal.append(keywords)
                    tryData.append(dataJournal)
                    dataJournal.append(abstract)
                    data.append(dataJournal)

    return data, tryData


dataCsv, tryd = parser()
# print(dataCsv)
with open('articleData.csv', 'w', encoding="utf-8", newline='') as datacsv:
    writer = csv.writer(datacsv, delimiter=";")
    writer.writerows(dataCsv)

with open('articlesDataAll.csv', 'w', encoding="utf-8", newline='') as file:
    writer = csv.writer(file, delimiter=";")
    writer.writerows(tryd)
