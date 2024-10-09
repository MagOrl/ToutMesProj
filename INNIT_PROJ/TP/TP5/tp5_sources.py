def nb_iter_pour3(liste, valeur):
    """[summary]

    Args:
        liste ([liste]): [une liste de nombres entier]
        valeur ([int]): [une valeur entière]

    Returns:
        [int]: [le nombre d'itération qu'il y'a fallu pour faire afficher 20, 3 fois] ou sinon  None si le nombre d'itération pour atteindre 3 n'a pas été faite 
    """
    xxx = 0
    yyy = 0
    for i in range(len(liste)):
        if liste[i] == valeur:
            yyy += 1
            if yyy > 3:
                return xxx
        xxx += 1
    return None


nb_iter_pour3([12, 5, 8, 48, 12, 418, 185, 17, 5, 87], 20)


# ---------------------------------------
# Exemple de scores
# ---------------------------------------
scores = [352100, 325410, 312785, 220199, 127853]
joueurs = ['Batman', 'Robin', 'Batman', 'Joker', 'Batman']

#Exo 2.1
def indiceduprem(phrase):
    for i in range(len(phrase)):
        if phrase[i] in "0123456789":
            return i 
    return None
indiceduprem("on est le 30/09/2021")
# --------------------------------------
# Exemple de villes avec leur population
# --------------------------------------
#Exo 2.2
def popville(liste_villes,population,nomville):
    for i in range(len(liste_villes)):
        if liste_villes[i] == nomville:
            return population[i]
    return None
print(popville(["Blois", "Bourges", "Chartres", "Châteauroux", "Dreux","Joué-lès-Tours", "Olivet", "Orléans", "Tours", "Vierzon"],[45871, 64668,  38426, 43442, 30664, 38250, 22168, 116238,136463,25725],("Orléans")))

#Exo 3.1
def croissant(linst):
    res = None 
    for i in range(len(linst)-1) :
        if linst[i] < linst[i+1]:
            res = True
        else:
            return False
    return res  
print(croissant([5,3,4,8,10]))
#Exo 3.2
def seuilfonc(liste, seuil):
    res = 0
    for i in range(len(liste)):
        res += liste[i]
        if res > seuil :
            return True 
    return False 

print(seuilfonc([1, 4, 1, 2, 3, 4],6))
#Exo 3.3
def mailu(mail):
    cptarobaz = 0
    if "." not in mail:
        return False   
    if "@" not in mail:
            return False
    if " " in mail :
        return False 
    for i in range(len(mail)):
        if mail[i] == "@":
            cptarobaz += 1
            if cptarobaz == 2:
                return False
        if  mail[0] == "@" or mail[0] == "." or mail[-1] == "." or mail[-1] == "@"  :
            return False
    return True 
print(mailu("celestin.maubert@gmail.com"))
        
     
