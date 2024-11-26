
# ==========================
# La maison qui rend fou
# ==========================
mqrf1 = {"Abribus":"Astus", "Jeancloddus":"Abribus", "Plexus":"Gugus",
             "Astus":None, "Gugus":"Plexus", "Saudepus":None}   
mqrf2 = {"Abribus":"Astus", "Jeancloddus":None, "Plexus":"Saudepus",
             "Astus":"Gugus", "Gugus":"Plexus", "Saudepus":None}
def quel_guichet(mqrf, guichet):
    """Détermine le nom du guichet qui délivre le formulaire A-38

    Args:
        mqrf (dict): représente une maison qui rend fou
        guichet (str): le nom du guichet de départ qui est le nom d'un guichet de la mqrf

    Returns:
        str: le nom du guichet qui finit par donner le formulaire A-38
    """
    aux = guichet
    if mqrf[guichet] is None:
        return guichet
    else:
        while mqrf[aux] is not None:
            aux = mqrf[aux]
    return aux 

def quel_guichet_v2(mqrf, guichet):
    """Détermine le nom du guichet qui délivre le formulaire A-38
    ainsi que le nombre de guichets visités

    Args:
        mqrf (dict): représente une maison qui rend fou
        guichet (str): le nom du guichet de départ qui est le nom d'un guichet de la mqrf

    Returns:
        tuple: le nom du guichet qui finit par donner le formulaire A-38 et le nombre de
        guichets visités pour y parvenir
    """
    cpt = 1
    aux = guichet
    if mqrf[guichet] is None:
        return (guichet, cpt)
    else:
        while mqrf[aux] is not None:
            aux = mqrf[aux]
            cpt +=1
    return (aux,cpt)
print(quel_guichet_v2(mqrf2,"Abribus")) 


def quel_guichet_v3(mqrf, guichet):
    """Détermine le nom du guichet qui délivre le formulaire A-38
    ainsi que le nombre de guichets visités

    Args:
        mqrf (dict): représente une maison qui rend fou
        guichet (str): le nom du guichet de départ qui est le nom d'un guichet de la mqrf

    Returns:
        tuple: le nom du guichet qui finit par donner le formulaire A-38 et le nombre de
        guichets visités pour y parvenir
        S'il n'est pas possible d'obtenir le formulaire en partant du guichet de depart,
        cette fonction renvoie None
    """
    ...

