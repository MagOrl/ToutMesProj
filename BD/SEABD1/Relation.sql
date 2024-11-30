---------------------------------------------- Insertion de valeurs ------------------------------------------------
insert into Reserve values ('R001', 'Reserve A', 'Paris', 'France', 1234567890, 'jeandupont@gmail.com', 'Jean Dupont');
insert into Reserve values ('R002', 'Reserve B', 'Lyon', 'France', 9876543210, 'mariecurie@yahoo.com', 'Marie Curie');

insert into ForetProtege values (150, 'R001');
insert into ForetProtege values (200, 'R002');

insert into JardinBotanique values ('Jardin Botanique Paris', 'Ministère de l Environnement', '12 Rue de l Écologie', '0102030405', 'R001');
insert into JardinBotanique values ('Jardin Botanique Lyon', 'Université Lyon 1', '45 Avenue de la Nature', '0203040506', 'R002');

insert into Nutriments values (1, 'Azote', 'NH3', 'Minéral');
insert into Nutriments values (2, 'Phosphore', 'PO4', 'Minéral');

insert into NutrimentSubstitus values (1);
insert into NutrimentSubstitus values (2);

insert into Stock values (100, 'R001', 1);
insert into Stock values (150, 'R002', 2);

insert into Emplacement values (1, 'R001');
insert into Emplacement values (2, 'R002');

insert into FicheArosage values (1, 'Goutte à goutte', 50, 'Oui', 'Sec');
insert into FicheArosage values (2, 'Pluie artificielle', 70, 'Non', 'Humide');

insert into Espece values (1, 'Quercus robur', 'Chêne', 'Arbre feuillu de grande taille', 'Résistant à la sécheresse', 1);
insert into Espece values (2, 'Pinus sylvestris', 'Pin sylvestre', 'Conifère de grande taille', 'Adapté aux sols acides', 2);

insert into ZoneGeo values ('Europe');
insert into ZoneGeo values ('Asie');

insert into ZoneOrigine values (1, 'Europe');
insert into ZoneOrigine values (2, 'Asie');

insert into besoin values (1, 'R001');
insert into besoin values (2, 'R002');

insert into Plantes values ('P001', '2024-05-01', 'Vert', 1.5, 1);
insert into Plantes values ('P002', '2023-03-15', 'Bleu', 2.0, 2);

---------------------------------------------- Requètes ----------------------------------------------
-- Savoir tout les attributs de la table Reserve 
SELECT * FROM Reserve;

-- Savoir montrer le nom de la reserve et sa ville d'une reserve française
SELECT NomReserve, VilleReserve 
FROM Reserve
WHERE PaysReserve = 'France';

-- Savoir l'ID de la reserve ansi que sa superficie 
SELECT IdReserve, Superficie
FROM ForetProtege;

-- Savoir l'id de la reserve sa date de plantation ainsi que sa hauteur d'une plante qui mesure plus 1m80
SELECT Idplante, DatePlantation, Hauteur 
FROM Plantes 
WHERE Hauteur > 1.8;

-- Savoir la reserve ainsi que les jardin 
SELECT JardinBotanique.NomOrganisme, Reserve.VilleReserve
FROM JardinBotanique
NATURAL JOIN Reserve;

-- Savoir la reserve et les nutriments 'Azote'
SELECT Reserve.NomReserve, Nutriments.NomNutri
FROM besoin
NATURAL JOIN Reserve
NATURAL JOIN Nutriments
WHERE Nutriments.NomNutri = 'Azote';
--------------------------------------------------------------------------------------------------------
