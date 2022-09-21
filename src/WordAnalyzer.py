def getWordsFromDictionary(path:str = "./frdic.txt"):
    """Renvois un tableau content les mots d'un fichier dictionnaire"""

    dictionaryAsList = []
    file = open(path)

    for line in file:
        dictionaryAsList.append(line.replace("\n", "", 1))

    return dictionaryAsList

def _placeInOccurences(occurenceList:list, locationX:int, locationY:int):
    """Teste si l'emplacement est correct, dans ce cas, ajoute 1 a cet emplacement"""

    # certains caracteres comme "-" ne sont pas dans l'alphabet et ne sont donc pas compris entre 0 et 25
    # ils ne seront alors pas repertoiriés dans le tableau
    # 26 pour locationY pour la case "fin"

    if(0 <= locationX <= 25 and 0 <= locationY <= 26):
        occurenceList[locationX][locationY] += 1

    return occurenceList

def _normalizeOccurences(occurrenceList:list, firstLetterList:list, listOfWords:list):
    """Divise par la somme du tableau"""

    # normalisation sur les lettres
    for x in range(26):

        # somme de toute la liste
        letterSum = sum(occurrenceList[x])
        firstLettreSum = sum(firstLetterList)

        for y in range(26):

            # division par l'addition de la ligne entiere
            occurrenceList[x][y] /= letterSum

            # normalization du tableau des premieres lettres
            firstLetterList[y] /= firstLettreSum

        occurrenceList[x][26] /= letterSum

    return occurrenceList, firstLetterList

def _cumulateOccurences(occurrenceList:list, firstLetterList:list):
    """Transforme les tableaux de probabilités en probabilités cumulées"""

    # creation de nouveaux tableaux
    cumulated = [[0 for x in range(27)] for x in range(26)]
    firstLetterCumulated = [0 for x in range(26)]
    
    for x in range(26):

        # on place dans le tableau les 2 premiers elements
        cumulated[x][0] = occurrenceList[x][0]
        cumulated[x][1] = cumulated[x][0] + occurrenceList[x][1]
        firstLetterCumulated[0] = firstLetterList[0]
        firstLetterCumulated[1] = firstLetterCumulated[0] + firstLetterList[1]

        for y in range(2, 26):

            # on cumule les probas
            cumulated[x][y] = cumulated[x][y - 1] + occurrenceList[x][y]
            firstLetterCumulated[y] = firstLetterCumulated[y - 1] + firstLetterList[y]

        # case de fin
        # elle est toujours = 1
        cumulated[x][26] = 1

    return cumulated, firstLetterCumulated

def getOccurrences(listOfWords:list):
    """Genere un tableau de probabilités pour chaques lettres, renvoie un tuple contenant deux tableaux"""

    # car ord("a") = 97
    offset = 97

    # 26 * 27 
    # la derniere ligne est pour les probabilités de derniere lettres
    occurrenceList = [[0 for x in range(27)] for x in range(26)]

    # autre tableau pour les premieres lettres
    firstCharactersList = [0 for x in range(26)]

    for word in listOfWords:

        # premier caractere
        firstCharacter = word[0].lower()
        location = ord(firstCharacter) - offset

        # on teste si le premier Carractere est une letter de l'alphabet 
        if(0 <= location <= 25):
            firstCharactersList[location] += 1

        # caracteres suivants
        # -1 car la derniere lettre n'a pas de lettre suivante
        for n in range(len(word) - 1):
            
            # on recupere la lettre a l'indice n du mot -> letter
            # on recupere son equivalent entier, il sert d'index pour le tableau -> locationX
            character = word[n].lower()
            locationX = ord(character) - offset

            # meme principe pour la lettre suivante -> (n + 1)
            nextCharacter = word[n + 1].lower()
            locationY = ord(nextCharacter) - offset

            _placeInOccurences(occurrenceList, locationX, locationY)
                

        # caractere de fin
        lastCharacter = word[len(word) - 1]

        # placer la derniere lettre dans le tableau 
        locationX = ord(lastCharacter) - offset
        locationY = 26
        _placeInOccurences(occurrenceList, locationX, locationY)

    # on normalise le tableau des occurrences
    occurrenceList, firstCharactersList = _normalizeOccurences(occurrenceList, firstCharactersList, listOfWords)

    # faire des probas cumulées
    occurrenceList, firstCharactersList = _cumulateOccurences(occurrenceList, firstCharactersList)

    return occurrenceList, firstCharactersList