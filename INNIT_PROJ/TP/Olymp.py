def OlympicQualif(record100m, genre, coursegg, champion):
    if genre == "M":
        if record100m <= 12 and coursegg >= 3 or champion:
            res = True

        else :
            res = False 
    if genre == "F":
        if record100m <= 15 and coursegg >= 3 or champion: 
            res = True
        
        else :
            res = False 
        
    return res 
print(OlympicQualif(12, "M", 3, False))

def test_OlymmpicQualif():
    assert OlympicQualif(12, "F", 4, False) == False
    
     

