import random

def generateWord(occurrenceList:list, firstLetters:str, wordlist:list):
    """Genere un mot"""

    word = ""

    while(True):

        offset = 97

        if(len(word) > 0):

            # on recupere le tableau des proba que l'on veut
            # on recupere la derniere lettre
            oldCharacter = word[len(word) - 1]

            # on recupere sa localisation dans le tableau 
            location = ord(oldCharacter) - offset
            proba = occurrenceList[location]

        else:
            proba = firstLetters

        # on tire un nombre aleatoire
        rand = random.random()

        # on teste a quel ensemble il appartient
        for n in range(26 - 1):
            a = proba[n]
            b = proba[n + 1]

            if(a < rand < b):
                word += chr((n + 1) + offset)
                break
        
            if(n == 24):
                # fin du mot
                if(len(word) <= 5):
                    return generateWord(occurrenceList, firstLetters, wordlist)
                return word