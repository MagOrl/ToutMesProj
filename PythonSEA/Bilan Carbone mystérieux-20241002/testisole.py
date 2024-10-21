co2_minute = {'type1': 0.87, 'type2': 0.65, 'type3': 0.96, 'type4': 0.63}

def temps_activite( co2_minute):
    """
    Retourne la durée d'une activité en minutes
    
    Args:
        activite (tuple): une activité
        co2_minute (dict): un dictionnaire associant un type d'activité à une émission de CO2 par minute
            
    Returns:
        float: la durée de l'activité en minutes
    """
    listo = []
    for elem in co2_minute.items():
        listo.append(elem)
    return listo 
print(temps_activite(co2_minute))