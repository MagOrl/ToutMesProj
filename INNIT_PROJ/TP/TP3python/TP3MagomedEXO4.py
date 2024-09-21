"""Travaille fait par ARSAMERZOEV Magomed en i11A """

#partie 1
def somme_pair(nombre) :
    """fonction qui fait la somme des nombres pair 
    Arg :
        nombre(int) : liste de nombres 
    Return :
        (int) : la somme des nombre pair
    """
    res = 0 
    # à chaque tour de boucle 
    # res vaut 0 (inisialiser à 0)
    # pair vaut le premier nombre de ma liste de nombre
    for pair in nombre :
        if pair%2 == 0:

         res += pair     
    return res 
def test_somme_pair():
   assert somme_pair([12,13,6,5,7]) == 18
   assert somme_pair([14,72,90,21,23]) == 176
   assert somme_pair([-4,-42,39,21,63]) == -46
   assert somme_pair([9,15,16,52]) == 69 

#----------------------------------------------------------------------------
#Partie 2
def last_voy(mot):
    """fonction qui fait donne la dernière voyelle de ma chaine de charactère
    Arg :
        mot(str) : ma chaine de charactère  
    Return :
        (str) : la dernière voyelle de ma chaine de charactère  
    """
    verif = None
    # à chaque tour de boucle
    #verif vaut None
    #lettre vaut la première lettre de ma chaine de charactère
    for lettre in mot:  
        if lettre in "aeiouy":
            verif = lettre  
    return verif 

def test_last_voy():
    assert last_voy("matador") == "o"
    assert last_voy("mmphhmphh") == None 
    assert last_voy("baththth") == "a"
    assert last_voy(" peau ") == "u"

#--------------------------------------------------------------------------------
#Partie 3
def prop_nega(nombre):
    """fonction qui fait la proportion des chiffre négatif avec la longuer de la liste de nombre donner 
    Arg :
        nombre(int) : liste de nombres 
    Return :
        (float) : le nombre de négatif sur la longueure de la liste
    """
    nb_nega = 0
    res = None
    # à chaque tour de boucle
    # nb_nega vaut 0
    #res vaut None
    # Nega est le premier nombre de ma liste de nombre
    for nega in nombre:
        if  nega < 0 :
            nb_nega += 1
            res = nb_nega / len(nombre)
        else : 
            res = 0
        
    return res 

def test_prop_nega():
    assert prop_nega([-2,-3,-5,-6]) == 1
    assert prop_nega([-3, 5, -4, 6]) == 0.5
    assert prop_nega([1,2,3,4]) == 0
    assert prop_nega([]) == None 
      