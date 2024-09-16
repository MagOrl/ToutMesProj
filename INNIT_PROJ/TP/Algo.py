def test2 (m ):
    res = 0 
    for lettre in m : 
        if lettre in 'aeiouy':
            res += 1 
        else : res -= 1 
    
    return res>0      

print(test2("determination"))
        
            
def test_test2 ():
    assert test2("opppa") == True