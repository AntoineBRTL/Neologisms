def getWordsFromDictionary(path:str = "./frdic.txt"):
    """Renvois un tableau content les mots d'un dictionaire"""

    # lire le fichier et le mettre dans une liste
    array = []
    file = open(path)

    for ligne in file:
        # On enleve les caracteres comme celui du saut de ligne ("\n")
        array.append(ligne.replace("\n", "", 1))

    return array

def placeInOccurences(lst:list, locationX:int, locationY:int):

    # certains caracteres comme "-" ne sont pas dans l'alphabet et donc ne sont pas compris entre 0 et 25
    # ils ne serons donc pas repertoiriés dans le tableau
    # 27 pour locationY pour les 2 cases "debut" & "fin" en plus
    if(0 <= locationX <= 25 and 0 <= locationY <= 27):
        lst[locationX][locationY] += 1

    return lst

def normalizeOccurences(lst:list, wordlist:list):

    # normalisation sur les lettres
    for x in range(26):

        # somme de toute la liste à l'exeption des cases "debut" & "fin"
        letterSum = sum(lst[x][0:26])

        for y in range(26):

            # division par l'addition de la ligne entiere
            lst[x][y] /= letterSum

    # normalization sur les cases "debut" & "fin"
    for x in range(26):
        lst[x][26] /= len(wordlist)
        lst[x][27] /= len(wordlist)

    return

def getOccurrences(wordlist:list):
    """Renvois un tableau double contenent les probabilités de lettre suivante par rapport a une autre, a partir d'une liste de mot"""

    # ord("a") : 97
    offset = 97

    occurrenceList = [[0 for x in range(28)] for x in range(26)]

    for word in wordlist:

        # debut du tableau
        firstLetter = word[0]

        # placer la premiere lettre dans le tableau 
        locationX = ord(firstLetter) - offset
        locationY = 26

        placeInOccurences(occurrenceList, locationX, locationY)

        # fin du tableau
        lastLetter = word[len(word) - 1]

        # placer la derniere lettre dans le tableau 
        locationX = ord(lastLetter) - offset
        locationY = 27

        placeInOccurences(occurrenceList, locationX, locationY)

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
                placeInOccurences(occurrenceList, locationX, locationY)

    # on normalise le tableau des occurrences
    normalizeOccurences(occurrenceList, wordlist)

    return occurrenceList