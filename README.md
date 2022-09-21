# Neologisms
Neologims est un programme developpé en Python dans le cadre d'un projets NSI au lycée.

Ce programme génére des [néologismes](https://fr.wikipedia.org/wiki/N%C3%A9ologisme) en utilisant de réels dictionnaires et ne nécessite aucunes libraries.

## Tester
Executer les commandes suivantes :
1. `git clone https://github.com/AntoineBRTL/Neologisms.git`
2. `cd ./Neologisms`
3. `python ./src/Main.py`

Quelques exemples de mots générés :
- `echivente`
- `chonevet`
- `ideostole`

## Utilisation
1. Commencer par récuperer une liste de mots, vous pouvez utiliser
`WordAnalyzer.getWordsFromDictionary()` prenant en argument un chemin vers un fichier contenant des mots - NB : vous pouvez utiliser un des dictionnaires se situant a la racine.
2. Récuperer une liste de probabilites, `WordAnalyzer.getOccurrences()` prenant en argument la liste de mots et renvoyant un tuple.
3. Générer un mot, `WordGenerator.generateWord()` prenant en argument le premier élément du tuple, puis le second et enfin la liste de mots.