dico = {'A':1 , 'B':2 , 'C':3,'B':4}
courses_morticia = ["bave de crapeau","oeufs de dragon","lézards" ,"ketchup" ,"sel"]
facture_morticia = [17 , 157 , 17 , 2 , 1]
course_morticialist = [ "bave de crapeau" , 17 , "oeufs de dragon" , 157 ,"lézards" , 17 , "ketchup" , 2 , "sel" , 1]
courses_morticiadico = { " bave de crapeau " :17 , "oeufs de dragon " :157 ," l é zards " :17 , " ketchup " :2 , " sel " :1}
courses_morticialistup = [( " bave de crapeau " , 17) , ( " oeufs de dragon " , 157) ,
( " l é zards " , 17) , ( " ketchup " , 2) , ( " sel " , 1) ]
def ajout_art52(liste1,liste2,nomart,prixart):
    liste1.append(nomart)
    liste2.append(prixart)
    return liste1,liste2 
def ajout_art53(liste,nomart,prixart):
    liste.append(nomart)
    liste.append(prixart)
    return liste
def ajout_art54(dico,nomart,prixart):
    dico[nomart] = prixart
    return dico 
def ajout_art56(list,nomart,prixart):
    list.append((nomart,prixart))
    return list 

def remove_art52(liste1,liste2,nomart):
    i=0
    while i < len(liste1):
        if nomart == liste1[i]:
            liste1.remove(liste1[i])
            liste2.remove(liste2[i])
        i+=1 
    return liste1,liste2

def remove_art53(liste,nomart):
    i=0
    while i < len(liste):
        if liste[i] == nomart: 
            liste.remove(liste[i])
            liste.remove(liste[i-1])
        i+=2
    return liste
def remove_art56(liste,nomart):
    i=0 
    while 



