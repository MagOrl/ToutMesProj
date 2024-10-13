def fusionner_activites(liste_activites1, liste_activites2):
    """
    Fusionne deux listes d'activités triées chronologiquement en une liste triée chronologiquement
    
    Args:
        liste_activites1 (list): une liste d'activites triée chronologiquement
        liste_activites2 (list): une liste d'activites triée chronologiquement
            
    Returns:
        list: la liste d'activités fusionnée
    """
    listo = liste_activites1 + liste_activites2
    listo.remove(listo[1])
    print(listo)
fusionner_activites([('Lucas', '2024-09-02', 67.2, 'type3')], [('Lucas', '2024-09-01', 70.08, 'type3')])