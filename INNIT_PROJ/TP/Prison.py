def sanction(limit, exe):
    pts = 12 
    if exe <= 20 and limit <= 50 : 
        Amende = 45
        pts -=1 
    elif limit >= 50 :
        Amende = 135
        pts -= 1

    if exe > 20 and exe < 30 :
        Amende = 90
        pts -= 2 
    if exe >= 30 and exe < 40 :
        Amende = 90
        pts -= 3 
        Susp = 3
    if exe >= 40 and exe < 50 :
        Amende = 90
        pts -= 3
    if exe >= 50 : 
        Amende = 1500
        pts -=6 
        Susp = 3 
    return pts, Amende, Susp 
print(sanction(50, 50))