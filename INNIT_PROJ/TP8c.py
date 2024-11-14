def trouver_dans_liste(liste,cible):
    indice = 0
    interon = False
    while indice < len(liste) and interon == False : 
        if liste[indice] == cible:
            interon = True
        indice +=1 
    return interon

def cumul_jusko_seuil(dico, seuil):
    total = 0
    interon = False 
    while interon == False:
        for cle, valeur in dico.items():
            total += valeur
            if total >= seuil:
                interon = True

    return total
