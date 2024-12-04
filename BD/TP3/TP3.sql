-- @ SCRIPTS/CreateANDDropTables-Voyages
-- @ SCRIPTS/instanceVOYAGES

drop table RESERVATIONS;
drop table CLIENTS;
drop table VOYAGES;

create table CLIENTS 
(Id Number(4)  primary key, 
Nom VarChar2(20),  
Prenom  VarChar2(20),
Ville Varchar2(20));

create table VOYAGES
(Code Varchar2(6) primary key,
VilleDepart VarChar2(30),
VilleArrivee VarChar2(30),
Depart Date,
Retour Date,
Prix Number(8,2));


create table RESERVATIONS (
Id Number(4) , 
Code Varchar2(6),
DateReserv Date,
foreign key (Id) references CLIENTS(Id) on delete cascade,
foreign key (Code) references VOYAGES (Code) on delete cascade);
------------------------------------------------------------------------
insert into Clients values ( 1, 'Dupont', 'Jean', 'Orleans');
insert into Clients values ( 2, 'Durand', 'Paul', 'Orleans');
insert into Clients values ( 3, 'Martin', 'Pierre', 'Paris');
insert into Clients values ( 4, 'Auger', 'Marcel', 'Paris');
insert into Clients values ( 5, 'Smith', 'Peter', 'Londres');
insert into Clients values ( 6, 'Barnes', 'Jane', 'Berlin');
insert into Clients values ( 7, 'Freud', 'Florian', 'Berlin');

insert into Voyages values ('V100', 'Paris', 'Amsterdam',  to_date('01-08-2019-10:30','DD-MM-YYYY-HH24:MI'), to_date('07-08-2019-14:30','DD-MM-YYYY-HH24:MI'),200.00);
insert into Voyages values ('V200', 'Paris', 'Rio de Janeiro',  to_date('01-12-2019-11:30','DD-MM-YYYY-HH24:MI'), to_date('07-12-2019-16:30','DD-MM-YYYY-HH24:MI'),2000.00);
insert into Voyages values ('V300', 'Prague', 'Amsterdam',  to_date('01-10-2019-8:30','DD-MM-YYYY-HH24:MI'), to_date('10-08-2019-15:30','DD-MM-YYYY-HH24:MI'),300.00);
insert into Voyages values ('V140', 'Paris', 'Amsterdam',  to_date('01-11-2019-10:30','DD-MM-YYYY-HH24:MI'), to_date('07-11-2019-14:30','DD-MM-YYYY-HH24:MI'),100.00);
insert into Voyages values ('V400', 'Lisbonne', 'Madrid',  to_date('01-03-2020-12:30','DD-MM-YYYY-HH24:MI'), to_date('07-03-2020-18:30','DD-MM-YYYY-HH24:MI'),400.00);
insert into Voyages values ('V500', 'Paris', 'Madrid',  to_date('01-04-2020-10:30','DD-MM-YYYY-HH24:MI'), to_date('07-04-2020-20:30','DD-MM-YYYY-HH24:MI'),300.00);
insert into Voyages values ('V600', 'Berlin', 'Madrid',  to_date('01-05-2020-10:30','DD-MM-YYYY-HH24:MI'), to_date('07-05-2020-20:30','DD-MM-YYYY-HH24:MI'),300.00);


insert into Reservations values (6, 'V100', to_date('01-07-2019-18:15','DD-MM-YYYY-HH24:MI'));
insert into Reservations values (1, 'V100', to_date('01-06-2019-8:15','DD-MM-YYYY-HH24:MI'));
insert into Reservations values (1, 'V200', to_date('01-05-2019-21:00','DD-MM-YYYY-HH24:MI'));
insert into Reservations values (1, 'V400', to_date('01-11-2019-18:30','DD-MM-YYYY-HH24:MI'));
insert into Reservations values (2, 'V400', to_date('01-11-2019-21:30','DD-MM-YYYY-HH24:MI'));
insert into Reservations values (3, 'V140', to_date('01-06-2019-9:25','DD-MM-YYYY-HH24:MI'));
insert into Reservations values (4, 'V300', to_date('01-05-2019-12:00','DD-MM-YYYY-HH24:MI'));
insert into Reservations values (3, 'V100', to_date('01-05-2019-19:25','DD-MM-YYYY-HH24:MI'));
-- CLIENTS [Id, Nom, Prenom, Ville]
-- VOYAGES [Code, VilleDepart, VilleArrivee, Depart, Retour, Prix]
-- RESERVATIONS [Id, Code, DateReserv]

-- 1. Lister les destinations propos´ees `a partir de Paris
select VilleArrivee
from VOYAGES 
where VilleDepart='Paris';

-- 2. Lister tous les voyages pour Amsterdam.
select * 
from VOYAGES
where VilleArrivee='Amsterdam';

-- 3. Lister les villes de d´epart, les dates et les heures de d´epart pour tous les voyages pour amster
select VilleDepart,Depart 
from VOYAGES
where VilleArrivee='Amsterdam';

-- 4. Lister des noms des clients ayant une r´eservation en informant leur destination et le prix du voyage. La r´eponse est en ordre alphab´etique du nom et un ordre d´ecroissante de prix.
select Nom, VilleArrivee,Prix
from CLIENTS natural join VOYAGES natural join RESERVATIONS
order by Nom, Prix desc ; 

-- 5. Donner les clients qui habitent dans la ville de d´epart de leur voyage. Indiquer le nom du client, la ville de d´epart et le code du voyage.
select Nom,VilleDepart,Code
from CLIENTS natural join RESERVATIONS natural join VOYAGES
where Ville=VilleDepart;

-- 6. Ins´erer dans la base au moins un nouveau voyage qui devra avoir lieu dans un an.
-- insert into VOYAGES values('V666', 'Pyongyang', 'Seoul',  to_date('01-05-2021-10:30','DD-MM-YYYY-HH24:MI'), to_date('07-05-2021-20:30','DD-MM-YYYY-HH24:MI'),300.00);
insert into VOYAGES values('V777', 'Gensokyo', 'NYC',  to_date('01-02-2025-10:30','DD-MM-YYYY-HH24:MI'), to_date('03-03-2025-20:30','DD-MM-YYYY-HH24:MI'),300.00);

-- 7. Pour tous les vols dont le d´epart est dans plus de 3 mois, lister les villes de d´epart et arriv´ee, les dates et les heures de d´epart. Pr´esenter la liste dans l’ordre chronologique de d´epar
select VilleDepart,VilleArrivee,to_char(Depart,'DD-MM-YYYY-HH24:MI') as Depart
from VOYAGES
where Depart > to_date('01-01-2025-10:30','DD-MM-YYYY-HH24:MI');
-- where months_between(sysdate,depart) > 3 

-- 8 Quelles sont les villes concern´ees par les voyages. Pr´esenter le r´esultat dans une relation avec un seul attribut : Villes.
select Ville
from CLIENTS natural join RESERVATIONS natural join VOYAGES
where 

-- 9. Lister les clients qui n’habitent pas Paris.
select * 
from CLIENTS
where Ville!='Paris';

-- 10. Lister les clients qui partent de Paris, mais qui n’habitent pas Paris
select * 
from CLIENTS natural join RESERVATIONS natural join VOYAGES
where Ville != VilleDepart and VilleDepart='Paris';

-- 11.Trouver les clients qui n’ont aucune reservation.
-- select * 
-- from CLIENTS 
-- where ID not in (select ID from Reservations);
select id, nom,Prenom,ville
from CLIENTS
MINUS 
select id, nom,Prenom,ville 
from clients natural join reservations;
-- 12 Voyages qui ne font pas objet d’une r´eservation.
select * 
from VOYAGES
where Code not in (select Code from RESERVATIONS);

-- 13 Clients qui partent de Paris, mais qui vont uniquement a Amsterdam (´eventuellement plusieurs fois). Aucun voyage vers une autre destination.
select * 
from CLIENTS natural join RESERVATIONS natural join VOYAGES
where VilleDepart='Paris' and VilleArrivee='Amsterdam';

-- 14 Clients qui vont `a Amsterdam et `a Rio de Janeiro
select Nom
from CLIENTS natural join Reservations natural join VOYAGES
where VilleArrivee='Rio de Janeiro'
intersect 
select Nom
from CLIENTS natural join Reservations natural join VOYAGES
where VilleArrivee='Amsterdam';
-- 15. Clients qui vont `a Amsterdam ou `a Rio de Janeiro
select Nom
from CLIENTS natural join Reservations natural join VOYAGES
where VilleArrivee='Rio de Janeiro'
union
select Nom
from CLIENTS natural join Reservations natural join VOYAGES
where VilleArrivee='Amsterdam';
-- 16. Couples de clients habitant la mˆeme ville. Indiquer la ville en question
select c1.Nom,c2.Nom,c1.Ville
from Clients c1, Clients c2 
where c1.ville = c2.ville and c1.Nom < c2.Nom ;
-- 17 Couples de (code) voyages ayant le mˆeme prix. Indiquer le prix en question
select c1.Code, c2.Code , c1.prix 
from Voyages c1, Voyages c2
where c1.prix = c2.prix and c1.code < c2.code;
-- 18 Clients ayant au moins deux reservations
select c1.Nom
from RESERVATIONS r1, RESERVATIONS r2, CLIENTS c1
where r1.ID = c1.ID and r2.ID = c1.ID and r1.code != r2.code and r1.code < r2.code ; 
