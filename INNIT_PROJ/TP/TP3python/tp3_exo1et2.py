# exercice 1
from sympy import false, true


def mystere_exo2(entree):
    """[summary]

    Args:
        entree ([int]): [la liste de nombre ]

    Returns:
        [bool]: [retourne TRUE si le nombre de pair est supérieure ou égale à impair, false sinon ]
    """
    pair = 0 
    impair= 0 
    # au début de chaque tour de boucle
    #  pair compte le nombre de nombre pair et impair les impairs 
    for list_nb in entree:
        if list_nb % 2 == 0:
            pair += 1
        else:
            impair += 1
    return pair >= impair
print(mystere_exo2([1,4,6,-2,-5,3,10]))
print(mystere_exo2([-4,5,-11,-56,5,-11]))

"""def test_mystere_exo2():
    assert mystere_exo2([1,2,-7,29,30,25,20]) == true
    assert mystere_exo2([478,53,61,47,21,52,64]) == false
    assert mystere_exo2([1,3,-9,45,70,22,26]) == false
    assert mystere_exo2([1,6,42,100,99,80,15]) == true """


# exercice 2
def min_sup(liste_nombres, valeur):
    """trouve le plus petit nombre d'une liste supérieur à une certaine valeur

    Args:
        liste_nombres (list): la liste de nombres
        valeur (int ou float): la valeur limite du minimum recherché

    Returns:
        int ou float: le plus petit nombre de la liste supérieur à valeur
    """
    
 
    res = None
    # au début de chaque tour de boucle res est le plus petit élément
    # déjà énuméré supérieur à valeur*
    #faut faire une deuxième boucle for
     
 
    for elem in liste_nombres:
        if elem > valeur :
            if res is None or elem < res :
                res = elem 
             

    return res
print(min_sup([8, 12, 7, 3, 9, 2, 1, 4, 9], 5))

"""def test_min_sup():
    assert min_sup([8, 12, 7, 3, 9, 2, 1, 4, 9], 5) == 7
    assert min_sup([5, 7, 6, 5, 7, 3], 10) is None
    assert min_sup([], 5) is None
    assert min_sup([-2, -5, 2, 9.8, -8.1, 7], 0) == 2"""""

