# entrée du program 

def recupererTableau(chemain:str = "./frdic.txt"):
    
    # lire le fichier et le mettre dans une liste
    tableau = []
    fichier1 = open(chemain)
    for ligne in fichier1:
        tableau.append(ligne.replace("\n", "", 1))

    return tableau

def compterLettres(tableau:list):

    tab = [[] * 26]

    for mot in tableau:
        for i in range(len(mot)):
            if(mot[i] == "a"):
                tab[ord("a") - 97][ord(mot[(i + 1) % len(mot)]) - 97] += 1

    print(tab["a"])

    pass

compterLettres(recupererTableau())