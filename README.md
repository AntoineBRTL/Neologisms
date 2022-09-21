# Neologisms
Neologims est un programme developpé en Python dans le cadre d'un projets NSI au lycée.

Ce programme genere de faux mots en utilisant de reels dictionnaires et ne necessite aucunes libraries.

## Tester
Executer les commandes suivantes :
1. `git clone https://github.com/AntoineBRTL/Neologisms.git`
2. `cd ./Neologisms`
3. `python ./src/Main.py`

Quelques exemples de mots generés :
- `echivente`
- `chonevet`
- `ideostole`

## Utilisation
1. Commencer par recuperer une liste de mots, vous pouvez utiliser
`WordAnalyzer.getWordsFromDictionary()` prenant en argument un chemin vers un fichier contenant des mots - NB : vous pouvez utiliser un des dictionaires se situant a la racine
2. Recuperer une liste de probabilites, `WordAnalyzer.getOccurrences()` prenant en argument la liste de mots et revoyant un tuple
3. Generer un mot, `WordGenerator.generateWord()` prenant en argument le premier element du tuple, puis le second et enfin la liste de mots