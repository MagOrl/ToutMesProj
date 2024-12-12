ATM={'Armand':'Beatrice','Beatrice':'Cesar','Cesar':'Dalida','Dalida':'Cesar','Etienne':'Beatrice','Firmin':'Henri', 'Gaston':'Beatrice','Henri':'Firmin'}

def amourreciprok(dico):
    amoureu = []
    for elem in dico:
        if elem in dico[dico[elem]] :
            if (dico[elem],elem) in amoureu:
                pass 
            else:
                amoureu.append((elem, dico[elem]))
    return amoureu
print(amourreciprok(ATM))
