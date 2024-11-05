def teste_de_longueur(long_mdp):
    """verifie la longueur de la liste 
        long_mdp(int): la longeure de la liste 
        return(bool): retourne True si la longeure de la liste est suppérieure 8"""
    if len(long_mdp) < 8:
        longeur_ok = False
    else:
        longeur_ok = True
    return longeur_ok
def verifie_chiffre(chaine_character):
    """
    verifie si la chaine contient un chiffre 
    Args:
        chiffre (str): la chaine de caractère à tester
    """
    cpt = 0
    chiffre_ok = False
    for lettre in chaine_character:
        if lettre.isdigit():
           cpt+=1
        if cpt >= 3:
            chiffre_ok = True
    return chiffre_ok
def pas_esapce(chaine_caracter):
    """verifie si dans le mot de passe il y a un espace ou non 
    Args:
        chaine_caracter (str): la chaine de caractère qui est envoyer par l'utilisateur  
    """
    sans_espace = True 
    for lettre in chaine_caracter:
        if lettre == " ":
            sans_espace = False
    return sans_espace
def chiffre_consequitf(chaine_caractère):
    """verifie deux chiffre consécutif"""
    for i in range(len(chaine_caractère)-1):
        if chaine_caractère[i].isdigit() and chaine_caractère[i+1].isdigit():
            return False 
    return True 
def chiffre_plusptit(chienne_caractère):
    """
    fait en sorte que le chiffre le plus petit n'apparait pas 2 fois
    Args:
        chienne_caract (str): 
    """
    min = 10
    cpt = 0
    for i in range(len(chienne_caractère)):
        if chienne_caractère[i].isdigit() and min > chienne_caractère[i]:
            min = chienne_caractère
            cpt +
    for j in  range(len(chienne_caractère)):
        if cpt< 2 :
def motdepasse():
    """Menu qui va demander à l'utilisateur de rentrer un nom et un mot de passe
    """
    connexion = input("Entrez votre nom : ")
    mot_de_passe_correct = False 
    while not mot_de_passe_correct:
        mot_de_passe= input("Entrez votre mot de passe : ")
        if  not teste_de_longueur(mot_de_passe) :
            print("Votre mot de passe doit comporter au moins 8 caractères")
        elif verifie_chiffre(mot_de_passe) == False:
            print("Votre mot de passe doit comporter au moins trois chiffre")
        elif chiffre_consequitf(mot_de_passe) == False:
            print("2 chiffres sont l'un à côté de l'autre")
        elif pas_esapce(mot_de_passe) == False:
            print("Votre mot de passe ne doit pas comporter d'espace")	   
        else:
            mot_de_passe_correct = True 
    print(f"Votre mot de passe est correct \n Bienvenue {connexion}")
    return mot_de_passe
motdepasse()