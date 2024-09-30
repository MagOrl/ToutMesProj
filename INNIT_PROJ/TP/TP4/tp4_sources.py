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

    chiffres="0123456789"
    for i in range(nombre) :
        for carac in nombre :
            if carac in nombre and carac in chiffres  :
                nb = nb *10 + i
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
""""
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
print(trv_mot(["caca", "pipi", "popo", "zizi", "fesse", "vomi", "crottedenez"],"c"))
#exo 5