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
select c1.Nom
from CLIENTS c1, 