/*-------------------------------------------------------------------------------------------------/
/                                                                                                  /
/ 01_Joining_data_in_SQL                                                                           /
/                                                                                                  /
/ Authors: S.G.M. Neves                                                                            /
/                                                                                                  /
/-------------------------------------------------------------------------------------------------*/

--1. Introducing Joins
SELECT *
  FROM facts
       INNER JOIN cities
       ON cities.facts_id = facts.id
 LIMIT 10;

/*------------------------------------------------------------------------------------------------*/

--2. Understanding Inner Joins
SELECT c.*, f.name country_name
  FROM facts f
       INNER JOIN cities c
       ON c.facts_id = f.id
 LIMIT 5;

/*------------------------------------------------------------------------------------------------*/

--3. Practicing Inner Joins
SELECT f.name country, c.name capital_city
  FROM facts f
       INNER JOIN cities c
       ON c.facts_id = f.id
 WHERE capital == 1;

/*------------------------------------------------------------------------------------------------*/

--4. Left Joins
SELECT f.name country, f.population
  FROM facts f
       LEFT JOIN cities c
       ON c.facts_id = f.id
 WHERE c.name IS NULL;

/*------------------------------------------------------------------------------------------------*/

--5. Right Joins and Outer Joins
-- No code

/*------------------------------------------------------------------------------------------------*/

--6. Finding the Most Populous Capital Cities
SELECT c.name capital_city, f.name country, c.population
  FROM cities c
       INNER JOIN facts f
       ON f.id = c.facts_id
 WHERE capital == 1
 ORDER BY 3 DESC
 LIMIT 10;

/*------------------------------------------------------------------------------------------------*/

--7. Combining Joins with Subqueries
SELECT c.name capital_city, f.name country, c.population
  FROM facts f
       INNER JOIN (
                   SELECT *
                     FROM cities
                    WHERE capital = 1
                      AND population > 10E6
                  ) c
       ON c.facts_id = f.id
 ORDER BY c.population DESC;

/*------------------------------------------------------------------------------------------------*/

--8. Challenge: Complex Query with Joins and Subqueries
SELECT f.name country,
       c.urban_pop, 
       f.population total_pop, 
       CAST(c.urban_pop AS FLOAT) / f.population urban_pct
  FROM facts f
       INNER JOIN (
                   SELECT facts_id, SUM(population) urban_pop
                     FROM cities
                    GROUP BY 1
                  ) c
       ON c.facts_id = f.id
 WHERE urban_pct > 0.5
 ORDER BY urban_pct;



SELECT f.name country, SUM(c.population) urban_pop, f.population total_pop,
       CAST(SUM(c.population) AS FLOAT) / f.population urban_pct
  FROM facts f
       INNER JOIN (
                   SELECT population, facts_id
                     FROM cities
                  ) c
       ON c.facts_id = f.id
 GROUP BY country
HAVING urban_pct > 0.5
 ORDER BY urban_pct;
