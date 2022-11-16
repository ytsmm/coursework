import os
from PyPDF2 import PdfFileReader
import csv

data = [["Doi", "Keywords"]]
for filename in os.listdir("pdf"):
    print(filename)
    with open(os.path.join("pdf", filename), 'rb') as f:
        pdf_reader = PdfFileReader(f)
        pages = pdf_reader.getNumPages()
        for i in range(pages):
            dataFile = []
            page = pdf_reader.getPage(i)
            text = page.extractText()
            findDoi = text.find("DOI")
            if findDoi != -1:
                startDoi = text.find("DOI")
                endDOI = text.find("\n", startDoi)
                textDoi = text[startDoi+5:endDOI]
                textDoi = textDoi.replace('\x0c', 'fi')
                if len(textDoi) == 19 and textDoi[8:13] == "/jsfi":
                    dataFile.append(textDoi)

            if text.find("Keywords") != -1:
                startKeywords = text.find("Keywords")
                endKeywords = text.find(".", startKeywords)
                textKeywords = text[startKeywords+10:endKeywords]
                textKeywords = textKeywords.replace('-\n', '')
                textKeywords = textKeywords.replace('\n', ' ')
                textKeywords = textKeywords.replace('ﬁ', 'fi')
                textKeywords = textKeywords.replace('ﬀ', 'ff')
                textKeywords = textKeywords.replace('ﬂ', 'fl')
                textKeywords = textKeywords.replace('ﬃ', 'ffi')
                textKeywords = textKeywords.replace('ﬃ', 'ffi')
                textKeywords = textKeywords.replace('ﬄ', 'ffl')
                textKeywords = textKeywords.replace('\x0c', 'fi')
                textKeywords = textKeywords.replace('’', '')
                textKeywords = textKeywords.replace('–', '-')
                dataFile.append(textKeywords)
            if dataFile:
                data.append(dataFile)
                print(dataFile)
        #break
    #break

#print(data)
with open('data.csv', 'w', encoding="utf-8", newline='') as csvfile:
        writer = csv.writer(csvfile, delimiter=";")
        writer.writerows(data)