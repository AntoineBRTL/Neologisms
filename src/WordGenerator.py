import random

def generateWord(occurrenceList:list, firstLetter:str, length:int, wordlist:list):

    # systeme par tolerance -> 
    # un nombre "t" est la probabilité / tolerance  
    # on recupere la proba "p" de la lettre qui a le plus de chance de tomber 
    # on effectue le produit t * p nous donnant une proba a son tour
    # une lettre est tiré aleatoirement
    #
    # si la proba d'avoir cette lettre en suivant est plus grande que t * p
    # -> alors cette lettre est choisie
    tolerance = 70

    word = firstLetter

    for n in range(length - 1):

        x = ord(word[len(word) - 1]) - 97
        y = random.randint(0, 25)

        # proba qu'elle soit derniere
        endProba = occurrenceList[x][27]
        maxProba = max(occurrenceList[x][0:26])

        # si on a plus de chance de finir le mot que d'avoir une lettre, le mot se fini
        # et si le mot a plus de 3 lettres !
        if(endProba > maxProba and len(word) > 3):
            return word

        while(occurrenceList[x][y] < (1 - (tolerance / 100)) * maxProba):
            y = random.randint(0, 25)

        word += chr(y + 97)

    if(word in wordlist):
        return word
    else:
        return generateWord(occurrenceList, firstLetter, length, wordlist)

def generateRandomWord(occurrenceList:list, count:int, wordlist:list):

    wordsGenerated = []

    for n in range(count):
        wordsGenerated.append(generateWord(occurrenceList, chr(random.randint(0, 25) + 97), random.randint(5, 11), wordlist))

    return wordsGenerated