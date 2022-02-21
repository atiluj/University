-- Julita Osman, PPo

-- Zadanie 0

drop table if exists sunken_city;

-- skopiowane z mondial-scheme
CREATE TABLE sunken_city
(Name VARCHAR(50),
 Country VARCHAR(4),
 Province VARCHAR(50),
 sinking_date DATE,
 Population DECIMAL CONSTRAINT CityPop
   CHECK (Population >= 0),
 Latitude DECIMAL CONSTRAINT CityLat
   CHECK ((Latitude >= -90) AND (Latitude <= 90)) ,
 Longitude DECIMAL CONSTRAINT CityLon
   CHECK ((Longitude >= -180) AND (Longitude <= 180)) ,
 Elevation DECIMAL ,
 CONSTRAINT sunken_cityKey PRIMARY KEY (Name, Country, Province));



-- Zadanie 1
drop table if exists last_sea_level;
create table last_sea_level(argument int);

CREATE OR REPLACE function sea_level(int) returns VOID
AS $X$
	-- MIASTA Z CITY DO SUNKEN_CITY
	insert into sunken_city 
		select name, country, province, current_timestamp, population, latitude, longitude, elevation
			from city
				where elevation < $1;
	-- USUNIĘCIE LOTNISK
	delete from airport 
		where elevation < $1;
	-- USTAWIENIE LOTNISK NA NULL JEŚLI MIASTO ZOSTAŁO ZATOPIONA, A LOTNISKO NIE
	update airport
		set city = null
		from city c --z tabeli city
		where airport.city = c.name and airport.country = c.country and c.elevation < $1;
	-- USUNIĘCIE MIAST Z CITY
	delete from city
		where elevation < $1; 
	--ZAPAMIETANIE OSTATNIEJ WARTOŚCI PRZEKAZNEJ DO SEA_LEVEL
	delete from last_sea_level;
	insert into last_sea_level values ($1); 
$X$ language SQL;

-- wywołanie
--select sea_level(2000);
--
---- upewaniamy się, że większośc miasto zostało przerzuconych.
--select * from sunken_city;
--
----upewnienie sie że miasta zostały usunięte z oryginalnej tabeli
--select * from city;
--
----sprawdzenie czy lotniska przetrwały jeśli miasto zostało zatopione a one nie
--select* from airport where city is NULL;
--
---- sprawdzenie czy ostatni argument został zapisany
-- select * from last_sea_level;
--
---- Widizmy, że postałe lotniska i miasta mają elevation wiekszy niż podany argument. Lotnikso El Alto Intl przetrwało a jego miasto nie. 
--select * from airport where city is null; 

--Lotnisk El Alto Intl przetrwało bo miasto La Paz w Boliwi nie zostało zatopione, zostały zatopiona inne miasta o nazwie 
--La Paz w innych krajach których elevacja była mniejsza niż podany argument

-- Zadanie 2
CREATE OR REPLACE FUNCTION delete_city() RETURNS TRIGGER AS
$X$
	declare arg int;
	select argument from last_sea_level into arg;

	delete city
		where elevation < arg;
$X$ LANGUAGE plpgsql;

CREATE TRIGGER trigger_sea_level AFTER INSERT ON sunken_city
FOR EACH ROW EXECUTE PROCEDURE delete_city();






