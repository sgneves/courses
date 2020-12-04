/*-------------------------------------------------------------------------------------------------/
/                                                                                                  /
/ 03_Building_and_organizing_complex_queries                                                       /
/                                                                                                  /
/ Authors: S.G.M. Neves                                                                            /
/                                                                                                  /
/-------------------------------------------------------------------------------------------------*/

--1. Introduction
-- No code

/*------------------------------------------------------------------------------------------------*/

--2. Writing Readable Queries
-- No code

/*------------------------------------------------------------------------------------------------*/

--3. The With Clause
  WITH playlist_info AS
       (
        SELECT pl.playlist_id,
               pl.name playlist_name,
               t.name track_name,
               t.milliseconds / 1000 length_seconds
          FROM playlist pl
               LEFT JOIN playlist_track plt
               ON plt.playlist_id = pl.playlist_id
               LEFT JOIN track t
               ON t.track_id = plt.track_id
       )
SELECT playlist_id,
       playlist_name,
       COUNT(track_name) number_of_tracks,
       SUM(length_seconds) length_seconds
  FROM playlist_info
 GROUP BY playlist_id
 ORDER BY playlist_id;

/*------------------------------------------------------------------------------------------------*/

--4. Creating Views
CREATE VIEW customer_gt_90_dollars AS
SELECT c.*
  FROM customer c
       LEFT JOIN invoice i
       ON i.customer_id = c.customer_id
 GROUP BY c.customer_id
HAVING SUM(i.total) > 90;

SELECT *
  FROM customer_gt_90_dollars;

CREATE VIEW customer_usa AS 
SELECT *
  FROM customer
 WHERE country = "USA";

/*------------------------------------------------------------------------------------------------*/

--5. Combining Rows With Union
SELECT *
  FROM customer_usa

UNION

SELECT *
  FROM customer_gt_90_dollars;

/*------------------------------------------------------------------------------------------------*/

--6. Combining Rows Using Intersect and Except
  WITH customers_usa_gt_90 AS
       (
           SELECT *
             FROM customer_usa
       
        INTERSECT
       
           SELECT *
             FROM customer_gt_90_dollars
       )
SELECT e.first_name || " " || e.last_name employee_name,
       COUNT(c.customer_id) customers_usa_gt_90
  FROM employee e
       LEFT JOIN customers_usa_gt_90 c
       ON c.support_rep_id = e.employee_id
 WHERE e.title = 'Sales Support Agent'
 GROUP BY 1
 ORDER BY 1;

/*------------------------------------------------------------------------------------------------*/

--7. Multiple Named Subqueries
  WITH customers_india AS
       (
        SELECT customer_id,
               first_name || " " || last_name customer_name
          FROM customer
         WHERE country = 'India'
       ),
       sales_per_customer AS
       (
        SELECT customer_id,
               SUM(total) total_purchases
          FROM invoice
         GROUP BY customer_id
       )
SELECT customer_name, total_purchases
  FROM customers_india
       LEFT JOIN sales_per_customer
       ON sales_per_customer.customer_id = customers_india.customer_id
 ORDER BY customer_name;

/*------------------------------------------------------------------------------------------------*/

--8. Challenge: Each Country's Best Customer
  WITH sales_per_customer AS
       (
        SELECT customer_id,
               SUM(total) total_purchased
          FROM invoice
         GROUP BY customer_id
       )
SELECT country,
       first_name || " " || last_name customer_name,
       MAX(total_purchased) total_purchased
  FROM customer
       LEFT JOIN sales_per_customer
       ON sales_per_customer.customer_id = customer.customer_id
 GROUP BY 1
 ORDER BY 1;
