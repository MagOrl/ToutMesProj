""" 
#exo 2
def plus_long_plateau(liste_villes, population):
    people = 0
    ini = ""
    for i in range(len(population)):
        if population[i] > people :
            people = population[i]
            ini = liste_villes[i]
    return ini

print(plus_long_plateau(["Blois", "Bourges", "Chartres", "Châteauroux", "Dreux","Joué-lès-Tours", "Olivet", "Orléans", "Tours", "Vierzon"], [45871, 64668,  38426, 43442, 30664, 38250, 22168, 116238, 136463,25725]))
"""
#exo 3
"""""
def intwannbe(nombre):
    nb = 0
    chiffres = "0123456789"

    for carac in nombre:
        for i in range(len(chiffres)):
            if carac == chiffres[i]:
                nb = nb * 10 + i
                break #J'ai trouver cette fonction sur internet et elle permet de sauver un peu de temps de calcul, par exemple ici tout les chiffres sont unique donc pas besoin de faire tourner la boucle à chaque fois si cette dernière à déjà été trouver une fois

    returnzz nb

print(intwannbe("2021"))
"""
"""
#exo4
def trv_mot(liste, lettre):
    listset = []
    for i in range(len(liste)):
        for carac in liste[i] :
            if lettre  != carac[0] :
                break#J'ai trouver cette fonction sur internet et elle permet de sauver un peu de temps de calcul, par exemple je n'ai pas envie qu'elle continue après la première lettre donc je break
            else :
                listset.append(liste[i])
                break
    return listset
"""


#exo 5
"""
def ma_var(text):
    setlist = []
    mot = ""
    for char in text:
        if char.isalpha(): 
            mot += char 
        elif mot :
            setlist.append(mot)  
            mot = ""  
    return setlist
print(ma_var("Cela fait déjà 28 jours! 28 jours à l’IUT'O! Cool"))
"""
"""
#exo 6
def trv_mot(text,lettre):
    setlist = []
    nouvlist = []
    mot = ""
    for i in range(len(text)):
        if text[i].isalpha(): 
            mot += text[i] 
        elif mot :
            setlist.append(mot)  
            mot = ""
    for u in range(len(setlist)):
        if lettre == setlist[u][0]:
            nouvlist.append(setlist[u])
    return nouvlist 
print(trv_mot("cela fait déjà 28 jours! 28 jours à l’IUT'O! cool!!", "c"))
"""
#exo 7.1 

def vraisof2(n):
    boolist = [False,False]
    for i  in range(2, n+1):
        boolist.append(True)
    return boolist 

#print(vraisof2(6))

#exo 7.2
#REVOIE CE CODE 
def indicebool(boolist, x):
    for i in range (len(boolist)):
        if i%x == 0 and i != x:
            boolist[i] = False
    return boolist
#print(indicebool(vraisof2(6),2))

def era(n):
    liste = [False, False]
    listenb = []
    for s in range(2,n+1) :
        liste.append(True)
        mop = 3*3
        pop = 5*5
        top = 7*7
        for x in range(2, len(liste), 2 and mop and pop and top ):
            liste[x] = False
    for i in range(len(liste)):
        if liste[i] == True :
            listenb.append(i)
    return listenb
print(era(6))