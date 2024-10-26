import bilan_carbone as bc
# Ici vos fonctions dédiées aux interactions
def affichage_menu(liste_options):
    print("+--------------------------------------+")
    print(" Choisi les informations que tu désire |")
    print("+--------------------------------------+")
    for i in range(len(liste_options)):
        print(i + 1, "-->", liste_options[i])

def nombreentrer(message, nombremax):
    messagestr = message + "[1-" + str(nombremax) + "]" + "\n"
    while True:
        try:
            rep = int(input(messagestr))
            if 1 <= rep <= nombremax:
                return rep
            else:
                print(f"Veuillez entrer un nombre entre 1 et {nombremax}.")
        except ValueError:
            print("Veuillez entrer un nombre valide.")

def menu(liste_options):
    affichage_menu(liste_options)
    return nombreentrer("Entrez votre choix ", len(liste_options))
  
                    
                    #########################################################################################################""
# Ici votre programme principal
def programme_principal():
    liste_options = ["Recherche d'une personne",
                     "charger un fichier",
                     "fusionner 2 liste ", 
                     "Quitter"]
    quitter = False 
    while not quitter:
        rep = menu(liste_options)
        print("Vous avez choisi : [", liste_options[rep - 1],"]")
        if rep == 1:
                para = input("Mettre un prenom de la liste" + "\n")
                print(f"Voici toutes les activité liée à {para}" +"\n")
                print(bc.filtre_par_prenom(bc.charger_activites(('./PythonSEA/Bilan Carbone mystérieux-20241002/emission.csv')),para))
                if bc.filtre_par_prenom(bc.charger_activites(('./PythonSEA/Bilan Carbone mystérieux-20241002/emission.csv')),para) == []:
                    print("la recherche n'a pas abouti"+"\n"+ "Le prénom n'est pas dans la liste "+ "\n"+"Ou vous avez surement mal tapper le prénom, un prénom commence par une majuscule et ne contient aucun espace")
                
        if rep == len(liste_options):
            quitter = True
        
        input("Appuyer sur Entrée pour continuer")
    print("Merci au revoir!")
#appel de fonction
programme_principal() 