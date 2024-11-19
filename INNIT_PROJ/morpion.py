def reglejeu(Lx,Cx,Lo,Co):
    Lx = Lx -1 
    Cx = Cx -1
    Lo = Lo -1 
    Co = Co -1
    grille = [[True,True,True],[None,None,None],[None,None,None]]
    perdu = False
    cpt = 0 
    var 
    while not perdu :
        if grille[Lx][Cx] is  None:
            grille[Lx][Cx] = True
        else:
            print("Case déjà prise") 
        if grille[Lo][Co] is None :
            grille[Lo][Co] = False
        else:
            print("Case déjà prise")
        if grille[0][0] == True and grille[1][1] == True and grille[-1][-1] or grille[0][-1] == True and grille[1][1] == True and grille[-1][0] == True:
            print("pipi")
        for j in range(len(grille)):
            for i in range(len(grille)):
                if grille[i][j] != True  :
                    var = 0   
                else:
                    var+= 1
                if var == 3:
                    print("cayeeeee")
                if grille[j][i] != True:
                    varco = 0
                else:
                    varco +=1
                if varco == 3:
                    print("CACAAAAAAAAA")
            cpt+=1
            if cpt == 3:
                var = 0
                varco = 0 
            

        
        

    


def menu():
    cpt = 0
    quitter = False
    while not quitter :
        rep = input("Voulez vous (J)ouez au morpion ? \n (Q) pour quitter \n ")
        if rep == "J":
            pass
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