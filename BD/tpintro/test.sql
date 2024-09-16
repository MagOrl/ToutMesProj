drop table Posseder;
drop table Personne;
drop table Voiture;


create table Personne (
    Id number(5),
    Prenom varchar2(20),
    Nom varchar2(20),
    Sexe varchar2(1),
    Rue varchar2(20),
    Num number(2),
    Ville varchar2(10),
    nomV varchar2(10),
    anneeV number(4),
    constraint keypersonne PRIMARY KEY (Id)
    
);
create table Voiture( 
    Immat varchar2(10),
    Marque varchar2(10),
    Couleur varchar2(10),
    Modele varchar2(10),
    Energie varchar2(10),
    constraint keyvoiture PRIMARY KEY (Immat)

);

create table Posseder(
    Id number(5),
    Immat varchar2(10),
    constraint FKPersonne FOREIGN KEY (Id) REFERENCES Personne (Id),
    constraint FKVoiture FOREIGN KEY (Immat) REFERENCES Voiture(Immat);
);

