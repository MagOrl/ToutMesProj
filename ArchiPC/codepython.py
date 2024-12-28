from PIL import Image
#B.1
i=Image.open("ArchiPC/taffe/hall-mod_0.bmp")
sortie=Image.new(i.mode, i.size)

donne= list(i.getdata())
nouvlist = [[]]
cpt = 0
for i in range(0, len(donne)):
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

#print(listgauche)
#print("")
#print(listdroite)

maindata = []
for i in range(len(listdroite)):
    for d in range(len(listdroite[0])-1,-1,-1):
        maindata.append(listdroite[i][d])

    for g in range(len(listgauche[0])-1,-1,-1):
        maindata.append(listgauche[i][g])
#print(listgauche)
#print("")
#print(listdroite)
#print("")
#print(maindata)

sortie.putdata(maindata)
sortie.save("caca.bmp")















"""for y in range(3, i.size[1]):
    for x in range(i.size[0]):
        c = i.getpixel( (x,y))
        print(c)
        sortie.putpixel((y,x),c)
    print("")
"""
"""for z in range(i.size[1]):
    for m in range(3,i.size[0]):
        g = i.getpixel((m,z))
        print(g)
        sortie.putpixel((z,m),g)
sortie.putpixel((1,0),(255,0,0))
sortie.putpixel((0,1),(0,255,0))
sortie.save("Imageout.bmp")
"""

#sortie=Image.new(i.mode,i.size)
#sortie.putdata(i.getdata())
#sortie.save("Imageout0.bmp")
#sortie=i.copy()
#sortie.putpixel((1,2),(0,0,255))
#sortie.save("Imageout.bmp")