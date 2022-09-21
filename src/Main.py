import WordAnalyzer
import WordGenerator

# entrée du programme
def main():
    words = WordAnalyzer.getWordsFromDictionary("./frdic.txt")
    occurrences, firstLetters = WordAnalyzer.getOccurrences(words)
    
    print(WordGenerator.generateWord(occurrences, firstLetters, words))

main()