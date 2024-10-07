def est_avant(activite1, activite2):
    """
    Retourne True si activite1 est avant activite2, False sinon
    les activités sont ordonnées selon leur type, puis en cas d'égalité selon le prénom et enfin selon leur date 
    Args:
        activite1 (tuple): une activité
        activite2 (tuple): une activité
    
    Returns:
        bool: True si activite1 est avant activite2, False sinon
    """

    if activite1[3] < activite2[3]:
        return True
    elif activite1[0] < activite2[0]:
        return True
    elif activite1[2] < activite2[2]:
        return True 
    else :
        return False

        
est_avant(('Lucas', '2024-09-01', 67.2, 'type3'), ('Lucas', '2024-09-01', 67.2, 'type4'))