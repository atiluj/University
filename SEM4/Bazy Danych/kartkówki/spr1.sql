
-- Zadanie 1

select country.name, count(islandIn.island) as wyspy
	from country
		full outer join geo_sea on (geo_sea.country = country.code) 
		full outer join islandin on (geo_sea.sea = islandin.sea)
	group by country.name
	order by wyspy desc, country.name ASC;

-- Zadanie 2
with
	all_group as
	(select country.name as nameC, count(distinct ethnicgroup.name)
		from country 	
			join ethnicgroup on (ethnicgroup.country = country.code)
			group by country.name
			having count(distinct ethnicgroup.name)>=10),
	polish as 
	(select country.name as nameC, ethnicgroup.percentage as procent
		from country
			join ethnicgroup on (country.code = ethnicgroup.country)
			where ethnicgroup.name ilike 'Polish')
	select all_group.nameC, polish.procent
		from all_group 
			join polish on (polish.nameC=all_group.nameC);
 
-- Zadanie 3

-- Zadanie 4
with
	population as
	(select country.name as countryN, sum(city.population)/country.population as populationP 
		from country
			join city on (country.code = city.country)
			group by country.name, country.population)
	select countryN, populationP 
		from population
		where populationP >= 0.75
		order by populationP desc;
	
		
		

