from PIL import Image

i=Image.open("ArchiPC/taffe/Image3.bmp")
for y in range(i.size[1]):
    for x in range(i.size[0]):
        c = i.getpixel( (x,y))
        print(c)
    print("")