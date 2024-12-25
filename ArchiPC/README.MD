
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
<br><b>6. </b>Oui le codage des pixels on changer, car à l'offset 32 il y a le nombre de couleur importante utiliser, ici 2 pour rouge et blanc.<br>Le codage RGB des pixels reste le même, il y a un "00" à chaque codage de RGB surement pour indiquer le padding(il est possible que ça soit pour R.G.B.A, A étant alpha, les nuance de gris mais dans ce cas la puisqu'on est en little endian il aurait du être tout devant faisant A.B.G.R), ensuite le 50 et le A0, qui respectivement en décimale donne 80 et 160, sont les valeurs pour pouvoir calculer la taille de la ligne pour 4 octets. 80/160 donnant 1/2, ça fait que un pixel et mit une fois sur deux<br>
<b>7. </b>Pour modifier les pixels rouge en bleu il suffisait d'inverser les 2 octets de droite et de gauche(donc inverser le rouge et bleu)
<img src="images/image copy 5.png"><br>
<b>8. </b>Pour inverser le bleu et le blanc il faut faire de même dans le codage de pixel on remplace FF 00 00 avec FF FF FF pour obtenir le damier inverser.<img src="images/image copy 6.png"><br>
<b>9. </b></p>