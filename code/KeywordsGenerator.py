"""
Функция находит пять ключевых слов для кластера
@:param type: list{float}, myVect - вещественный массив весов слов
@:param type: list{int}, myClusters - целочисленный массив кластеров
@:param type: list{str}, allWords - строковый массив терминов
@:param type: int, number - число кластеров
@:return type: list{str}, keyWords - строковый массив ключевых слов
"""
def KeysGenerator(myVect, myClusters, allwords, number):
    ar = [0] * number
    for i in range(number):
        ar[i] = [0] * len(myVect[i])
    # Складываем веса
    for j in range(number):
        for i in range(len(myClusters)):
            if myClusters[i] == j:
                for l in range(len(myVect[i])):
                    ar[myClusters[i]][l] += myVect[i][l]
    keyWords = []
    for i in range(number):
        # Массив весов
        arCopy = ar[i]
        # Массив пяти наибольших весов
        arSort = sorted(arCopy, reverse=True)[:5]
        keyWords.append('')
        for j in range(len(arSort)):
            ind = arCopy.index(arSort[j])
            # Если слова имеют одинаковый вес
            while allwords[ind] in keyWords[i]:
                ind += 1
            if j == len(arSort) - 1:
                keyWords[i] += allwords[ind]
            else:
                keyWords[i] += allwords[ind] + ', '
    return keyWords