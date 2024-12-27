from PIL import Image
#B.1
i=Image.open("ArchiPC/taffe/Imagetest.bmp")
sortie=i.copy()

sortie.save("Imageout.bmp")
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