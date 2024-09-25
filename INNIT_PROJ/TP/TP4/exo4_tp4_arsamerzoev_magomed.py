    #Travaille fait par ARSAMERZOEV Magomed de la i11A

def trv_mot(liste, lettre):
    """fonction qui donne une liste de mots en fonction de sa première lettre  
    Arg :
        liste(list) : liste de mots
        lettre(str) : lettre 
    Return :
        (list) : liste de tout le mots qui commence par la lettre, lettre.
    """
    listset = []
    #listset aura une liste vide
    #i sera égale à la longueur de liste pour chaque itération de boucle 
    for i in range(len(liste)):
        for carac in liste[i] :
            if lettre  != carac[0] :
                break#J'ai trouver cette fonction sur internet et elle permet de sauver un peu de temps de calcul, par exemple je n'ai pas envie qu'elle continue après la première lettre donc je break
            else :
                listset.append(liste[i])
                break
    return listset 

def test_trv_mot():
    assert trv_mot(["hello","priviet","shalom","salut","salamalekum","selemat-pagi"],"s") == ["shalom","salut","salamalekum","selemat-pagi"]
    assert trv_mot(["hello","priviet","shalom","salut","salamalekum","selemat-pagi"],"z") == []
    assert trv_mot(["hello","priviet","shalom","salut","salamalekum","selemat-pagi"],"p") == ["priviet"]
    assert trv_mot(["z-le","z-programme","z-est","pas","z-bon"],"z") == ["z-le","z-programme","z-est","z-bon"]