def KeysGenerator(myVect, myClusters, fn, number):
    # Массив нулей для нахождения суммы весов слов
    ar = [0] * number
    for i in range(number):
        ar[i] = [0] * len(myVect[i])

    # Складываем веса
    for j in range(number):
        for i in range(len(myClusters)):
            if myClusters[i] == j:
                for l in range(len(myVect[i])):
                    ar[myClusters[i]][l] += myVect[i][l]

    # Будущий массив слов
    keyWords = []
    for i in range(number):
        arCopy = ar[i]
        arSort = sorted(arCopy, reverse=True)[:5]
        keyWords.append('Keywords: ')
        for j in range(len(arSort)):
            if j == len(arSort) - 1:
                keyWords[i] = keyWords[i] + fn[arCopy.index(arSort[j])]
            else:
                keyWords[i] = keyWords[i] + fn[arCopy.index(arSort[j])] + ', '
    return keyWords