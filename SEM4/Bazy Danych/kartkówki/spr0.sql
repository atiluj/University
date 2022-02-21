
-- Zadanie 1
select * from city
	join airport on city.name = airport.city
	where city.elevation < 100
		and city.country = 'PL'
	order by city.name;

-- Zadanie 2
select distinct sea.name, sea.area from Sea
	join river on Sea.name = river.Sea
	join geo_river on river.name = geo_river.river 
	where river.length > 800
		and geo_river.country = 'F'
	order by sea.area desc;
