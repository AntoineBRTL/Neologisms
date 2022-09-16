import WordAnalyzer
import WordGenerator

# entrée du programme
def main():
    words = WordAnalyzer.getWordsFromDictionary("./endic.txt")
    occurrences, firstLetters = WordAnalyzer.getOccurrences(words)

    #wordsGenerated = WordGenerator.generateRandomWord(occurrences, 10, words)
    #for w in occurrences:
    #    print(w)
    
    print(WordGenerator.generateWord(occurrences, firstLetters, words))

main()