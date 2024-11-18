def reglejeu(Lx,Cx,Lo,Co):
    Lx = Lx -1 
    Cx = Cx -1
    Lo = Lo -1 
    Co = Co -1
    grille = [[True,True,True],[None,None,None],[None,None,None]]
    perdu = False
    while not perdu :
        if grille[Lx][Cx] is  None:
            grille[Lx][Cx] = True
        else:
            print("Case déjà prise") 
        if grille[Lo][Co] is None :
            grille[Lo][Co] = False
        else:
            print("Case déjà prise")
        for i in range(len(grille)):
            if  grille[i][:3] is True:
                print("Victoire du joueur X")
                perdu = True
            elif grille[i][:3] is False:
                print("Victoire du joueur O")
                perdu = True 
            

        
        

    


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