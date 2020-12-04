/*-------------------------------------------------------------------------------------------------/
/                                                                                                  /
/ 02_Intermediate_joins_in_SQL                                                                     /
/                                                                                                  /
/ Authors: S.G.M. Neves                                                                            /
/                                                                                                  /
/-------------------------------------------------------------------------------------------------*/

--1. Working With Larger Databases
-- No code

/*------------------------------------------------------------------------------------------------*/

--2. Joining Three Tables
SELECT il.track_id track_id,
       t.name track_name,
       mt.name track_type,
       il.unit_price,
       il.quantity
  FROM invoice_line il
       INNER JOIN track t
       ON t.track_id = il.track_id
       INNER JOIN media_type mt
       ON mt.media_type_id = t.media_type_id
WHERE invoice_id = 4;

/*------------------------------------------------------------------------------------------------*/

--3. Joining More Than Three Tables
SELECT il.track_id track_id,
       t.name track_name,
       art.name artist_name,
       mt.name track_type,
       il.unit_price,
       il.quantity
  FROM invoice_line il
       INNER JOIN track t
       ON t.track_id = il.track_id
       INNER JOIN media_type mt
       ON mt.media_type_id = t.media_type_id
       INNER JOIN album alb
       ON alb.album_id = t.album_id
       INNER JOIN artist art
       ON art.artist_id = alb.artist_id
WHERE invoice_id = 4;

/*------------------------------------------------------------------------------------------------*/

--4. Combining Multiple Joins with Subqueries
SELECT ta.album, ta.artist, COUNT(*) tracks_purchased
  FROM invoice_line il
       INNER JOIN (
                   SELECT t.track_id, art.name artist, alb.title album
                     FROM track t
                          INNER JOIN album alb
                          ON alb.album_id = t.album_id
                          INNER JOIN artist art
                          ON art.artist_id = alb.artist_id
                  ) ta
       ON ta.track_id = il.track_id
 GROUP BY album
 ORDER BY tracks_purchased DESC
 LIMIT 5;

/*------------------------------------------------------------------------------------------------*/

--5. Recursive Joins
SELECT e.first_name || ' ' || e.last_name employee_name,
       e.title employee_title,
       s.first_name || ' ' || s.last_name supervisor_name,
       s.title supervisor_title
  FROM employee e
       LEFT JOIN employee s
       ON s.employee_id = e.reports_to
 ORDER BY 1;

/*------------------------------------------------------------------------------------------------*/

--6. Pattern Matching Using Like
SELECT first_name, last_name, phone
  FROM customer
 WHERE first_name LIKE '%Belle%';

/*------------------------------------------------------------------------------------------------*/

--7. Generating Columns With The Case Statement
SELECT c.first_name || ' ' || c.last_name customer_name,
       COUNT(*) number_of_purchases,
       SUM(i.total) total_spent,
       CASE
       WHEN SUM(i.total) < 40 THEN 'small spender'
       WHEN SUM(i.total) <= 100 THEN 'regular'
       ELSE 'big spender'
       END AS customer_category
  FROM customer c
       LEFT JOIN invoice i
       ON i.customer_id = c.customer_id
 GROUP BY customer_name;
