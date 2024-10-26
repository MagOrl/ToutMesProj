
# Ici vos fonctions dédiées aux interactions
def affichage_menu(liste_options):
    print("+--------------------------------------+")
    print(" Choisi les informations que tu désire |")
    print("+--------------------------------------+")
    for i in range(len(liste_options)):
        print(i+1,"-->",liste_options[i])
def nombreentrer(message,nombremax):
    messagestr = message + "[1-" +  str(nombremax) + "]" +"\n"
    while True:
        rep = int(input(messagestr))
        if 1<= rep <= nombremax:
            return rep 
        else:
            return None  

def menu(liste_options):
    affichage_menu(liste_options)
    return nombreentrer("Entrez votre choix", len(liste_options))
     

# ici votre programme principal
def programme_principal():
    liste_options = ["Charger un fichier",
                     "Rechercher la population d'une commune",
                     "Afficher la population d'un département", 
                     "Quitter"]
    quitter = False 
    while not quitter:
        rep = menu(liste_options)
        if rep is None:
            print("Cette fonctions n'existe pas, entrez vos réponses de manière cohérente S.V.P")
        elif rep == 1:
            print("Vous avez choisi", liste_options[rep - 1])
        elif rep == 2:
            print("Vous avez choisi", liste_options[rep - 1])
        elif rep == 3:
            print("Vous avez choisi", liste_options[rep - 1])
        elif rep == len(liste_options):
            print("Vous avez choisi", liste_options[rep - 1])
            quitter = True
        input("Appuyer sur Entrée pour continuer")
    print("Merci au revoir!")

programme_principal()