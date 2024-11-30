create table Reserve(
    IdReserve Varchar2(5) , 
    NomReserve Varchar2(15),
    VilleReserve Varchar2(15),
    PaysReserve Varchar2(15),
    TelReserve Number(10),
    EmailReserve Varchar2(15),
    NomResponsable Varchar2(15),
constraint IdentificationReserve PRIMARY KEY (IdReserve) 
);

create table ForetProtege(
    Superficie Number(3),
    IdReserve Varchar2(5),
constraint IdentificationReserve FOREIGN KEY (IdReserve) REFERENCES Reserve(IdReserve) 
);
create table JardinBotanique(
    NomOrganisme Varchar2(15),
    TutelleResponsable Varchar2(10),
    AdresseResponsable Varchar2(20),
    ContactResponsable Varchar2(10),
    IdReserve Varchar2(5), 
constraint IdentificationReserve FOREIGN KEY (IdReserve) REFERENCES Reserve(IdReserve)
);
create table Nutriments(
    IdNutri Number(4),
    NomNutri Varchar2(30),
    FormulChim Varchar2(25),
    TypeNutri Varchar2(25),
constraint IdentNutriment PRIMARY KEY(IdNutri)
);
create table NutrimentSubstitus(
    IdNutri Number(4) NOT NULL REFERENCES Nutriments(IdNutri)
);
create table Stock(
    StockDeNutriment Number(4),
    IdReserve Varchar2(5),
    IdNutri Number(4),
constraint IdReserveExistStock FOREIGN KEY(IdReserve) REFERENCES Reserve(IdReserve),
constraint IdNutriExistStock FOREIGN KEY(IdNutri) REFERENCES Nutriments(IdNutri)
);
create table Emplacement(
    CodeEmplacement Number(5) NOT NULL,
    IdReserve Varchar2(5), 
constraint CodeDeEmplacement PRIMARY KEY (CodeEmplacement),
constraint IdentificationReserve FOREIGN KEY (IdReserve) REFERENCES Reserve(IdReserve)
);
create table FicheArosage(
    Idfiche Number(4),
    ModeArrosage Varchar2(20),
    QuantitéEauPrSemaine Number(3),
    AjustSaison Varchar2(10),
    ConditionClima Varchar2(10),
constraint IdentFiche PRIMARY KEY(Idfiche)
);
create table Espece(
    IdEspec Number(4),
    NomSctfk Varchar2(40),
    NomVulg Varchar2(25),
    Descrip Varchar2(100),
    Remarq Varchar2(40)
    Idfiche Number(4),
constraint IdentEspec PRIMARY KEY(IdentEspec),
constraint FicheExiste FOREIGN KEY(Idfiche) REFERENCES FicheArosage(Idfiche)
);
create table ZoneGeo(
    NomZoneGeo Varchar2(10),
constraint NomZoneGeologique PRIMARY KEY(NomZoneGeo)
);
create table ZoneOrigine(
    IdentEspec Number(4),
    NomZoneGeo Varchar2(10),
constraint IdentEspecZoneOrigine FOREIGN KEY(IdentEspec) REFERENCES Espece(IdEspec),
constraint NomZoneGeoZoneOrigine FOREIGN KEY(NomZoneGeo) REFERENCES ZoneGeo(NomZoneGeo)
);
create table besoin(
    IdNutri Number(4),
    IdReserve Varchar2(5),
constraint IdNutriBesoin FOREIGN KEY(IdNutri) REFERENCES Nutriments(IdNutri),
constraint IdReserveBesoin FOREIGN KEY(Idfiche) REFERENCES Reserve(IdReserve)
);
create table Plantes(
    Idplante Varchar2(4),
    DatePlantation Varchar2(8),
    Couleur Varchar2(10),
    Hauteur Number(5),
    CodeDeEmplacement Number(5),
constraint IdentPlante PRIMARY KEY (Idplante),
constraint EmplacementExist FOREIGN KEY(CodeDeEmplacement) REFERENCES Emplacement(CodeDeEmplacement)
);
