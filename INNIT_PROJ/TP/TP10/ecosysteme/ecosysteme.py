"""
Init Dev : TP10
Exercice 2 : Ecosystème
"""
ecosysteme_1 = { 'Loup': 'Mouton', 'Mouton':'Herbe', 'Dragon':'Lion', 'Lion':'Lapin', 'Herbe':None, 'Lapin':'Carotte', 'Requin':'Surfer'}
ecosysteme_2 = { 'Renard':'Poule', 'Poule':'Ver de terre', 'Ver de terre':'Renard', 'Ours':'Renard' }
ecosysteme_3 = { 'Renard':'Poule', 'Poule':'Ver de terre', 'Ver de terre':'Renard' }
eco = {1:2, 2:3, 3:4, 4:5, 5:17, 6:4, 7:6, 8:9, 9:10, 10:11, 11:8}

def extinction_immediate(ecosysteme, animal):
    """
    renvoie True si animal s'éteint immédiatement dans l'écosystème faute
    de nourriture
    """
    if ecosysteme[animal] in ecosysteme or ecosysteme[animal] is None:
        return False
    return True 


def en_voie_disparition(ecosysteme, animal):
    """
    renvoie True si animal s'éteint est voué à disparaitre à long terme
    """
    var = animal 
    cpt = 0
    try:
        while ecosysteme[var] is not None :
            cpt += 1 
            if var in ecosysteme:
                var = ecosysteme[var]
            else:
                return False
            if cpt > len(ecosysteme):
                return False 
        return False 
    except:
        return True

def animaux_en_danger(ecosysteme):
    """ renvoie l'ensemble des animaux qui sont en danger d'extinction immédiate"""
    ens = set()
    for elem in ecosysteme:
        if extinction_immediate(ecosysteme,elem):
            ens.add(elem)
    return ens 


def especes_en_voie_disparition(ecosysteme):
    """ renvoie l'ensemble des animaux qui sont en voués à disparaitre à long terme
    """
    ens = set()
    for elem in ecosysteme:
        if en_voie_disparition(ecosysteme,elem):
            ens.add(elem)
    return ens




