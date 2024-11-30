def sort_array(source_array):
    dico = {}
    i=0
    while i < len(source_array):
        if source_array[i]%2 == 1:
            dico[i]= source_array[i]
        i+=1
    dico2 = dict(sorted(dico.items(), key = lambda val : val[1] )) #found this by searching tbh
    for j in range(len(source_array)):
        if source_array[j]%2 == 1:
            for value in dico2.values():
                source_array[j] = value
    for key in dico2.items:
        print(key) 
    return source_array 
    