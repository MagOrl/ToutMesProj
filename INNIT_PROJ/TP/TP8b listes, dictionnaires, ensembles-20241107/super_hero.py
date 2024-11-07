perso = {'a':(1,1,'a'),'b ':(3,9,'b'),'Cinderilla' :(7,2,'c')}
pers = {}

def intelligence_moyenne(personnage):
    """"""
    if len(personnage) == 0:
        return None 
    cpt = 0
    for value in personnage.values():
        cpt += value[1]
    return cpt/len(personnage)

def kikelplusfort(personnage):
    if len(personnage) == 0:
        return None 
    max = 0
    nomax = ""
    for keys,value in personnage.items():
        if max < value[0]:
            max = value[0]
            nomax = keys
    return nomax

def combienDeCretins(personnage):
    if len(personnage) == 0:
        return None 
    cpt = 0
    for value in personnage.values():
        if value[1] < intelligence_moyenne(personnage):
            cpt += 1
    return cpt
print(combienDeCretins(perso))