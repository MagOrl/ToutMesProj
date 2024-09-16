def test(a,b,c,d):  


    if a < b :
        res = a 

    else :
        res = b

    if c < res :
        res = c

    if d < res :
        res = d 
    return res 
print(test(0,0,3,15))


   