
# exercice 3
def nb_mots(phrase):
    """Fonction qui compte le nombre de mots d'une phrase

    Args:
        phrase (str): une phrase dont les mots sont
        séparés par des espaces (éventuellement plusieurs)

    Returns:
        int: le nombre de mots de la phrase
    """    
    resultat = 0
    c1 = ''
    # au début de chaque tour de boucle
    # c1 vaut 
    # c2 vaut
    # resultat vaut
    for c2 in phrase:
        if c1 == ' ' and c2 != ' ': 
            resultat = resultat +1
            c1 = c2
        else : 
            c1 = c2
    if phrase =="" or phrase[0] ==" ":
        return resultat
    else :
        return resultat+1
print(nb_mots(" houla!     je    mets beaucoup   d'  espaces    "))

def test_nb_mots():
    assert nb_mots("bonjour, il fait beau") == 4
    assert nb_mots(" houla!     je    mets beaucoup   d'  espaces    ") == 6
    assert nb_mots(" ce  test ne  marche pas ") == 5
    assert nb_mots("") == 0  # celui ci non plus

