"""Init Dev : TP10"""
pokedex_anakin = {
        ('Carmache', 'Dragon'), ('Carmache', 'Sol'),
        ('Colimucus', 'Dragon'), ('Palkia', 'Dragon'),
        ('Palkia', 'Eau')}
pokedex_romain = {('Maraiste','Eau'),('Maraiste','Sol'),('Racaillou','Sol'),('Racaillou','Roche')}     

# =====================================================================
# Exercice 1 : Choix de modélisation et complexité
# =====================================================================
# Modélisation n°1
# =====================================================================

# Penser à completer la fonction exemples_pokedex_v1 dans le fichier de tests

def appartient_v1(pokemon, pokedex): 
    """ renvoie True si pokemon (str) est présent dans le pokedex """
    for elem in pokedex:
        if pokemon in elem[0]:
            return True
    return False

def toutes_les_attaques_v1(pokemon, pokedex): 
    """
    param: un pokedex et le nom d'un pokemon (str) qui appartient au pokedex
    resultat: renvoie l'ensemble des types d'attaque du pokemon passé en paramètre
    """
    ens = set()
    for elem in pokedex:
        if  pokemon == elem[0] :
            ens.add(elem[1])
    return ens 
def nombre_de_v1(attaque, pokedex): 
    """
    param: un pokedex et un type d'attaque (str)
    resultat: renvoie le nombre de pokemons de ce type d'attaque
    dans le pokedex
    """
    dico = {}
    for elem in pokedex:
        if elem[0] in dico.keys():
            dico[elem[0]] +=1 
        else:
            dico[elem[0]] = 1 
    


def attaque_preferee_v1(pokedex):
    """
    Renvoie le nom du type d'attaque qui est la plus fréquente dans le pokedex
    """
    ...


# =====================================================================
# Modélisation n°2
# =====================================================================

# Penser à completer la fonction exemples_pokedex_v2 dans le fichier de tests

def appartient_v2(pokemon, pokedex):
    """ renvoie True si pokemon (str) est présent dans le pokedex """
    ...


def toutes_les_attaques_v2(pokemon, pokedex):
    """
    param: un pokedex et le nom d'un pokemon (str) qui appartient au pokedex
    resultat: renvoie l'ensemble des types d'attaque du pokemon passé en paramètre
    """
    ...


def nombre_de_v2(attaque, pokedex):
    """
    param: un pokedex et un type d'attaque (str)
    resultat: renvoie le nombre de pokemons de ce type d'attaque
    dans le pokedex
    """
    ...


def attaque_preferee_v2(pokedex):
    """
    Renvoie le nom du type d'attaque qui est la plus fréquente dans le pokedex
    """
    ...

# =====================================================================
# Modélisation n°3
# =====================================================================

# Penser à completer la fonction exemples_pokedex_v3 dans le fichier de tests


def appartient_v3(pokemon, pokedex):
    """ renvoie True si pokemon (str) est présent dans le pokedex """
    ...


def toutes_les_attaques_v3(pokemon, pokedex):
    """
    param: un pokedex et le nom d'un pokemon (str) qui appartient au pokedex
    resultat: renvoie l'ensemble des types d'attaque du pokemon passé en paramètre
    """
    ...


def nombre_de_v3(attaque, pokedex):
    """
    param: un pokedex et un type d'attaque (str)
    resultat: renvoie le nombre de pokemons de ce type d'attaque
    dans le pokedex
    """
    ...


def attaque_preferee_v3(pokedex):
    """
    Renvoie le nom du type d'attaque qui est la plus fréquente dans le pokedex
    """
    ...

# =====================================================================
# Transformations
# =====================================================================

# Version 1 ==> Version 2

def v1_to_v2(pokedex_v1):
    """
    param: prend en paramètre un pokedex version 1
    renvoie le même pokedex mais en version 2
    """
    ...


# Version 1 ==> Version 2

def v2_to_v3(pokedex_v2):
    """
    param: prend en paramètre un pokedex version2
    renvoie le même pokedex mais en version3
    """
    ...
