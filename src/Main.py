import WordAnalyzer
import WordGenerator

# entrée du programme
def Main():
    words = WordAnalyzer.getWordsFromDictionary("./frdic.txt")
    occurrences = WordAnalyzer.getOccurrences(words)

    wordsGenerated = WordGenerator.generateRandomWord(occurrences, 10, words)
    for w in wordsGenerated:
        print(w)

Main()