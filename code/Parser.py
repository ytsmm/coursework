import os
import re
from PyPDF2 import PdfReader
import requests
from bs4 import BeautifulSoup as bs


data = []
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
                keywords = text[text.lower().find("keywords: ")+10:text.lower().find(".", text.lower().find("keywords: "))]
                keywords = keywords.replace("-\n", "")
                # print("Keywords:", keywords)

                # DOI
                doi = text[text.lower().find("doi: ") + 5:text.lower().find("doi: ") + 23].replace('\x0c', 'fi')
                doi = 'https://doi.org/' + doi
                # print("DOI:", doi)

                # Open link by DOI
                r = requests.get('https://doi.org/' + doi)
                soup = bs(r.text, "html.parser")

                # Title
                title = soup.find('h2', class_='page_title').text
                title = title.replace("\n", "")
                title = title.replace("\t", "")
                # print("Title:", title)

                # Authors
                authorsSpan = soup.find_all('span', class_='name')
                authors = []
                for author in authorsSpan:
                    author = author.text
                    author = author.replace("\n", "")
                    author = author.replace("\t", "")
                    authors.append(author)
                authors = ', '.join(authors)
                # print("Authors: ", authors)
                dataJournal.append(title)
                dataJournal.append(authors)
                dataJournal.append(doi)
                dataJournal.append(keywords)
                data.append(dataJournal)
    break

for k in data:
    print(k)
