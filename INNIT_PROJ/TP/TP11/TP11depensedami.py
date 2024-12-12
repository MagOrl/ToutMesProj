DepenseDuWE= {'Pierre':[12,70,10],'Paul':[100],'Marie':[15],'Anna':[]}
def affiche_bilan_financier(week_end):
    somme = 0 
    for ami in week_end :
        somme += sum(week_end[ami])
    dico = {}
    for amidepens in week_end:
        dico[amidepens] = somme/len(week_end) - sum(week_end[amidepens])  
    
    for personne in dico:
        if dico[personne] < 0:
            print(f"{personne} doit recevoir {abs(dico[personne])}")
        if dico[personne] > 0: 
            print(f"{personne} doit payé {dico[personne]}")
    return dico


print(affiche_bilan_financier(DepenseDuWE))
        