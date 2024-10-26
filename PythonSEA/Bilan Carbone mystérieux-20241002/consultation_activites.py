import bilan_carbone as bc
# Ici vos fonctions dédiées aux interactions
def affichage_menu(liste_options):
    print("+--------------------------------------+")
    print(" Choisi les options que tu désire      |")
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
def indepth(liste_info):
    print("+--------------------------------------+")
    print(" Choisi les infos que tu désire        |")
    print("+--------------------------------------+")
    print("les chiffres dans les paranthèse signifie le nombre de liste que vous avez besoin")
    for i in range(len(liste_info)):
        print(i + 1, "-->", liste_info[i])
def nombreindepth(message, nombremax):
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
    affichage_menu(liste_info)
    return nombreentrer("Entrez votre choix ", len(liste_info))
# Ici votre programme principal
def programme_principal():
    liste_options = ["Recherche d'info",
                     "Sauvgarder les info dans un fichiers CSV",
                     "Voir vos listes sauvgarder", 
                     "Quitter"]
    liste_info =["Recherche par nom(1)",
                 "Teste si 2 liste est bien avant l'autre(2)","Donne le maximum d'une emission(1)",
                 "Fusion de listes(2)","Recherche dichitomique(1)","quitter"]
    saved = {}
    quitter = False 
    quitterinfo = False
    while not quitter:
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
                    else:
                        print("il faut sauvgarder plus de 2 listes")
                if repinfo == 3 :
                    if len(saved) != 0:
                        question = input("voulez vous utiliser l'une de vos liste[Y/N]"+"\n" "si vous repondez [N]on nous allons utiliser la grande liste"+"\n")
                        if question == "Y":
                            clef = input("Quelle liste voulez vous mettre ?")
                            for keys,valeur in saved.items():
                                if clef == keys:
                                    valoc = valeur
                            print(f"la consomation max est {bc.max_emmission(valoc)}")
                        if question == "N":
                            print(f"la consomation max est{bc.max_emmission(bc.charger_activites(('./PythonSEA/Bilan Carbone mystérieux-20241002/emission.csv')))}")
                    else:
                        print(f"la consomation max est{bc.max_emmission(bc.charger_activites(('./PythonSEA/Bilan Carbone mystérieux-20241002/emission.csv')))}")
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
                            saved[nomlist] = varloc
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
                            parajour = input("Quelle jour cherchez vous ?"+"\n"+'format: "anne-mm-jj"\n') 
                            paratype = input("Quelle type cherchez vous ? \n")
                            for keys, valeur in saved.items():
                                if cle == keys:
                                    valoc = valeur
                            print(f"Voici la trouvaille : {bc.recherche_activite_dichotomique(paranom,parajour,paratype,valoc)}\n")
                        if question == "N":
                            paranom =input("Quelle nom cherchez vous ?\n")
                            parajour = input("Quelle jour cherchez vous ?"+"\n"+'format: "anne-mm-jj"\n') 
                            paratype = input("Quelle type cherchez vous ? \n")
                            for keys, valeur in saved.items():
                                if clef == keys:
                                    valoc = valeur
                            print(f"Voici la trouvaille : {bc.recherche_activite_dichotomique(paranom, parajour ,paratype ,bc.charger_activites(('./PythonSEA/Bilan Carbone mystérieux-20241002/emission.csv')))}\n")
                    else:
                        paranom = input("Quelle nom cherchez vous ? \n")
                        parajour = input("Quelle jour cherchez vous ?"+"\n"+'format: "anne-mm-jj"\n') 
                        paratype = input("Quelle type cherchez vous ? \n")
                        for keys, valeur in saved.items():
                            if clef == keys:
                                valoc = valeur                    
                        print(f"Voici la trouvaille : {bc.recherche_activite_dichotomique(paranom, parajour ,paratype ,bc.charger_activites(('./PythonSEA/Bilan Carbone mystérieux-20241002/emission.csv')))}\n")
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
                    question2 = input("quelle liste voulez vous savoir la valeur de ?"+"\n"+"appuyer sur entrer pour passer (pour que le nom de la liste qui vous intéresse coincide avec sont indexe"+ "\n"+ "par exemple si la liste qui vous interesse se trouve a la 3 ème place appuyer sur entrer 3 fois et écrivez sont nom)"+"\n")
                    if question2 == key :
                        print(valeur)
                        print(f"voici le contenu de votre liste {question2}")
                    else:
                        print("aucune liste de ce nom")
            elif question == "N":
                pass

        if rep == len(liste_options):
            quitter = True
        input("Appuyer sur Entrée pour continuer")
    print("Merci au revoir!")

#appel de fonction
programme_principal() 