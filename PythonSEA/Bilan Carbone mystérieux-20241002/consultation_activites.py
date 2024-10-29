import bilan_carbone as bc
# Ici vos fonctions dédiées aux interactions
def affichage_menu(liste_options):
    """L'affichage du menu principale 
    args(liste): liste d'option proposer """
    print("+--------------------------------------+")
    print(" Choisi les options que tu désire      |")
    print("+--------------------------------------+")
    for i in range(len(liste_options)):
        print(i + 1, "-->", liste_options[i])

def nombreentrer(message, nombremax):
    """regarde le nombre entrer par la personne et  détermine si elle est juste ou non
        arg(str): message du menu
        arg(int): la longeur de la liste d'option
        
        return:
        (int): le nombre choisi par l'utilisateur """
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
    """Le menu en entièreté
        arg(liste): pour pouvoir afficher toutes les options disponible"""
    affichage_menu(liste_options)
    return nombreentrer("Entrez votre choix ", len(liste_options))
def indepth(liste_info):
    """affichage du menu de la liste d'option des choix de fonctions à faire tourner
    arg(list): la liste d'option de fonction à faire tourner"""
    for i in range(len(liste_info)):
        print(i + 1, "-->", liste_info[i])
def nombreindepth(message, nombremax):
    """regarde le nombre entrer par la personne et  détermine si elle est juste ou non
        arg(str): message du menu
        arg(int): la longeur de la liste d'option de fonction
        
        return:
        (int): le nombre choisi par l'utilisateur """
    messagestr = message + "[1-" + str(nombremax) + "]" + "\n"
    while True:
        try:
            repinfo = int(input(messagestr))
            if 1 <= repinfo <= nombremax:
                return repinfo
            else:
                print(f"Veuillez entrer un nombre entre 1 et {nombremax}.")
        except ValueError:
            print("Veuillez entrer un nombre valide.")
def menuindepth(liste_info):
    """affichage complet du menu de fonctions
    arg(list): la liste de fonctions disponible"""
    affichage_menu(liste_info)
    return nombreentrer("Entrez votre choix ", len(liste_info))
# Ici votre programme principal
def programme_principal():
    """Le programme principale, reprennant toutes les autres fonctions, pour pouvoir avoir un affichage adéquoit pour que l'utilisateur
    puisse interagire avec le fichier emission.csv, plus de documentation dans le code et dans l'option 4:'Comment utiliser le programme' """
    liste_options = ["Recherche d'info",
                     "Sauvgarder les info dans un fichiers CSV",
                     "Voir vos listes sauvgarder","Comment utiliser le programme",
                     "Quitter"]
    liste_info =["Recherche par nom(1*)",
                 "Teste si 2 liste est croissant(2)","Donne le maximum d'une emission(1)",
                 "Fusion de listes(2*)","Recherche(N/A)","Liste de personne uniquement(1)","Cumul du temps d'activité d'une liste(1)","date de première apparition d'un type(1)",
                 "filtres selon plusieures critères(1*)","Plus longue suite d'émission décroissante(1)","Verifie si liste est trier(1)","Liste de types uniquement(1)","Temps d'activité pour 1 seule profile(N/A)",
                 "Savoir l'année d'un profile(N/A)","Savoir l'année et le mois d'un profile(N/A)","Emission totale d'une liste(1)",
                 "Retour au menu\n le chiffre entre paranthèse signifie le nombre de liste qu'il faut avoir sauvgarder au préalable \n pour les options ou on à besoin de qu'une seule liste il est aussi possible de le faire avec la grande liste(c'est comme ca qu'on enregistres des listes) \n les '*' signifie que l'option propose d'enregistrer la liste obtenu pour la manipuler par la suite"]
    saved = {}
    quitter = False 
    while not quitter:
        quitterinfo = False
        rep = menu(liste_options)
        print("Vous avez choisi : [", liste_options[rep - 1],"]")
        if rep == 1:
            while not quitterinfo:
                repinfo =  menuindepth(liste_info)
                print("Vous avez choisi : [",liste_info[repinfo - 1] ,"]")
                if repinfo == 1:
                    if len(saved) != 0:
                        question = input("voulez vous utiliser l'une de vos liste[Y/N]"+"\n" "si vous repondez [N]on nous allons utiliser la grande liste"+"\n")
                        if question == "Y":
                            clef = input("Quelle liste voulez vous mettre ?"+"\n")
                            para = input("Mettre un prenom de la liste" + "\n")
                            for keys,valeur in saved.items():
                                if clef == keys:
                                    valoc = valeur
                                if bc.filtre_par_prenom(valoc, para) == []:
                                    print("> la recherche n'a pas abouti:"+"\n"+ "  indice : Le prénom n'est pas dans la liste "+ "\n"+"  indice : Vous avez surement mal tapper le prénom, un prénom commence par une majuscule et ne contient aucun espace")
                                else:
                                    print(f"Voici toutes les activité liée à {para}" +"\n")
                                    varloc = bc.filtre_par_prenom(valoc,para)
                                    print(varloc)
                                    listYN = input("Voulez vous sauvgarder les information ? [Y/N]"+"\n")
                                    if listYN == "N":
                                        pass 
                                    elif listYN == "Y":
                                        nomlist = input("donner un nom a donner à la variable"+"\n")
                                        saved[nomlist] = varloc
                                        print("Jusqu'à la fin de votre session, le nom de la liste se nomera " + nomlist)
                                    else:
                                        print("réponse par Y pour Oui et N pour Non")
                        elif question == "N":
                            para = input("Mettre un prenom de la liste" + "\n")
                        if bc.filtre_par_prenom(bc.charger_activites(('./PythonSEA/Bilan Carbone mystérieux-20241002/emission.csv')),para) == []:
                            print("> la recherche n'a pas abouti:"+"\n"+ "  indice : Le prénom n'est pas dans la liste "+ "\n"+"  indice : Vous avez surement mal tapper le prénom, un prénom commence par une majuscule et ne contient aucun espace")
                        else :
                            print(f"Voici toutes les activité liée à {para}" +"\n")
                            varloc = bc.filtre_par_prenom(bc.charger_activites(('./PythonSEA/Bilan Carbone mystérieux-20241002/emission.csv')),para)
                            print(varloc)
                            listYN = input("Voulez vous sauvgarder les information ? [Y/N]"+"\n")
                            if listYN == "N":
                                pass 
                            elif listYN == "Y":
                                nomlist = input("donner un nom a donner à la variable"+"\n")
                                saved[nomlist] = varloc
                                print("Jusqu'à la fin de votre session, le nom de la liste se nomera " + nomlist)
                            else:
                                print("réponse par Y pour Oui et N pour Non")
                    else :
                        para = input("Mettre un prenom de la liste" + "\n")
                        if bc.filtre_par_prenom(bc.charger_activites(('./PythonSEA/Bilan Carbone mystérieux-20241002/emission.csv')),para) == []:
                            print("> la recherche n'a pas abouti:"+"\n"+ "  indice : Le prénom n'est pas dans la liste "+ "\n"+"  indice : Vous avez surement mal tapper le prénom, un prénom commence par une majuscule et ne contient aucun espace")
                        else :
                            print(f"Voici toutes les activité liée à {para}" +"\n")
                            varloc = bc.filtre_par_prenom(bc.charger_activites(('./PythonSEA/Bilan Carbone mystérieux-20241002/emission.csv')),para)
                            print(varloc)
                            listYN = input("Voulez vous sauvgarder les information ? [Y/N]"+"\n")
                            if listYN == "N":
                                pass 
                            elif listYN == "Y":
                                nomlist = input("donner un nom a donner à la variable"+"\n")
                                saved[nomlist] = varloc
                                print("Jusqu'à la fin de votre session, le nom de la liste se nomera " + nomlist)
                            else:
                                print("réponse par Y pour Oui et N pour Non")                     
                if repinfo == 2:
                    if len(saved) >= 2:
                        try :
                            clay1 = input("Quelle est la premiere liste que voulez vous mettre ?"+"\n")
                            clay2 = input("Quelle est la deuxième liste que voulez vous mettre ?"+"\n")
                            for keys,valeur in saved.items():
                                if clay1 == keys:
                                    varloc1 = valeur
                                else:
                                    print("aucune liste de ce nom")
                            for key, valor in saved.items():
                                if clay2 == key:
                                    varloc2 = valor
                                else:
                                    ("aucune liste de ce nom")
                            if varloc1 and varloc2:
                                tar = bc.est_avant(varloc1,varloc2)
                                if tar == False: 
                                    print(f"Votre liste {clay1} n'est pas avant votre liste {clay2}")
                                else:
                                    print(f"Votre liste {clay1} est avant votre liste {clay2}")
                        except:
                            print("ERREUR : Vous avez surement mal tapper l'une de vos 2 listes ou les 2, retourner sur le menu pour voir le nom de vos listes ")
                    else:
                        print("il faut sauvgarder plus de 2 listes")
                if repinfo == 3 :
                    if len(saved) != 0:
                        question = input("voulez vous utiliser l'une de vos liste[Y/N]"+"\n" "si vous repondez [N]on nous allons utiliser la grande liste"+"\n")
                        if question == "Y":
                            try :
                                clef = input("Quelle liste voulez vous mettre ?\n")
                                for keys,valeur in saved.items():
                                    if clef == keys:
                                        valoc = valeur
                                print(f"la consomation maximal de votre liste {clef} est {bc.max_emmission(valoc)}")
                            except:
                                print("Recherche n'a pas abouti vous avez surement mal tapper le nom de votre liste, retourner dans le menu principal et choissisez la 3ème option pour avoir le nom de vos listes ")
                        if question == "N":
                            print(f"la consomation maximal est{bc.max_emmission(bc.charger_activites(('./PythonSEA/Bilan Carbone mystérieux-20241002/emission.csv')))}")
                    else:
                        print(f"la consomation maximale est{bc.max_emmission(bc.charger_activites(('./PythonSEA/Bilan Carbone mystérieux-20241002/emission.csv')))}")
                if repinfo == 4:
                    if len(saved) >= 2:
                        clay1 = input("Quelle est la premiere liste que voulez vous mettre ?"+"\n")
                        clay2 = input("Quelle est la deuxième liste que voulez vous mettre ?"+"\n")
                        for keys,valeur in saved.items():
                            if clay1 == keys:
                                varlocal1 = valeur
                            else:
                                print("aucune liste de ce nom")
                        for key, valor in saved.items():
                            if clay2 == key:
                                varlocal2 = valor
                            else:
                                print("aucune liste de ce nom")
                        print(bc.fusionner_activites(varlocal1,varlocal2))
                        print(f"voici la fusion entre {clay1} et {clay2}")
                        listYN = input("Voulez vous sauvgarder les information ? [Y/N]"+"\n")
                        if listYN == "N":
                            pass 
                        elif listYN == "Y":
                            nomlist = input("donner un nom a donner à la variable"+"\n")
                            saved[nomlist] = bc.fusionner_activites(varlocal1,varlocal2)
                            print("Jusqu'à la fin de votre session, le nom de la liste se nomera " + nomlist)
                        else:
                            print("réponse par Y pour Oui et N pour Non")
                    else: 
                        print("Veuillez avoir plus de 2 listes sauvgarder")
                if repinfo == 5:
                    if len(saved) != 0:
                        question = input("voulez vous utiliser l'une de vos liste[Y/N]"+"\n" "si vous repondez [N]on nous allons utiliser la grande liste"+"\n")
                        if question == "Y":
                            cle = input("quelle liste voulez vous mettre \n")
                            paranom =input("Quelle nom cherchez vous ?\n")
                            parajour = input("Quelle date cherchez vous ?"+"\n"+'format: "anne-mm-jj"\n') 
                            paratype = input("Quelle type cherchez vous ? \n")
                            print(f"Voici la trouvaille : {bc.recherche_activite_dichotomique(paranom,parajour,paratype,valoc)}\n")
                        if question == "N":
                            try :
                                paranom =input("Quelle nom cherchez vous ?\n")
                                parajour = input("Quelle date cherchez vous ?"+"\n"+'format: "anne-mm-jj"\n') 
                                paratype = input("Quelle type cherchez vous ? \n")
                                print(f"Voici la trouvaille : {bc.recherche_activite_dichotomique(paranom, parajour ,paratype ,bc.charger_activites(('./PythonSEA/Bilan Carbone mystérieux-20241002/emission.csv')))}\n")
                            except:
                                print("L'une des informations que vous avez rentrer est fallacieuse ")
                    else:
                        try:
                            paranom = input("Quelle nom cherchez vous ? \n")
                            parajour = input("Quelle date cherchez vous ?"+"\n"+'format: "anne-mm-jj"\n') 
                            paratype = input("Quelle type cherchez vous ? \n")                
                            print(f"Voici la trouvaille : {bc.recherche_activite_dichotomique(paranom, parajour ,paratype ,bc.charger_activites(('./PythonSEA/Bilan Carbone mystérieux-20241002/emission.csv')))}\n")
                        except:
                            print("L'une des informations que vous avez rentrer est fallacieuse ")

                if repinfo == 6:
                    if len(saved) != 0:
                        question = input("voulez vous utiliser l'une de vos liste[Y/N]"+"\n" "si vous repondez [N]on nous allons utiliser la grande liste"+"\n")
                        if question == "Y":
                            cle = input("quelle liste voulez vous mettre \n")
                            for keys, valeur in saved.items():
                                if cle == keys:
                                    valoc = valeur
                            print(f"Voici toutes les personnes de l'activité : {bc.liste_des_personnes(valoc)}")
                        if question == "N":
                            print(f"Voici toutes les personnes de l'activité : {bc.liste_des_personnes(bc.charger_activites('./PythonSEA/Bilan Carbone mystérieux-20241002/emission.csv'))}")
                    else:
                        print(f"Voici toutes les personnes de l'activité : {bc.liste_des_personnes(bc.charger_activites('./PythonSEA/Bilan Carbone mystérieux-20241002/emission.csv'))}")
                if repinfo == 7:
                    if len(saved) != 0:
                        question = input("voulez vous utiliser l'une de vos liste[Y/N]"+"\n" "si vous repondez [N]on nous allons utiliser la grande liste"+"\n")
                        if question == "Y":
                            cle = input("quelle liste voulez vous mettre \n")
                            for keys, valeur in saved.items():
                                if cle == keys:
                                    valoc = valeur
                            print(f"le cumul temps total est de {cle}: {bc.cumul_temps_activite(valoc,bc.co2_minute)} minutes")
                        if question == "N":
                            print(f"Voici le cumul de temps total : {bc.cumul_temps_activite(bc.charger_activites('./PythonSEA/Bilan Carbone mystérieux-20241002/emission.csv'), bc.co2_minute)} m")
                    else:
                        print(f"Voici le cumul de temps total : {bc.cumul_temps_activite(bc.charger_activites('./PythonSEA/Bilan Carbone mystérieux-20241002/emission.csv'), bc.co2_minute)} m")
                if repinfo == 8:
                    if len(saved) != 0:
                        question = input("voulez vous utiliser l'une de vos liste[Y/N]"+"\n" "si vous repondez [N]on nous allons utiliser la grande liste"+"\n")
                        if question == "Y":
                            cle = input("quelle liste voulez vous mettre \n")
                            paratype = input("quelle type voulez vous cherchez en premier ?(mettez un type qui va de 1 à 4) \n")
                            for keys, valeur in saved.items():
                                if cle == keys:
                                    valoc = valeur
                            print(f"la première date retourner dans votre liste {cle} est {bc.premiere_apparition_type(valoc, paratype)}")
                        if question == "N":
                            paratype = input("quelle type voulez vous cherchez en premier ?(mettez un type qui va de 1 à 4) \n")
                            print(f"la première date retourner de votre liste est {bc.premiere_apparition_type(bc.charger_activites('./PythonSEA/Bilan Carbone mystérieux-20241002/emission.csv'), paratype)}")
                    else :
                        paratype = input("quelle type voulez vous cherchez en premier ?(mettez un type qui va de 1 à 4) \n")
                        print(f"la première date retourner de votre liste est {bc.premiere_apparition_type(bc.charger_activites('./PythonSEA/Bilan Carbone mystérieux-20241002/emission.csv'), paratype)}")
                if repinfo == 9:
                    if len(saved) != 0:
                        question = input("voulez vous utiliser l'une de vos liste[Y/N]"+"\n" "si vous repondez [N]on nous allons utiliser la grande liste"+"\n")
                        if question == "Y":
                            cle = input("quelle liste voulez vous mettre \n")
                            paraindexe = int(input(f"quelles est l'indexe que vous voulez mettre (va de 1 à 4)? \n")) -1
                            if paraindexe == 0:
                                critero = input("quelle est le nom que vous voulez mettre ?\n")
                            elif paraindexe == 1 :
                                critero = input("quelle est la date que vous voulez mettre ?(anne-mm-jj)\n")
                            elif paraindexe == 2:
                                critero = input("quelle est la consomation que vous voulez mettre ?\n")
                            elif paraindexe == 3:
                                critero = input("quelle est le type que vous voulez mettre ?(de 1 à 4)\n")
                            else :
                                print("mettre une valeur entre 1 à 4 svp")
                            for keys, valeur in saved.items():
                                if cle == keys:
                                    valoc = valeur
                            try :
                                print("Voici ce que vous cherchez : ",bc.filtre(valoc,paraindexe,critero))
                            except :
                                print("Mettre un indexe entre 1 ou 4 svp")
                            varloc = bc.filtre(valoc,paraindexe,critero)
                            listYN = input("Voulez vous sauvgarder les information ? [Y/N]"+"\n")
                            if listYN == "N":
                                pass 
                            elif listYN == "Y":
                                nomlist = input("donner un nom a donner à la variable"+"\n")
                                saved[nomlist] = varloc
                                print("Jusqu'à la fin de votre session, le nom de la liste se nomera " + nomlist)
                            else:
                                print("réponse par Y pour Oui et N pour Non")
                        if question == "N":
                            paraindexe = int(input(f"quelles est l'indexe que vous voulez mettre (va de 1 à 4)? \n")) -1
                            if paraindexe == 0:
                                critero = input("quelle est le nom que vous voulez mettre ?\n")
                            elif paraindexe == 1 :
                                critero = input("quelle est la date que vous voulez mettre ?(anne-mm-jj)\n")
                            elif paraindexe == 2:
                                critero = input("quelle est la consomation que vous voulez mettre ?\n")
                            elif paraindexe == 3:
                                critero = input("quelle est le type que vous voulez mettre ?(de 1 à 4)\n")
                            else :
                                print("mettre une valeur entre 1 à 4 svp")
                            try :
                                print("Voici ce que vous cherchez : ", bc.filtre(bc.charger_activites('./PythonSEA/Bilan Carbone mystérieux-20241002/emission.csv'),paraindexe,critero))
                            except :
                                print("Mettre un indexe entre 1 ou 4 svp")
                            listYN = input("Voulez vous sauvgarder les information ? [Y/N]"+"\n")
                            varloc = bc.filtre(bc.charger_activites('./PythonSEA/Bilan Carbone mystérieux-20241002/emission.csv'),paraindexe,critero)
                            if listYN == "N":
                                pass 
                            elif listYN == "Y":
                                nomlist = input("donner un nom a donner à la variable"+"\n")
                                saved[nomlist] = varloc
                                print("Jusqu'à la fin de votre session, le nom de la liste se nomera " + nomlist)
                            else:
                                print("réponse par Y pour Oui et N pour Non")
                    else:
                        paraindexe = int(input(f"quelles est l'indexe que vous voulez mettre (va de 1 à 4)? \n")) -1
                        if paraindexe == 0:
                            critero = input("quelle est le nom que vous voulez mettre ?\n")
                        elif paraindexe == 1 :
                            critero = input("quelle est la date que vous voulez mettre ?(anne-mm-jj)\n")
                        elif paraindexe == 2:
                            critero = input("quelle est la consomation que vous voulez mettre ?\n")
                        elif paraindexe == 3:
                            critero = input("quelle est le type que vous voulez mettre ?(va de 1 à 4)\n")
                        else :
                            print("mettre une valeur entre 1 à 4 svp")
                        try :
                            print("Voici ce que vous cherchez : ", bc.filtre(bc.charger_activites('./PythonSEA/Bilan Carbone mystérieux-20241002/emission.csv'),paraindexe,critero))
                        except  :
                            print("Mettre un indexe entre 1 ou 4 svp ")
                        varloc = bc.filtre(bc.charger_activites('./PythonSEA/Bilan Carbone mystérieux-20241002/emission.csv'),paraindexe,critero)
                        listYN = input("Voulez vous sauvgarder les information ? [Y/N]"+"\n")
                        if listYN == "N":
                            pass 
                        elif listYN == "Y":
                            nomlist = input("donner un nom a donner à la variable"+"\n")
                            saved[nomlist] = varloc
                            print("Jusqu'à la fin de votre session, le nom de la liste se nomera " + nomlist)
                        else:
                            print("réponse par Y pour Oui et N pour Non")
                if repinfo == 10:
                    if len(saved) != 0:
                        question = input("voulez vous utiliser l'une de vos liste[Y/N]"+"\n" "si vous repondez [N]on nous allons utiliser la grande liste"+"\n")
                        if question == "Y":
                            cle = input("quelle liste voulez vous mettre \n")
                            for keys, valeur in saved.items():
                                if cle == keys:
                                    valoc = valeur
                            print(f"La plus longue suite de consomation décroissante est {bc.plus_longue_periode_emmissions_decroissantes(valoc)}")
                        elif question == "N":
                            print(f"La plus longue suite de consomation décroissante est {bc.plus_longue_periode_emmissions_decroissantes(bc.charger_activites('./PythonSEA/Bilan Carbone mystérieux-20241002/emission.csv'))}")
                    else:
                        print(f"La plus longue suite de consomation décroissante est {bc.plus_longue_periode_emmissions_decroissantes(bc.charger_activites('./PythonSEA/Bilan Carbone mystérieux-20241002/emission.csv'))}")
                if repinfo == 11:
                    if len(saved) != 0:
                        question = input("voulez vous utiliser l'une de vos liste[Y/N]"+"\n" "si vous repondez [N]on nous allons utiliser la grande liste"+"\n")
                        if question == "Y":
                            cle = input("quelle liste voulez vous mettre \n")
                            for keys, valeur in saved.items():
                                if cle == keys:
                                    valoc = valeur
                            if bc.est_bien_triee(valoc) == True:
                                print(f"Votre liste {cle} est bien trier!")
                            else:
                                print(f"Votre liste {cle} n'est pas trier! \n ne l'utilisez pas sur des options qui demande une liste triée! \n si vous voulez la trier! faite la trier! en choisiant l'option trier!")
                        if question == "N":
                            print("La grande liste est déjà bien trier")
                    else:
                        print("La grande liste est déjà trier, enregistrer une liste et faite la passer ici")
                if repinfo == 12:
                    if len(saved) != 0:
                        question = input("voulez vous utiliser l'une de vos liste[Y/N]"+"\n" "si vous repondez [N]on nous allons utiliser la grande liste"+"\n")
                        if question == "Y":
                            cle = input("quelle liste voulez vous mettre \n")
                            for keys, valeur in saved.items():
                                if cle == keys:
                                    valoc = valeur
                            print(f"voici la liste de type de votre liste {cle} : {bc.liste_des_types(valoc)}")
                        if question == "N":
                            print(f"voici la liste de type : {bc.liste_des_types(bc.charger_activites('./PythonSEA/Bilan Carbone mystérieux-20241002/emission.csv'))}")
                    else:
                        print(f"voici la liste de type : {bc.liste_des_types(bc.charger_activites('./PythonSEA/Bilan Carbone mystérieux-20241002/emission.csv'))}")
                if repinfo == 13:
                        paranom = input("Quelle nom cherchez vous ? \n")
                        parajour = input("Quelle jour cherchez vous ?"+"\n"+'format: "anne-mm-jj"\n') 
                        paratype = input("Quelle type cherchez vous ? \n") 
                        try :                  
                            print("l'activité de ce profile est de ",f"{bc.temps_activite(bc.recherche_activite_dichotomique(paranom, parajour ,paratype ,bc.charger_activites(('./PythonSEA/Bilan Carbone mystérieux-20241002/emission.csv'))),bc.co2_minute)} minutes")
                        except:
                            print("Vous avez mal tapper les informations de la liste!!")
                if repinfo == 14: 
                    paranom = input("Quelle nom cherchez vous ? \n")
                    parajour = input("Quelle jour cherchez vous ?"+"\n"+'format: "anne-mm-jj"\n') 
                    paratype = input("Quelle type cherchez vous ? \n") 
                    try :
                        print("l'année du profile est de ",bc.annee(bc.recherche_activite_dichotomique(paranom, parajour ,paratype ,bc.charger_activites(('./PythonSEA/Bilan Carbone mystérieux-20241002/emission.csv')))))
                        #je suis au courant que l'utilisateur tappe déjà l'année pour chercher ça mais pour l'instant j'ai pas meilleur solution
                    except:
                        print("veuillez tappez correctement les information \n quoi ?! vous pouvez pas mettre l'année parceque c'est justement ce que vous cherchez ?")
                if repinfo == 15:
                    paranom = input("Quelle nom cherchez vous ? \n")
                    parajour = input("Quelle jour cherchez vous ?"+"\n"+'format: "anne-mm-jj"\n') 
                    paratype = input("Quelle type cherchez vous ? \n") 
                    try :
                        print("l'année et le mois du profile est de ",bc.annee_mois(bc.recherche_activite_dichotomique(paranom, parajour ,paratype ,bc.charger_activites(('./PythonSEA/Bilan Carbone mystérieux-20241002/emission.csv')))))
                        #je suis au courant que l'utilisateur tappe déjà l'année et le mois pour chercher ça mais pour l'instant j'ai pas meilleur solution
                    except:
                        print("veuillez tappez correctement les information \n quoi ?! vous pouvez pas mettre l'année ni le mois parceque c'est justement ce que vous cherchez ?")
                if repinfo == 16:
                    if len(saved) != 0:
                        question = input("voulez vous utiliser l'une de vos liste[Y/N]"+"\n" "si vous repondez [N]on nous allons utiliser la grande liste"+"\n")
                        if question == "Y":
                            cle = input("quelle liste voulez vous mettre \n")
                            for keys, valeur in saved.items():
                                if cle == keys:
                                    valoc = valeur
                            print(f"voici la consomation total de co2 de la liste : {cle} : {bc.cumul_emmissions(valoc)} g")
                        if question == "N":
                            print(f"voici la consomation total de co2 de la liste {bc.cumul_emmissions(bc.charger_activites('./PythonSEA/Bilan Carbone mystérieux-20241002/emission.csv'))} g")
                    else:
                        print(f"voici la consomation total de co2 de la liste  {bc.cumul_emmissions(bc.charger_activites('./PythonSEA/Bilan Carbone mystérieux-20241002/emission.csv'))} g")
                if repinfo == len(liste_info):
                    quitterinfo = True
                input("Appuyer sur Entrée pour continuer")
        if rep == 2:
            if len(saved) == 0:
                print("enregistrer des listes d'abord")
            else:
                nomfic = input("Comment voulez vous appeler le fichier?"+"\n")
                kle = input("Quelle liste voulez vous mettre ?"+"\n")
                for keys,valeur in saved.items():
                    if kle == keys:
                        bc.sauver_activites(f'./PythonSEA/Bilan Carbone mystérieux-20241002/{nomfic}.csv', valeur)           
        if rep == 3:
            print("Voici les listes sauvegardées :")
            print(saved.keys())
            question = input("Voulez vous le contenu de votre liste ?[Y/N]"+"\n")
            if question == "Y":
                for key,valeur in saved.items():
                    question2 = input("quelle liste voulez vous savoir la valeur de ?"+"\n"+"appuyer sur entrer pour passer (pour que le nom de la liste qui vous intéresse coincide avec sont indexe"+ "\n"+ "par exemple si la liste qui vous interesse se trouve a la 3 ème place appuyer sur entrer 2 fois et écrivez sont nom)"+"\n")
                    if question2 == key :
                        print(valeur)
                        print(f"voici le contenu de votre liste {question2}")
                    else:
                        print("aucune liste de ce nom")
            elif question == "N":
                pass
        if rep == 4:
            print("Il y'a plusieurs étapes pour pouvoir plainement utiliser le programme:\n d'abord faite enregistrer des listes grâce au fichier CSV fourni(contenant toutes les informations), les options qui propose de sauvgarder vos listes  sont marquer d'une étoile '*' \n cela va créée une mémoire dynamique qui contient votre liste (grâce au dictionnaire), à noter que vous pouvez aussi nommer les listes comme vous le shouaitez \n ensuite une fois que avez enregistrer des listes vous pourrez les manipuler (il vous sera demander si oui ou non vous voulez utilser l'une de vos listes pour lancer une option, si vous repondez non ça va lancer le programme avec le fichier CSV), \n ensuite quand vous aurez fini, revenez dans le menu principale pour sauvgarder vos listes en fichiers CSV (fichier CSV que vous pouvez nommer à votre guise)")
        if rep == len(liste_options):
            quitter = True
        input("Appuyer sur Entrée pour continuer")
    print("Merci au revoir!")

#appel de fonction
programme_principal() 