# --------------------------------------
# DONNEES
# --------------------------------------

# exemple de liste d'oiseaux observables
oiseaux = [("Merle", "Turtidé"), ("Moineau", "Passereau"), ("Mésange", "Passereau"),
           ("Pic vert", "Picidae"), ("Pie", "Corvidé"), ("Pinson", "Passereau"),
           ("Rouge-gorge", "Passereau"), ("Tourterelle", "Colombidé")] 

# exemples de listes de comptage ces listes ont la même longueur que oiseaux
comptage1 = [2, 5, 0, 1, 2, 0, 3, 5]
comptage2 = [2, 1, 3, 0, 0, 3, 5, 1]
comptage3 = [0, 0, 4, 3, 2, 1, 2, 4]

# exemples de listes d'observations. Notez que chaque liste correspond à la liste de comptage de
# même numéro
observations1 = [("Merle", 1), ("Moineau", 1), ("Pic vert", 1), ("Pie", 2),
                 ("Rouge-gorge", 3), ("Tourterelle", 5)]

observations2 = [("Merle", 2), ("Mésange", 1), ("Moineau", 3),
                 ("Pinson", 3), ("Tourterelle", 5), ("Rouge-gorge", 1)]

observations3 = [("Mésange", 4), ("Pic vert", 3), ("Pie", 2), ("Pinson", 1),
                 ("Rouge-gorge", 2), ("Tourterelle", 4)]


# --------------------------------------
# FONCTIONS
# --------------------------------------

def oiseau_le_plus_observe(liste_observations):
    """ recherche le nom de l'oiseau le plus observé de la liste
        (si il y en a plusieur on donne le 1er trouve)

    Args:
        liste_observations (list): une liste de tuples (nom_oiseau, nb_observes)

    Returns:
        str: l'oiseau le plus observé (None si la liste est vide)
    """
    #PAR ELEM
    """ 
    oiseau_max = 0
    for observation in liste_observations:
        if observation[1] > oiseau_max:
            oiseau_max = observation[1]
            oiseau_res = observation
    return oiseau_res"""
    #PAR INDICE
    oiseaux_max = 0
    for i in range(len(liste_observations)):
        if liste_observations[i][1] > oiseaux_max:
            oiseaux_max = liste_observations[i][1]
            oiseaux_res = liste_observations[i]
    return oiseaux_res
#print(oiseau_le_plus_observe(observations2))

#EXO 2.1
def famillepiaf(nom, racepiaf):

    for i in range(len(racepiaf)):
        if nom == racepiaf[i][0]:
            return racepiaf[i]
    
    return None 
#print(famillepiaf("Merle", oiseaux))

#EXO 2.2
def findpiaf(famille, listepiaf):
    listo = []
    for i in range(len(listepiaf)):
        if famille == listepiaf[i][1]:
            listo.append(listepiaf[i][0]) 
    return listo
#print(findpiaf("Passereau", oiseaux))
#EXO 3.1
def verifpiaf(liste):
    prec = liste[0]
    if len(liste) == 1 :
        if liste[0][1] == 0:
            return False 
    for elem in liste :
        if elem[0] < prec[0]:
            return False
        if elem[1] == 0:
            return False 
        prec = elem
    
    return True 
#print(verifpiaf(observations1))
#EXO 3.2
def maxpiaf(liste):
    oiseaux_max = 0
    for i in range(len(liste)):
        if liste[i][1] > oiseaux_max:
            oiseaux_max = liste[i][1]
            
    return oiseaux_max 
#print(maxpiaf(observations1))
#EXO 3.3
def moypiaf(listpiaf): 
    cpt = 0 
    moy = 0
    if len(listpiaf) == 0 :
        return None 
    for i in range(len(listpiaf)):
        if listpiaf[i][1]:
            cpt += listpiaf[i][1]
    return cpt/len(listpiaf)    
#print(moypiaf(observations1))
#EXO 3.4
def sommefamillepiaf(listpiaf, famillepiaf, famille):
    cpt = 0
    var = ""
    for i in range(len(listpiaf)):
        if famille == famillepiaf[i][1]:
                cpt += 1
                if famillepiaf[i][0] == listpiaf[i][0]:
                    cpt += 1
    return cpt
print(sommefamillepiaf(observations1, oiseaux,"Passereau"))

            

#--------------------------------------
# PROGRAMME PRINCIPAL
#--------------------------------------

# afficher_graphique_observation(construire_liste_observations(oiseaux, comptage3))
# observes = saisie_observations(oiseaux)
# afficher_graphique_observation(observes)
# afficher_observations(oiseaux, observes)
