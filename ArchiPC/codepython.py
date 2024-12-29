from PIL import Image


def B1changecouleur(img):
    i=Image.open(img)
    sortie = i.copy()
    for y in range(i.size[1]):
        for x in range(i.size[0]):
            c = i.getpixel( (x,y))
            sortie.putpixel((y,x),c)
    sortie.save("Imageout.bmp")

#appel de fonction ici
#B1changecouleur("ArchiPC/taffe/hall-mod_0.bmp")


def B2mirror(img):
    i=Image.open(img)
    sortie=Image.new(i.mode, i.size)

    donne= list(i.getdata())
    nouvlist = [[]]
    cpt = 0
    for i in range(len(donne)):
        if len(nouvlist[cpt]) < sortie.size[0]:
            nouvlist[cpt].append(donne[i])
        else:
            nouvlist.append([donne[i]])
            cpt +=1 
    cptg = 0
    cptd = 0
    listgauche = [[]]
    listdroite = [[]]

    for i in range(len(nouvlist)):
        for y in range(len(nouvlist[i])//2):
            listgauche[cptg].append(nouvlist[i][y])
        cptg +=1
        listgauche.append([])
        for z in range(len(nouvlist[i])//2,len(nouvlist[i])):
            listdroite[cptd].append(nouvlist[i][z])
        listdroite.append([])
        cptd +=1
    del listdroite[-1]
    del listgauche[-1]

    maindata = []
    for i in range(len(listdroite)):
        for d in range(len(listdroite[0])-1,-1,-1):
            maindata.append(listdroite[i][d])

        for g in range(len(listgauche[0])-1,-1,-1):
            maindata.append(listgauche[i][g])

    sortie.putdata(maindata)
    sortie.save("Imageout1.bmp")
#appel de fonction ici
#B2mirror("ArchiPC/taffe/hall-mod_0.bmp")












