<h3> A.0 </h3>
<p>L'erreure afficher par display est que la longeur et la taille de l'image ne convienne pas.
la raison est que le premier octet était a 99 au lieux que 9A, mais pour que display affiche correctement l'image il faut que que le première quarter soient initialiser à 0 donc il faut mettre 9A. </p>

<h3> A.1 </h3>
<p> voici le resultat</p>
<img src="image0.png">
<p>pour ce code </p>
O