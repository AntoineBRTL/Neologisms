def recupererTableau(chemain:str = "./frdic.txt"):
    
    # lire le fichier et le mettre dans une liste
    tableau = []
    fichier1 = open(chemain)
    for ligne in fichier1:
        tableau.append(ligne.replace("\n", "", 1))

    return tableau

def compterLettres(tableau:list):

    alphabetOffest = 97

    tableauOccurrences = [[0] * 26] * 26

    """# methode lente 
    # boucle sur tout l'alphabet
    # TODO: opptimiser la boucle n**4
    for tlx in range(26):
        lettrex = chr(tlx + alphabetOffest)

        for tly in range(26):
            lettrey = chr(tly + alphabetOffest)

            for mot in tableau:

                # len(mot) - 1 car on a pas besoin de regarder la lettre suivante si c'est la derniere
                for i in range(len(mot) - 1):

                    lettre = mot[i]

                    if(lettre == lettrex):

                        lettreSuivante = mot[i + 1]

                        if(lettreSuivante == lettrey):

                            tableauOccurrences[tlx][tly] += 1"""

    # methode n² * plus rapide
    for mot in tableau:
        for i in range(len(mot) - 1):
            
            lettre = mot[i]
            tlx = ord(lettre) - alphabetOffest

            lettreSuivante = mot[i + 1]
            tly = ord(lettreSuivante) - alphabetOffest

            if(0 <= tlx <= 26 and 0 <= tly <= 26):
                tableauOccurrences[tlx][tly] += 1

            return tableauOccurrences

    # uniformiser le tableau des occurrences
    for iox in range(len(tableauOccurrences)):
        for ioy in range(len(tableauOccurrences[iox])):
            tableauOccurrences[iox][ioy] = int((tableauOccurrences[iox][ioy] / sum(tableauOccurrences[iox])) * 100)

    return tableauOccurrences

# entrée du program 
def main():

    tab = recupererTableau()
    tabOccu = compterLettres(tab)

    # afficher le tableau
    # print(tabOccu)

    for line in tabOccu:
        print(line)

main()