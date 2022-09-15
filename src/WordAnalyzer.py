def getWordsFromDictionary(path:str = "./frdic.txt"):
    """Renvois un tableau content les mots d'un dictionaire"""

    # lire le fichier et le mettre dans une liste
    array = []
    file = open(path)

    for ligne in file:
        # On enleve les caracteres comme celui du saut de ligne ("\n")
        array.append(ligne.replace("\n", "", 1))

    return array

def _placeInOccurences(lst:list, locationX:int, locationY:int):
    """Teste si l'emplacement est correct, dans ce cas, ajoute 1 a cette emplacement"""
    # certains caracteres comme "-" ne sont pas dans l'alphabet et donc ne sont pas compris entre 0 et 25
    # ils ne serons donc pas repertoiriés dans le tableau
    # 27 pour locationY pour les 2 cases "debut" & "fin" en plus
    if(0 <= locationX <= 25 and 0 <= locationY <= 26):
        lst[locationX][locationY] += 1

    return lst

def _normalizeOccurences(occurrenceList:list, firstLetterList:list, wordlist:list):

    """Divise par la somme du tableau"""
    # normalisation sur les lettres
    for x in range(26):

        # somme de toute la liste à l'exeption des cases "debut" & "fin"
        letterSum = sum(occurrenceList[x][0:26])
        firstLettreSum = sum(firstLetterList)

        for y in range(26):

            # division par l'addition de la ligne entiere
            occurrenceList[x][y] /= letterSum

            # normalization du tableau des premieres lettres
            firstLetterList[y] /= firstLettreSum

    # normalization sur les caracteres de fin
    for x in range(26):
        occurrenceList[x][26] /= len(wordlist)

    return occurrenceList, firstLetterList

def _cumulateOccurences(occurrenceList:list, firstLetterList:list):

    cumulated = [[0 for x in range(27)] for x in range(26)]

    firstLetterCumulated = [0 for x in range(26)]
    
    for x in range(26):

        cumulated[x][0] = occurrenceList[x][0]
        cumulated[x][1] = cumulated[x][0] + occurrenceList[x][1]

        firstLetterCumulated[0] = firstLetterList[0]
        firstLetterCumulated[1] = firstLetterCumulated[0] + firstLetterList[1]

        for y in range(2, 26):
            cumulated[x][y] = cumulated[x][y - 1] + occurrenceList[x][y]
            firstLetterCumulated[y] = firstLetterCumulated[y - 1] + firstLetterList[y]

        cumulated[x][26] = 1

    return cumulated, firstLetterCumulated

def getOccurrences(wordlist:list):
    """Renvois un tableau double contenent les probabilités de lettre suivante par rapport a une autre, a partir d'une liste de mot"""

    # ord("a") : 97
    offset = 97

    occurrenceList = [[0 for x in range(27)] for x in range(26)]
    firstLetterList = [0 for x in range(26)]

    for word in wordlist:

        if(0 < ord(word[0].lower()) - offset < 25):
            firstLetterList[ord(word[0].lower()) - offset] += 1

        # fin du tableau
        lastLetter = word[len(word) - 1]

        # placer la derniere lettre dans le tableau 
        locationX = ord(lastLetter) - offset
        locationY = 26

        _placeInOccurences(occurrenceList, locationX, locationY)

        # -1 car la derniere lettre n'a pas de lettre suivante
        for n in range(len(word) - 1):
            
            # on recupere la lettre a l'indice n du mot -> letter
            # on recupere son equivalent entier, il sert d'index pour le tableau -> locationX
            letter = word[n].lower()
            locationX = ord(letter) - offset

            # meme principe pour la lettre suivante -> (n + 1)
            nextLetter = word[(n + 1)].lower()
            locationY = ord(nextLetter) - offset

            # certains caracteres comme "-" ne sont pas dans l'alphabet et donc ne sont pas compris entre 0 et 25
            # ils ne serons donc pas repertoiriés dans le tableau
            if(0 <= locationX <= 25 and 0 <= locationY <= 25):
                _placeInOccurences(occurrenceList, locationX, locationY)

    # on normalise le tableau des occurrences
    occurrenceList, firstLetterList = _normalizeOccurences(occurrenceList, firstLetterList, wordlist)

    # faire des probas cumulées
    occurrenceList, firstLetterList = _cumulateOccurences(occurrenceList, firstLetterList)

    return occurrenceList, firstLetterList