dico = {'A':1 , 'B':2 , 'C':3,'B':4}
courses_morticia = ["bave de crapeau","oeufs de dragon","lézards" ,"ketchup" ,"sel"]
facture_morticia = [17 , 157 , 17 , 2 , 1]
course_morticialist = [ "bave de crapeau" , 17 , "oeufs de dragon" , 157 ,"lézards" , 17 , "ketchup" , 2 , "sel" , 1]
courses_morticiadico = { " bave de crapeau " :17 , "oeufs de dragon " :157 ,"lézards" :17 , " ketchup " :2 , " sel " :1}
courses_morticialistup = [( " bave de crapeau " , 17) , ( " oeufs de dragon " , 157) ,( "lézards" , 17) , ( " ketchup " , 2) , ( " sel " , 1) ]
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
    while i < len(liste):
        if liste[i][0] == nomart:
            liste.pop(i)
        i+=1
    return liste
def remove_art54(dico,nomart):
    del dico[nomart]
    return dico 
def modif_prix52(liste1,liste2,nomart,prix):
    for i in range(len(liste1)):
        if liste1[i] == nomart:
            liste2[i] = prix 
    return (liste1,liste2)
def modifprix53(liste,nomart,prix):
    for i in range(0,len(liste),2):
        if liste[i] == nomart:
            liste[i+1] = prix
    return liste 
def modifprix56(liste,nomart,prix):
    for i in range(len(liste)):
        if liste[i][0] == nomart:
            liste[i] = ((liste[i][0],prix))
    return liste
def modifprix54(dico,nomart,prix):
    dico[nomart] = prix 
    return dico 
def cptart52(liste2):
    cpt = 0
    for compt in liste2:
        cpt += compt
    return cpt 
def cptart53(liste):
    cpt = 0 
    for i in range(1,len(liste),2):
        cpt += liste[i]
    return cpt
def cptart54(dico):
    cpt = 0 
    for val in dico.values():
        cpt += val 
    return cpt 
def cptart56(lise):
    cpt = 0
    for i in range(len(lise)):
        cpt+= lise[i][1]
    return cpt
def maxart52(liste):
    max = liste[0]
    for i in range(len(liste)):
        if max < liste[i]:
            max = liste[i]
    return max 
def maxart53(liste):
    max = liste[1]
    for i in range(1,len(liste),2):
        if max < liste[i] :
            max = liste[i]
    return max 
def maxart56(liste):
    max = liste[0][1]
    for i in range(len(liste)):
        if max < liste[i][1]:
            max = liste[i][1]
    return max 
def maxart54(dico):
    max = -1
    for val in dico.values():
        if max < val:
            max = val 
    return max

def menu(option):
    print("~~~~~~~~~~La liste d'Adams~~~~~~~~~~")
    for i in range(len(option)):
        print('choisi option',option,i+1)
def programme():
    listoption=["Supprime un art","total des prix", "ajoute un art",'modif un art']
    print(menu(listoption))
    quitter = False
    while not quitter:
        rep = input("Entre une réponse")
        if rep == 1:           
programme()