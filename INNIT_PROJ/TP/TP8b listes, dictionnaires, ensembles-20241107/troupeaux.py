# TP8 B - Manipuler des listes, ensembles et dictionnaires
troupeaux = {"cochon":25,"poule":13,"mouton":14,"canard":30,"vache":12}
troupeau_de_jean = {'vache':12, 'cochon':17, 'veau':3}
troupeaux_vide = {}
def total_animaux(troupeau):
    """ Calcule le nombre total d'animaux dans un troupeau

    Args:
        troupeau (dict): un dictionnaire modélisant un troupeau {nom_animaux: nombre}

    Returns:
        int: le nombre total d'animaux dans le troupeau
    """
    cptsomme = 0 
    for valeur in troupeau.values():
        cptsomme += valeur
    return cptsomme    
def tous_les_animaux(troupeau):
    """ Détermine l'ensemble des animaux dans un troupeau

    Args:
        troupeau (dict): un dictionnaire modélisant un troupeau {nom_animaux: nombre}

    Returns:
        set: l'ensemble des animaux du troupeau
    """
    if len(troupeau) == 0:
        return set()
    list = []
    for keys in troupeau.keys():
        list.append(keys)
    return set(list)
def specialise(troupeau):
    """ Vérifie si le troupeau contient 30 individus ou plus d'un même type d'animal 

    Args:
        troupeau (dict): un dictionnaire modélisant un troupeau {nom_animaux: nombre}

    Returns:
        bool: True si le troupeau contient 30 (ou plus) individus d'un même type d'animal,
        False sinon 
    """
    for valeur in troupeau.values():
        if valeur >= 30:
            return True
    return False


def le_plus_represente(troupeau):
    """ Recherche le nom de l'animal qui a le plus d'individus dans le troupeau
    
    Args:
        troupeau (dict): un dictionnaire modélisant un troupeau {nom_animaux: nombre}

    Returns:
        str: le nom de l'animal qui a le plus d'individus  dans le troupeau
        None si le troupeau est vide) 
    """
    if len(troupeau) == 0:
        return None 
    max = 0
    cle = ""
    for cles,valeur in troupeau.items():
        if max < valeur: 
            max = valeur
            cle = cles 
    return cle 

def quantite_suffisante(troupeau):
    """ Vérifie si le troupeau contient au moins 5 individus de chaque type d'animal

    Args:
        troupeau (dict): un dictionnaire modélisant un troupeau {nom_animaux: nombre}

    Returns:
        bool: True si le troupeau contient au moins 5 individus de chaque type d'animal
        False sinon    
    """
    for value in troupeau.values():
        if value < 5:
            return False
    return True

def reunion_troupeaux(troupeau1, troupeau2):
    """ Simule la réunion de deux troupeaux

    Args:
        troupeau1 (dict): un dictionnaire modélisant un premier troupeau {nom_animaux: nombre}
        troupeau2 (dict): un dictionnaire modélisant un deuxième troupeau        

    Returns:
        dict: le dictionnaire modélisant la réunion des deux troupeaux    
    """
    i = 0
    i2= 0
    cpt = 0
    listo1 = list(troupeau1.items()) 
    listo2 = list(troupeau2.items())
    listofinal = []
    while i < (len(listo1)) and i2 < len(listo2):
        if listo1[i][0] == listo2[i2][0]:
            cpt = listo1[i][1] + listo2[i2][1]  
            listofinal.append(listo1[i][0],)  
    return 
print(reunion_troupeaux(troupeaux,troupeau_de_jean))
