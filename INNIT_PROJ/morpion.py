def tkt(grillou):
    if grillou[0][0] == "O" and grillou[1][1] == "O" and grillou[-1][-1] == "O" or grillou[0][-1] == "O" and grillou[1][1] == "O" and grillou[-1][0] == "O":
        return True
    cpt = 0 
    varX = 0
    varcoX = 0
    for j in range(len(grillou)):
        for i in range(len(grillou)):
            if grillou[i][j] != "O"  :
                varX = 0   
            else:
                varX+= 1
            if varX >= 3:
                print('popo')   
                return True 
            if grillou[j][i] != "O":
                varcoX = 0
            else:
                varcoX +=1
            if varcoX >= 3:
                print("caca")
                return True 
        cpt+=1
        if cpt >= 3:
            varX = 0
            varcoX = 0
     

def jsptkt(grillou):
    cpt = 0 
    varX = 0
    varcoX = 0
    if grillou[0][0] == "X" and grillou[1][1] == "X" and grillou[-1][-1] == "X" or grillou[0][-1] == "X" and grillou[1][1] == "X" and grillou[-1][0] == "X":
        return True
    for j in range(len(grillou)):
        for i in range(len(grillou)):
            if grillou[i][j] != "X"  :
                varX = 0   
            else:
                varX+= 1
            if varX >= 3:
                print('popo')   
                return True 
            if grillou[j][i] != "X":
                varcoX = 0
            else:
                varcoX +=1
            if varcoX >= 3:
                print("caca")
                return True 
        cpt+=1
        if cpt >= 3:
            varX = 0
            varcoX = 0     




def reglejeu():
    grille = [["","",""],["","",""],["","",""]]
    perdu = False
    while not perdu:
        Lx = int(input("ecrit batar")) -1
        Cx = int(input("ecrit batar")) -1
        grille[Lx][Cx] = "X"
        print(grille)

        perdu = jsptkt(grille) 


        Lo = int(input("ecrit batar")) -1
        Co = int(input("ecrit batar")) -1
        grille[Lo][Co] = "O"
        print(grille)
        perdu = tkt(grille)
        

    
reglejeu()
