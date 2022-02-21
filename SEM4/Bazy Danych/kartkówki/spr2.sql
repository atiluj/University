-- Julita Osman, PPo

-- Zadanie 1
drop view seaairports; 

create view SeaAirports
  (iatacode, name, city, province, country, sea)
as
select distinct airport.iatacode , airport.name, airport.city, airport.province, airport.country, located.sea
	from airport 
		--join country on(country.code = airport.country) 
		join located on(airport.city = located.city)
		join city on(located.city = city.name)
	where city.elevation > 200 --napisałam 200 poniewaz Pan Wieczorek napisał informacje na teams
		and sea is not null;
	
-- select * from seaairports;



-- Zadanie 2
--Usuń klucz główny tabeli city.
alter table city drop constraint citykey;
--Dodaj nową kolumnę id do tabeli city, w której wartości będą automatycznie generowane. Ustaw ją jako klucz główny.
alter table city add column id serial primary key;
--Dodaj nową kolumnę CityId do tabeli airports. Jej typ powinien odpowiadać typowi kolumny id tabeli city.
ALTER TABLE airport ADD COLUMN CityId int;
--Ustaw wartości w kolumnie CityId tabeli airports tak aby odpowiadały wartościom w kolumnie city.

--Dodaj klucz obcy, który wymusi aby w tabeli airport wszystkie niepuste wartości CityId występowały jako id w tabeli city.

--Dodaj do bazy informacje o lotnisku dla miasta Zielona Góra o nazwie Babimost i kodzie IATA IEG tak, aby ta operacja powiodła się w obecności klucza z poprzedniego podpunktu. Dla tych kolumn, dla których to możliwe przepisz wartości z odpowiednich kolumn dla Zielonej Góry. Pozostałym kolumnom nadaj wartości NULL.
	
 
 
 
 
-- Zadanie 3
--select * from countrypops
--order by year desc;
	
insert into countrypops(country, year, population)
select country.code, 2021, country.population 
	from country;

select * from countrypops
order by year desc;




-- Zadanie 4
select year, max(population)
	from countrypops



		
		

