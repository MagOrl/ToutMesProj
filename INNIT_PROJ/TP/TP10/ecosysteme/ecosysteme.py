"""
Init Dev : TP10
Exercice 2 : Ecosystème
"""
ecosysteme_1 = { 'Loup': 'Mouton', 'Mouton':'Herbe', 'Dragon':'Lion', 'Lion':'Lapin', 'Herbe':None, 'Lapin':'Carotte', 'Requin':'Surfer'}

def extinction_immediate(ecosysteme, animal):
    """
    renvoie True si animal s'éteint immédiatement dans l'écosystème faute
    de nourriture
    """
    if ecosysteme[animal] in ecosysteme:
        return False
    return True 


def en_voie_disparition(ecosysteme, animal):
    """
    renvoie True si animal s'éteint est voué à disparaitre à long terme
    """
    var = animal 
    try:
        while ecosysteme[var] is not None:
            
            if var in ecosysteme:
                var = ecosysteme[var]
            else:
                return False
        return False 
    except:
        return True 
print(en_voie_disparition(ecosysteme_1,'Lapin'))


def animaux_en_danger(ecosysteme):
    """ renvoie l'ensemble des animaux qui sont en danger d'extinction immédiate"""
    


def especes_en_voie_disparition(ecosysteme):
    """ renvoie l'ensemble des animaux qui sont en voués à disparaitre à long terme
    """
    ...




