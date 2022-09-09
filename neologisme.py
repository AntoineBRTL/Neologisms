# tableaux avec proba cummulés

def recupererTableau(chemain:str = "./frdic.txt"):
    
    # lire le fichier et le mettre dans une liste
    tableau = []
    fichier1 = open(chemain)

    for ligne in fichier1:
        tableau.append(ligne.replace("\n", "", 1))

    return tableau

def compterLettres(tableau:list):

    alphabetOffest = 97

    tableauOccurrences = [[0 for x in range(26)] for x in range(26)]

    # methode n² * plus rapide
    for mot in tableau:
        for i in range(len(mot) - 1):
            
            lettre = mot[i]
            tlx = ord(lettre) - alphabetOffest

            lettreSuivante = mot[(i + 1)]
            tly = ord(lettreSuivante) - alphabetOffest

            if(0 <= tlx <= 25 and 0 <= tly <= 25):
                tableauOccurrences[tlx][tly] += 1

    # uniformiser le tableau des occurrences (en %)
    for iox in range(len(tableauOccurrences)):
        for ioy in range(len(tableauOccurrences[iox])):
            tableauOccurrences[iox][ioy] = (tableauOccurrences[iox][ioy] / sum(tableauOccurrences[iox])) * 100
            pass

    return tableauOccurrences

def nouveauMot(nombreDeLettres):
    if(nombreDeLettres <= 2):
        raise ValueError('Mot de moins ou egal a 2 lettres dans le programme')

    print("erreur passée")

    return

# entrée du program 
def main():

    tab = recupererTableau()
    tabOccu = compterLettres(tab)

    #for line in tabOccu:
    #    print(line)
    nouveauMot(5)

main()