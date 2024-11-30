def tkt(grillou):
    if grillou[0][0] == "O" and grillou[1][1] == "O" and grillou[-1][-1] == "O" or grillou[0][-1] == "O" and grillou[1][1] == "O" and grillou[-1][0] == "O":
        print('Victoire du O')
        return True
    autresauv = 0 
    varX = 0
    varcoX = 0
    ptitsauv = 0
    for j in range(len(grillou)):
        for i in range(len(grillou)):
            if grillou[i][j] != "O" or ptitsauv != j :
                varX = 0   
            else:
                varX+= 1
            ptitsauv = j 
            if varX >= 3:
                print('Victoire du O')
                return True

            if grillou[j][i] != "O" or autresauv != j :
                varcoX = 0
            else:
                varcoX +=1
            autresauv = j 
            if varcoX >= 3:
                print('Victoire du O')
                return True 
    return False 


def jsptkt(grillou):
    if grillou[0][0] == "X" and grillou[1][1] == "X" and grillou[-1][-1] == "X" or grillou[0][-1] == "X" and grillou[1][1] == "X" and grillou[-1][0] == "X":
        print("Victoire du X")
        return True
    autresauv = 0 
    varX = 0
    varcoX = 0
    ptitsauv = 0
    for j in range(len(grillou)):
        for i in range(len(grillou)):
            if grillou[i][j] != "X" or ptitsauv != j:
                varX = 0   
            else:
                varX+= 1
            ptitsauv = j 
            if varX >= 3:
                print("Victoire du X")
                return True 

            if grillou[j][i] != "X" or autresauv != j:
                varcoX = 0
            else:
                varcoX +=1
            autresauv = j 
            if varcoX >= 3:
                print("victoire du X")
                return True   
    return False 

def affichagedutruc(grilliard):
    for i in range(len(grilliard)):
        print(f"{grilliard[i]}\n")




def reglejeu():
    grille = [["","",""],["","",""],["","",""]]
    perdu = False
    cpt = 0
    affichagedutruc(grille)
    while not perdu :
        joueurquitter  = {"X":False,"O":False}
        while not joueurquitter["O"]:
            try:
                Lo = int(input("Joueur O : ecrit le numéro de ta ligne\n")) -1
                Co = int(input("Joueur O : ecrit le numéro de ta colonne\n")) -1
                if grille[Lo][Co] == "":
                    grille[Lo][Co] = "O"
                    joueurquitter["O"] = True 
                else:
                    affichagedutruc(grille)
                    print("Case déjà prise")
            except :
                affichagedutruc(grille)
                print("Mettre une case entre 1 et 3")
        perdu = tkt(grille)  
        cpt +=1   
        if cpt == 9 :
            print("Draw ! ")
            perdu = True 
        affichagedutruc(grille)

        if perdu is False :
            while not joueurquitter["X"]:
                try:
                    Lx = int(input("Joueur X : écrit le numéro de ta ligne\n")) -1
                    Cx = int(input("Joueur X : écrit le numéro de ta colonne\n")) -1
                    if grille[Lx][Cx] == "":
                        grille[Lx][Cx] = "X"
                        joueurquitter["X"] = True 
                    else:
                        affichagedutruc(grille)
                        print("Case déjà prise veuillez en mettre une nouvelle")
                except:
                    affichagedutruc(grille)
                    print("Mettre une valeur entre 1 et 3 stp")
            perdu = jsptkt(grille)   
            cpt += 1   
            if cpt == 9 :
                print("Draw ! ")
                perdu = True 
            affichagedutruc(grille)

#appel fonc
reglejeu()
