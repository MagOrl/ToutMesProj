-- purge recyclebin;

-- set linesize 500;

create table CLIENT(
    codeCl number(10),
    nomCl varchar2(30),
    prenomCl varchar2(30),
    adressCl varchar2(50),
    Email varchar2(30),
    refPtDist number(3)
);

create table ARTICLE(
    refart number(4)

);

insert into client values(12,'Celestin','Maubert','Rue des cramptés','vivi@yahoo.com',3);
