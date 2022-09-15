import WordAnalyzer
import WordGenerator

# entrée du programme
def Main():
    words = WordAnalyzer.getWordsFromDictionary("./frdic.txt")
    occurrences, firstLetters = WordAnalyzer.getOccurrences(words)

    #wordsGenerated = WordGenerator.generateRandomWord(occurrences, 10, words)
    #for w in occurrences:
    #    print(w)
    
    print(WordGenerator.generateWord(occurrences, firstLetters, 5, words))

Main()