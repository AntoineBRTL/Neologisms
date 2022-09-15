from binascii import b2a_base64
import random

def generateWord(occurrenceList:list, firstLetters:str, length:int, wordlist:list):
    """Genere un mot"""

    # TODO: generer a partir de proba
    word = ""

    for i in range(length):

        offset = 97

        # on recupere le tableau des proba que l'on veut
        if(i == 0):
            proba = firstLetters
        else:
            # on recupere la derniere lettre
            lastLetter = word[len(word) - 1]

            # on recupere sa localisation dans le tableau 
            location = ord(lastLetter) - offset
            proba = occurrenceList[location]

        # on tire un nombre aleatoire
        rand = random.random()

        # on teste a quel ensemble il appartient
        for n in range(26 - 1):
            a = proba[n]
            b = proba[n + 1]

            if(a < rand < b):
                word += chr((n + 1) + offset)
                break

            # fin de boucle
            if(n == 24):
                return word

    return word


def generateRandomWord(occurrenceList:list, count:int, wordlist:list):
    """Genere une liste de mots"""

    wordsGenerated = []

    for n in range(count):
        wordsGenerated.append(generateWord(occurrenceList, chr(random.randint(0, 25) + 97), random.randint(3, 11), wordlist))

    return wordsGenerated