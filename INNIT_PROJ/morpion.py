def reglejeu(Lx,Cx,Lo,Co):
    Lx = Lx -1 
    Cx = Cx -1
    Lo = Lo -1 
    Co = Co -1
    grille = [[None,None,None],[None,None,None],[None,None,None]]
    if grille[Lx][Cx] is  None:
        grille[Lx][Cx] = True
    else:
        print("Case déjà prise") 
    if grille[Lo][Co] is None :
        grille[Lo][Co] = False
    else:
        print("Case déjà prise")
    perdu = False
    if grille[]

    


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