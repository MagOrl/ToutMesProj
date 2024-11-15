-- purge recyclebin;

-- set linesize 500;
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
-- Insertion 
insert into PointDeDistribution('AE2312421','Avenue Charle de Gaulle');
insert into PointDeDistribution('AE2319832','Avenue Napoleon Bonaparte');
insert into PointDeDistribution('AE2332345',"Avenue Jeanne d'Arc");

insert into client values(666,'Celestin','Maubert','Rue des cramptés','vivi@yahoo.com','AE2312421');
insert into client(777,'Gecko','Erwan','Rue de la sainte fleur','gekoewan@gmail.com','AE2319832');
insert into client(1092,'Kero','Suwako','Boulvard du Crapeau','AE2332345');


