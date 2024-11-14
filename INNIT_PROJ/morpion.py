
# Jeu du morpion

def init_grille():
    ...


def init_joueur():
    ...


def change(joueur):
    ...



def init_jeu(taille=3):
    ...

            

def ajoute_ligne(largeur, gauche, milieu, droite):
    """
    Petite fonction utilitaire pour ajouter des bordures à
    l'affichage des tableau2D
    """ 
    return "   "+gauche + ("──"+milieu)*(largeur-1) + ("──"+droite) +"\n"
    
def affiche(tableau2d):
    """
    Affiche un tableau2D à condition que :
        - le tableau est carré (largeur = hauteur)
        - le tableau ne contient que des chaines de caractères de longueur 0, 1 ou 2
        - le tableau2D est modélisé par une liste de listes
    """
    taille = len(tableau2d)
    affiche = "   "
    for colonne in range(taille):
        affiche+=" C"+str(colonne)
    affiche+="\n"
    affiche += ajoute_ligne(taille, "┌","┬","┐")
    for ligne in range(taille):
        affiche+="L"+str(ligne) + " │"
        for colonne in range(taille):
            valeur = tableau2d[ligne][colonne]
            if valeur is None:
                valeur = ""
            affiche+= valeur + " "*(2-len(valeur))+"│"
        affiche+="\n"
        if ligne != taille-1:
            affiche+= ajoute_ligne(taille, "├","┼","┤")
        else:
            affiche+= ajoute_ligne(taille, "└","┴","┘")
    print(affiche)


def csv_to_liste(fichier):
    ...


def verification_des_lignes(joueur, grille):
    ...

    
def verification_des_colonnes(joueur, grille):
    ...


def verification_des_diagonales(joueur, grille):
    ...


def gagne(joueur, grille):
    ...


def joue(joueur, grille, ligne, colonne):
    """
    Le joueur joue à la position ligne/colonne.
    La fonction met le jeu à jour et envoie True si tout s'est bien passé
    False sinon
    """
    ...


def jeu_est_fini(grille):
    ...

    
    
def coup_valide(ligne, colonne, jeu):
    """
    Le joueur joue à la position ligne/colonne.
    La fonction met le jeu à jour et envoie True si tout s'est bien passé
    False sinon
    """
    ...


def lance_jeu():
    ...

                    


def affiche_menu():
    fin = False
    while not fin:
        reponse = input("=====================\nJeu du morpion\nQuel est votre choix ?\n(J)ouer ou (Q)uitter ? ")
        if reponse == 'J':
            lance_jeu()
        elif reponse == 'Q':
            fin = True


affiche_menu()
