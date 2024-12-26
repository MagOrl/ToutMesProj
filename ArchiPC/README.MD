<h1>‎ ‎ ‎ ‎ ‎‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎SAE IMAGE</h1>
<h6>ARSAMERZOEV Magomed 11A</h6>


<h3> A.0 </h3>
<p>L'erreure afficher par display est que la longeur et la taille de l'image ne convienne pas.
la raison est que le premier octet était a 99 au lieux que 9A, mais pour que display affiche correctement l'image il faut que que le première quarter soient initialiser à 0 donc il faut mettre 9A. </p>

<h3> A.1 </h3>
<p> voici le resultat : </p>
<img src="images/image0.png">
<p>mais bon ce résultat ne prouve rien.<br>Pour pouvoir arriver à cela il à fallu modifier le fichier bmp en héxadécimal <img src="images/mosaique.png"> <br> Les premier octets répresente "BM" la signature de bmp, ensuite la taille de l'image ici 4A pour 74 octets ensuite les coordonée de la ou les pixels commence, ici les pixels commence à l'adresse 1A, après 0C réprente la taille de la seconde partie, le 04 04 représente la hauteur et la largeure ici c'est du 4x4, pour le 18 c'est la valeur héxadécimal de 24, car sur pour réprésenter les couleurs RVB chacune des couleurs sont codée sur 1 octet, donc 3, sachant qu'un octet c'est 8 bit il faut faire 3*8 donc 24 donc 18 en héxa <br> Ensuite le reste c'est les pixels qui sont mit en fonction de leurs couleur, puisqu'on on est en little endian on fait bleu vert rouge.
</p>
<h3>A.2</h3>
<p> Pour obtenir ce resultat : <img src="images/image copy.png"> <br> j'ai dû faire passer ce code : <img src="images/image copy 2.png"><br>Donc rien de plus à expliquer car tout à été dit dans la question précédente, j'ai du faire attention de bien tout inverser car je suis en little endian, le vert n'était jamais un problème car il est au milieu.</p>

<h3>A.3</h3>
<p>Après la conversion de mon damier avec imagemagick voici le résultat : <img src="images/image copy 3.png"> <br> 
On peut déjà remarquer que la taille du fichier à naturellement changer, elle est passer à 66(en hexadecimal).<br> 
Le codage des pixels reste le même, c'est à dire du codage RGB mit en little endian donc BGR.<br>
Il y à toujours 24 bits par pixels.<br>
Aucune méthode de compression à été utiliser car dans les octets de l'offset 1E les octets sont à 0 <br> <br>
Pour savoir la taille des données pixels il faut voir à l'offset 22, et ici on voit 30 donc 48 en décimale</p>
 
<h3>A.4</h3>
<p>après conversion on obtient : <img src="images/image copy 4.png"></p>
<p><b>1. </b>À l'octet 1C on peut voir que le nombre de bits par pixel est de 1.
<br><b>2. </b>La taille du fichier est de 16 en décimal on peut voir ça à l'offset 22.<br><b>3. </b>Aucune méthode de compression utiliser car les valeur de l'offset 1E sont à 0<br><b>4 et 5. </b>Les palettes sont codées de manière 2^n ou n est est le nombre de bits par pixels, dans notre cas 1, donc 2¹(ou 2) ce qui reste cohérent car on à que 2 couleur dans notre mosaique.
<br><b>6. </b>Oui le codage des pixels on changer, car à l'offset 32 il y a le nombre de couleur importante utiliser, ici 2 pour rouge et blanc.<br>Le codage RGB des pixels reste le même, il y a un "00" à chaque codage de RGB surement pour indiquer le padding(il est possible que ça soit pour R.G.B.A, A étant alpha, les nuance de gris mais dans ce cas la puisqu'on est en little endian il aurait du être tout devant faisant A.B.G.R), ensuite le 50 et le A0, il faut convertir les valeurs en binaire, pour A0 par exemple ca nous fait 1010 0000 ce qui est exactement le patterne de notre damier, blanc, rouge, blanc, rouge(1 c'est blanc et 0 c'est rouge), Il faut couper 1 octet en deux pour pouvoir répartire les couleurs sur une ligne, 50 donne 1010 0000 en binaire ce qui est encore le patterne de notre damier <br>
<b>7. </b>Pour modifier les pixels rouge en bleu il suffisait d'inverser les 2 octets de droite et de gauche(donc inverser le rouge et bleu)
<img src="images/image copy 5.png"><br>
<b>8. </b>Pour inverser le bleu et le blanc il faut faire de même dans le codage de pixel on remplace FF 00 00 avec FF FF FF pour obtenir le damier inverser. Ou encore remplacer F0 et 50 (si on fait les 2 en même temps on reviens sur le damier de départ)<img src="images/image copy 6.png"><br>
<b>9. </b> Voici le resultat de <b>Image3</b><img src="images/image copy 7.png">Donc en prenant le même raisonnement expliquer dans la question 6, ici pour d'abord avoir une ranger de blanc il faut 1111 donc convertit en héxadécimal ça donne F0 ensuite 2 lignes de rouge donc on met 0 pour les 2 lignes suivantes, après on veut un cadriage de base donc on prend A0<br>
<b>10. </b>Voici une partie de l'image en indexe de couleur ouvert dans un héditeur héxadécimal<img src="images/image copy 8.png"><br>
<b>11. </b>On peut voir le nombre de couleurs dans la palettes à l'adresse 2E, ici 10 converti en binaire 16 donc 2¹⁶ couleurs possible<br>
<b>12. </b> Le Blanc est retrouver en couleur dominante à l'adresse 66 avec FE FE FD reconvertit en RGB et en big endian ca nous donne 253 254 254, donc pas du blanc pur mais du blanc quand même<br>
<b>13. </b>le tableau de pixel commence à l'adresse 76,on peut le voir car c'est la ou s'arrete la définition des couleurs importantes qui se remarque car il 3 octets puis 1 autre octet avec 00, et aussi car visuellement je sais que l'image commence avec du blanc et le fait que CC soient répété met la puce à l'oreille. Mais concrètement la couleur blanche que j'ai répéré auparavant est à la 12ème position (des couleurs importantes) et 12 en héxa se note C, et donc le fait qu'il y est que des ranger de CC fait que ca commence ici.<br>
<b>14. </b>Pour commencer j'ai répéré qu'une des couleurs de bleu était à l'indice 0. Donc pour avoir cette ranger de bleu j'ai juste mit des 0 un peut comme je le sentais et donc voici le résultat<img src="images/image copy 9.png"> et voici ce que ça donne dans un éditeur héxadécimal <img src="images/image copy 10.png"><br>
<b>15.<br> </b><img src="images/image copy 11.png">Visuellement la dimunition de couleur se voit, ici c'est surtout la couleur orange qui à été affecter et queleque nuance de bleu.
<br><img src="images/image copy 12.png">D'un point de vue héxadécimal on voit que les couleurs des palettes on été remplacé par des 0 </p>
<p><h3>A.5</h3><br>
<b>1 et 2. </b>Pour passer de 4 à -4 en héxadécimal voici le calcule que j'ai fait: 4-2⁸ = -252,(4 est la valeur que je veux convertir et 2⁸ sont les bits)je prend la valeur absolue 252, et je converti en héxadécimal donc FC et je rempli le reste avec l'inverse de 0 donc F <br> voici ce que ca donne dans l'interpréteur héxadécimal <img src="images/image copy 13.png"> et voici le résultat :<br><img src="images/image copy 14.png"><br>l'image à donc bien été inverser.<br>
<b>3. </b>Pour cette image la hauter est de 425 car A9 01 en little endian donne 425, 425 - 2¹⁶ = -65 1111, 65 1111 donne FE 57 en héxadécimal, 57 FE en little endian, on remplace les 0 par des F et on est bon, voici la représentation dans un éditeur héxadécimal<img src="images/image copy 15.png"></p>
<p><h3>A.6 </h3>
Voici la représentation dans un éditeur héxadécimal : 
<img src ="images/image copy 16.png"><br>
<b>1. </b>6*16 + 4*16² = 1120, le poid du fichier est de 1120 octets, contre les 74 octets initial.<br>
La raison de ce changement est que la méthode de compréssion RLE fait que quand un certain motif répété la simplifie en mettant un nombre signifiant le nombre de fois que le motif est répété,<b>a la suite</b>, donc dans notre cas ce n'est pas le plus pertinant car on à pas de motif répété à la suite, ca fera qu'on ajoutera plus d'octet que nécessaire.<br>
<b>2. </b>c'est à l'adresse 0x0A ou l'on trouve l'entête de la ou démarre les pixels, ici 36 04, donc 0436, et c'est bien à l'adresse 0x436 qu'on voit apparaître des octets avec des 00 et des 01.
<br><b>3. </b>voici une représentation de la ou les pixels sont représenter: 
<img src="images/image copy 17.png"><br>
Comme je l'ai dit il y'a un chiffre pour représenter le nombre de fois qu'un motif est répété, ici il faut savoir que 0 veut dire rouge et que 1 veux dire blanc car le rouge à été défini en premier et le blanc en deuxième. Ensuite pour lire un pixel il faut prendre 16 bits soit 2 octet, 1 octet pour dire le nombre de répétéition et le 2ème la couleur du pixel. En appliquant cette méthode on peut voir que ca reste cohérent, pour rouge blanc rouge blanc, ca nous fait 1 rouge, 1 blanc, 1 rouge, 1 blanc, 01 00 01 01 01 00 01 00(les 00 00 sont la pour représenter les fin de lignes et le 01 de fin est la pour représenter la fin du bitmap).</p>
<p><h3>A.7</h3>
voici une représentation de l'entête :<img src ="images/image copy 18.png"><br>
<b>1. </b>le poid de l'image est de 1102 octets, donc ici c'est logique que ça soit moins lourd car la compression sera plus utile car on à plusieurs fois des pixels répété, des octets vont donc être économisé, contrairement à l'image 4 qui lui n'avait pas de pixels qui se répétait donc ca utiliser 1 octet pour rien.<br>
<b>2. </b>Voici une représentation sur un éditeur héxadécimal :<img src="images/image copy 19.png"><br>
Donc on commence avec 04 01, ce qui veut dire qu'il y aura 4 pixel de couleur blanche(rappel : 0 rouge 1 blanc) suivit d'un double 00 marquant la fin de la ligne. ensuite 04 00 qui veut dire 4 pixel rouge, 2 fois, ensuite 01 01 donc 1 pixel blanc, 01 00 1 pixel rouge, et ainsi du suite. 
</p>
<h3>A.8</h3>
<p>voici la réprésentation héxadécimal du résultat attendu : <img src="images/image copy 20.png"><br>
donc ici j'ai du d'abord enlever le 04 01 qui signifiat 4 pixel blanc, pour ensuite faire 02 01 pour dire que je veux 2 pixel blanc, 01 00 pour 1 pixel rouge et enfin 01 01 pour 1 pixel blanc(je touche pas au reste). Puisque les modifications ont rendu l'image plus lourde je n'ai pas oublier de mettre la bonne taille dans l'entête.</p>
<h3>A.9</h3>
<p>Pour arrive rau résultat attendu j'ai du d'ab</p>