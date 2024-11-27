def reglejeu():
    grille = [["","",""],["","",""],["","",""]]
    cpt = 0 
    varX = 0
    varcoX = 0
    perdu = False
    while not perdu:
        Lx = int(input("ecrit batar")) -1
        Cx = int(input("ecrit batar"))-1
        grille[Lx][Cx] = "X"
        print(grille)
        Lo = int(input("ecrit batar"))-1
        Co = int(input("ecrit batar")) -1
        grille[Lo][Co] = "O"
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
            if cpt >= 3:
                varX = 0
                varcoX = 0 
        print(grille)

    
print(reglejeu())
