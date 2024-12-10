#some codewar code I solved me happy :)

"""Pete likes to bake some cakes. He has some recipes and ingredients.
 Unfortunately he is not good in maths. Can you help him to find out, how many cakes he could bake considering his recipes?"""
def cakes(recipe, available):
    seto = set()
    for clef, valeur in recipe.items():
        if clef in available.keys():
            seto.add(available[clef] // valeur)  
        else:
            return 0
    return min(seto)
#first

def HelloName(name):
    
print(HelloName("mago"))
