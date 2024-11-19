def reglejeu(Lx,Cx,Lo,Co):
    Lx = Lx -1 
    Cx = Cx -1
    Lo = Lo -1 
    Co = Co -1
    grille = [["","",""],["","",""],["","",""]]
    perdu = False
    cpt = 0 
    varX = 0
    varcoX = 0
    while not perdu :
        if grille[Lx][Cx] == "":
            grille[Lx][Cx] = "X"
        else:
            print("Case déjà prise") 
        if grille[Lo][Co] == "" :
            grille[Lo][Co] = "O"
        else:
            print("Case déjà prise")
        if grille[0][0] == "X" and grille[1][1] == "X" and grille[-1][-1] == "X" or grille[0][-1] == "X" and grille[1][1] == "X" and grille[-1][0] == "X":
            perdu = True 
        if grille[0][0] == "O" and grille[1][1] == "O" and grille[-1][-1] == "O" or grille[0][-1] == "O" and grille[1][1] == "O" and grille[-1][0] == "O":
            perdu = True
        for j in range(len(grille)):
            for i in range(len(grille)):
                if grille[i][j] != "X"  :
                    varX = 0   
                else:
                    varX+= 1
                if varX == 3:
                    perdu = True
                if grille[j][i] != "X":
                    varcoX = 0
                else:
                    varcoX +=1
                if varcoX == 3:
                    perdu = True
            cpt+=1
            if cpt == 3:
                varX = 0
                varcoX = 0 
            
def menu():
    cpt = 0
    quitter = False
    while not quitter :
        rep = input("Voulez vous (J)ouez au morpion ? \n (Q) pour quitter \n ")
        if rep == "J":
            XplayL = input("X CO DE LIGNE \n")
            XplayC = input("X CO DE COLONNE\n")
            
            cpt = 0
        elif rep == "Q":
            quitter = True
        else:
            if cpt >= 3 :
                print('Visiblement votre IQ doit être assez négatif \n je vous déconseille notre jeu car il sera peut être un effort mental trop conséquent pour votre cerveau')
            else :
                print("[J] pour [J]ouer et [Q] pour Quitter ")
            cpt +=1 
menu()
