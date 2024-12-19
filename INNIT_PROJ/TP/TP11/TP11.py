import api_matrice as mat
ATM={'Armand':'Beatrice','Beatrice':'Cesar','Cesar':'Dalida','Dalida':'Cesar','Etienne':'Beatrice','Firmin':'Henri', 'Gaston':'Beatrice','Henri':'Firmin'}

def amourreciprok(dico):
    amoureu = []
    for elem in dico:
        if elem in dico[dico[elem]] :
            if (dico[elem],elem) in amoureu:
                pass 
            else:
                amoureu.append((elem, dico[elem]))
    return amoureu

def soupirant(personne, dico):
    personneamoureu = []
    for elem in dico:
        if dico[elem] == personne:
            personneamoureu.append(elem)
    return personneamoureu

def sous_matrice(matrice, nb_lignes, nb_colonnes, position_haut, position_gauche):
    
    mato = mat.creer_matrice(nb_lignes,nb_colonnes)
    
    for i in range (nb_lignes):
        for j in range(nb_colonnes):
            mat.set_valeur(mato,i,j,matrice[position_haut + i ][position_gauche + j])
    return mato 
  

mati = [[1,2,3],[4,5,6],[7,8,9]]
print(sous_matrice(mati,2,2,0,0))

def colle_sous_matrice(matrice,sous_matrice,ligne_haut,colonne_gauche):
    for i in range(len(sous_matrice)):
        for j in range(len(sous_matrice[1])):
            matrice[ligne_haut + i][colonne_gauche +j] = sous_matrice[i][j]
    return matrice 

sousmat = [[67, 42], [43, 17]]

print(colle_sous_matrice(mati,sousmat,0,0))

#exo 4
