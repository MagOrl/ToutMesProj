
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
def intwannbe(nombre):
    nb = 0
    chiffres="0123456789"
    for i in range(len(nombre)) :
        for carac in nombre :
            if carac in nombre and carac in chiffres  :
                nb = nb *10 + i

    return nb
    
print(intwannbe("2021"))
            
        
        