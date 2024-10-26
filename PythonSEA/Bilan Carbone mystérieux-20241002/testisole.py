
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