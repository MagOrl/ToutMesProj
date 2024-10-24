""" TP7 une application complète
    ATTENTION VOUS DEVEZ METTRE DES DOCSTRING A TOUTES VOS FONCTIONS
"""
def afficher_menu(titre, liste_options):
    print("+-------------------------+")
    print(titre,"|")
    print("+-------------------------+")
    imin = 4
    imax = 0
    for i in range(len(liste_options)):
        print(i+1,"-->",liste_options[i])

def demander_nombre(message, borne_max):
    meme = message + "[1-" +  str(borne_max) + "]" +"\n"
    rep = int(input(meme))
    if str(rep).isdecimal() and 0 > rep > 5:
        return rep
    else :
        return None

def menu(titre, liste_options):
    afficher_menu(titre ,liste_options)
    ceci = demander_nombre("Entrez votre choix", len(liste_options))
    return ceci 


def programme_principal():
    liste_options = ["Charger un fichier",
                     "Rechercher la population d'une commune",
                     "Afficher la population d'un département", 
                     "Quitter"]
    liste_communes = []
    quitter =False
    while  not quitter:
        rep = menu("MENU DE MON APPLICATION", liste_options)
        if rep is None:
            print("Cette option n'existe pas")
        elif rep == 1:
            print("Vous avez choisi", liste_options[rep - 1])
        elif rep == 2:
            print("Vous avez choisi", liste_options[rep - 1])
        elif rep == 3:
            print("Vous avez choisi", liste_options[rep - 1])
        elif rep == 4:
            print("Vous avez choisi", liste_options[rep - 1])
            quitter = True
        input("Appuyer sur Entrée pour continuer")
    print("Merci au revoir!")




def charger_fichier_population(nom_fic):
    ...

def population_d_une_commune(liste_pop, nom_commune):
    ...

def liste_des_communes_commencant_par(liste_pop, debut_nom):
    ...

def commune_plus_peuplee_departement(liste_pop, num_dpt):
    ...

def nombre_de_communes_tranche_pop(liste_pop, pop_min, pop_max):
    ...

def place_top(commune, liste_pop):
    ...

def ajouter_trier(commune, liste_pop, taille_max):
    ...


def top_n_population(liste_pop, nbre):
    ...

def population_par_departement(liste_pop):
    ...

def sauve_population_dpt(nom_fic, liste_pop_dep):
    ...

# appel au programme principal
programme_principal()
