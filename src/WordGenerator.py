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

        # on teste entre quelles probabilités le nombre aleatoire se trouve
        for n in range(26):
            a = proba[n]

            if(rand < a):
                word += chr(n + offset)
                break
        
            # On arrive a la lettre "z" et le nombre aleatoire est plus grand que la probabilité d'avoir la lettre "z"
            if(n == 25):

                # On ce cas on arrete le mot si il contient assez de lettres sinon on en regenere un
                if(len(word) <= 5):
                    return generateWord(occurrenceList, firstLetters, wordlist)

                return word