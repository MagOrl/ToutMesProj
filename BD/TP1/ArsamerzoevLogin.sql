-- TRAVAILLE FAIT PAR ARSAMERZOEV MAGOMED de la 11A (2024) 


purge recyclebin;

set linesize 500;
-- Creation de TABLE
create table PointDeDistribution(
    refPointDist varchar2(10),
    adressePointDist varchar2(30),
constraint CLEPOINTDIS primary key(refPointDist)
);
create table CLIENT(
    codeCl number(5),
    nomCl varchar2(30),
    prenomCl varchar2(30),
    adressCl varchar2(50),
    Email varchar2(30),
    refPointDist varchar2(10),
constraint CLECLI primary key(codeCl),
constraint PDISTEXIST foreign key(refPointDist) references PointDeDistribution(refPointDist) 
);

create table ARTICLE(
    numart number(4),
    designation varchar2(30),
    prix number(5),
    TVA number(4,2),
    qteStock varchar2(3),
constraint REFART primary key(numart)
);
create table COMMANDE(
    numcom number(3),
    datecom date,
    codeCl number(5),
constraint CLECOM primary key(numcom),
constraint CLIENTEXIST foreign key(codeCl) references CLIENT(codeCl)
);
create table COLIS(
    numcom number(3),
    numcolis number(3),
    indicRetrait varchar2(30),
constraint CLECOLIS primary key (numcolis, numcom),
constraint COMEXIST foreign key(numcom) references COMMANDE(numcom) 
);
create table Expedier(
    numCom number(3),
    numcolis number(3),
    numart number(4),
    qteExd number(3),
    qteAcc number(3),
constraint CLEEXP primary key(numcom,numcolis,numart),
constraint COLISEXIST foreign key(numcolis,numcom) references COLIS(numcolis,numcom)
constraint ARTICLEEXPEXIST foreign key(numart) references ARTICLE(numart)
);
create table CONTENIR(
    numcom number(3),
    numart number(4),
    qtecom number(3),
constraint CLECONTENIR primary key(numcom,numart),
constraint CONTENIRCOMEXIST foreign key(numcom) references COMMANDE(numcom),
constraint ARTICLEEXIST foreign key(numart) references ARTICLE(numart)
);

/** Supprimer mes tables**/
drop table CONTENIR;
drop table Expedier;
drop table COLIS;
drop table COMMANDE;
drop table ARTICLE;
drop table CLIENT;
drop table PointDeDistribution;

-- Insertion Disitrubtion
insert into PointDeDistribution values ('AE2342347', 'Boulevard de la République');
insert into PointDeDistribution values ('AE2347789', 'Rue des Pyramides');
insert into PointDeDistribution values ('AE2355566', 'Place du Marché');

-- Insertion  CLIENT
insert into CLIENT values (888, 'Lemoine', 'Sophie', 'Rue de la paix', 'sophie.lemoine@gmail.com', 'AE2342347');
insert into CLIENT values (999, 'Dupont', 'Jean', 'Avenue des Cramptées', 'jean.dupont@hotmail.com', 'AE2347789');
insert into CLIENT values (1001, 'Dufresne', 'Alice', 'Quartier Latin', 'alice.dufresne@yahoo.com', 'AE2355566');

-- Insertion  ARTICLE
insert into ARTICLE values (1475, 'Smash Bros', 45, 20, 10);
insert into ARTICLE values (9021, 'Figurine', 120, 15, 5);
insert into ARTICLE values (3542, 'CD', 25, 5, 0);

-- Insertion  COMMANDE
insert into COMMANDE values (126, ('10-10-2023'), 888);
insert into COMMANDE values (127, ('15-11-2023'), 999);
insert into COMMANDE values (128, ('25-12-2023'), 1001);

-- Insertion  COLIS
insert into COLIS values (126, 1, 'Livraison standard');
insert into COLIS values (127, 2, 'Livraison express');
insert into COLIS values (128, 3, 'Livraison a domicile');

-- Insertion  Expedier
insert into Expedier values (126, 1, 1475, 3, 3);
insert into Expedier values (127, 2, 9021, 2, 2);
insert into Expedier values (128, 3, 3542, 1, 0);

-- Insertion  CONTENIR
insert into CONTENIR values (126, 1475, 2);
insert into CONTENIR values (127, 9021, 1);
insert into CONTENIR values (128, 3542, 1);

-- Queleque requètes
SELECT numcom, datecom
FROM COMMANDE
WHERE codeCl = 888;

SELECT numart, designation
FROM ARTICLE
WHERE TO_NUMBER(qteStock) = 0;


