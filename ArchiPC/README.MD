A.0
L'erreure afficher par display est que la longeur et la taille de l'image ne convienne pas.
la raison est que le premier octet était a 99 au lieux que 9A, mais pour que display affiche correctement l'image il faut que que le première quarter soient initialiser à 0 donc il faut mettre 9A. 

A.1
