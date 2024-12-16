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


-- 1. Trouver les clients n’ayant r ́eserv ́e aucun voyage.
select id, Nom
from CLIENTS
where id not in (select id from RESERVATIONS);

-- 2. Trouver les voyages n’ayant  ́et ́e r ́eserv ́es par aucun client.
select Code, VilleArrivee
from VOYAGES
where Code not in ( select code from RESERVATIONS);
-- 3. Trouver les noms des clients ayant r ́eserv ́e seulement un voyage (une seule r ́eservation).
select Nom 
from CLIENTS natural join Reservations
where id not in (select c1.Id from Reservations c1, Reservations c2 where c1.code != c2.code and c1.id = c2.id) ;

-- 4. Codes des voyages les plus chers.
select Code, Prix
from Voyages 
where prix >= ALL(select prix from VOYAGES);

-- 5. Codes des voyages les moins chers.
select Code, Prix
from Voyages 
where prix <= ALL(select prix from VOYAGES);

-- 6. Code, trajet et prix des voyages pour lesquels il existe au moins un autre voyage pour le meme parcours, c’est-`a-dire, ayant les mˆemes villes d’arrivee et de d ́epart.
select v1.code,v1.VilleDepart,v1.VilleArrivee,v1.prix 
from Voyages v1 
where exists (select * from voyages v2 where v1.code != v2.code and v1.VilleArrivee = v2.VilleArrivee and v1.VilleDepart = v2.VilleDepart );
--7. Code, trajet et prix des voyages pour lesquels il existe une unique option. Autrement dit, les voyages pour lesquels il n’existe pas un autre voyage pour le mˆeme parcours, c’est-`a-dire, ayant les mˆemes villes d’arriv ́ee et de d ́epar
select v1.code,v1.VilleDepart,v1.VilleArrivee,v1.prix 
from Voyages v1 
where not exists (select * from voyages v2 where v1.code != v2.code and v1.VilleArrivee = v2.VilleArrivee and v1.VilleDepart = v2.VilleDepart );
--8. Trouver les clients qui ont r ́eserv ́e tous les voyages `a Amsterdam. Autrement dit : trouvez les clients (id) pour lesquels il n’existe pas un voyage `a Amsterdam qu’ils n’ont pas reserve.
select nom
from Clients
where not exists (select code FROM voyages where VilleArrivee='Amsterdam')
minus 
select code from reservations where reservations.id = Clients.id ; 

-- 9. Trouver les voyages qui ont  ́et ́e r ́eserv ́es par tous les clients parisiens. 
select Nom, Ville,VilleDepart, VilleArrivee 
from clients natural join reservations natural join VOYAGES
where Ville ='Paris' ;