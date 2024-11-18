grille = [[None,None,True],[None,None,None],[True,None,None]]
var = 0
varco = 0
cpt = 0
reteneurColonne = 0
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
     
       
       