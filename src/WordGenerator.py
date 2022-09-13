import random

def generateWord(occurrenceList:list, firstLetter:str, length:int):

    tolerance = 50
    word = firstLetter

    for n in range(length - 1):

        x = ord(word[len(word) - 1]) - 97
        y = random.randint(0, 25)

        maxProba = max(occurrenceList[x][0:26])

        while(occurrenceList[x][y] < (1 - (tolerance / 100)) * maxProba):
            y = random.randint(0, 25)

        word += chr(y + 97)

    return word

def generateRandomWord(occurrenceList:list, count:int):

    wordsGenerated = []

    for n in range(count):
        wordsGenerated.append(generateWord(occurrenceList, chr(random.randint(0, 25) + 97), random.randint(5, 11)))

    return wordsGenerated