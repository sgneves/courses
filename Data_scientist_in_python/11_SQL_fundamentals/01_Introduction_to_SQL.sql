/*-------------------------------------------------------------------------------------------------/
/                                                                                                  /
/ 01_Introduction_to_SQL                                                                           /
/                                                                                                  /
/ Authors: S.G.M. Neves                                                                            /
/                                                                                                  /
/-------------------------------------------------------------------------------------------------*/

-- 1. Why_SQL_is_Important_to_Learn
-- No code

/*------------------------------------------------------------------------------------------------*/

-- 2. Introduction_to_Databases
-- No code

/*------------------------------------------------------------------------------------------------*/

-- 3. Your_First_Query
SELECT *
  FROM recent_grads;

/*------------------------------------------------------------------------------------------------*/

-- 4. Understanding_your_First_Query
SELECT * 
  FROM recent_grads;
  
select * from recent_grads

/*------------------------------------------------------------------------------------------------*/

-- 5. Previewing_a_Table
-- No code

/*------------------------------------------------------------------------------------------------*/

-- 6. The_LIMIT_Clause
SELECT *
  FROM recent_grads
 LIMIT 5;

/*------------------------------------------------------------------------------------------------*/

-- 7. Selecting_Specific_Columns
SELECT Major, ShareWomen
  FROM recent_grads;

/*------------------------------------------------------------------------------------------------*/

-- 8. Filtering_Rows_Using_WHERE
SELECT Major, ShareWomen
  FROM recent_grads
 WHERE ShareWomen < 0.5;

/*------------------------------------------------------------------------------------------------*/

-- 9. Expressing_Multiple_Filter_Criteria_Using_'AND'
SELECT Major, Major_category, Median, ShareWomen
  FROM recent_grads
 WHERE ShareWomen > 0.5
   AND Median > 50000;

/*------------------------------------------------------------------------------------------------*/

-- 10. Returning_One_of_Several_Conditions_With_OR
SELECT Major, Median, Unemployed
  FROM recent_grads
 WHERE Median >= 10000
    OR Men > Women
 LIMIT 20;

/*------------------------------------------------------------------------------------------------*/

-- 11. Grouping_Operators_With_Parentheses
SELECT Major, Major_category, ShareWomen, Unemployment_rate
  FROM recent_grads
 WHERE (Major_category = 'Engineering') 
   AND (ShareWomen > 0.5 OR Unemployment_rate < 0.051);

/*------------------------------------------------------------------------------------------------*/

-- 12. Ordering_Results_Using_ORDER_BY
SELECT Major, ShareWomen, Unemployment_rate
  FROM recent_grads
 WHERE ShareWomen > 0.3
   AND Unemployment_rate < 0.1
 ORDER BY ShareWomen DESC;

/*------------------------------------------------------------------------------------------------*/

-- 13. Practice_Writing_a_Query
SELECT Major_category, Major, Unemployment_rate
  FROM recent_grads
 WHERE Major_category = 'Engineering'
    OR Major_category = 'Physical Sciences'
 ORDER BY Unemployment_rate;
