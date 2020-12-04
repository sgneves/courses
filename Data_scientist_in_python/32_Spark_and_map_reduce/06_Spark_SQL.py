#**************************************************************************************************#
#                                                                                                  #
# 06_Spark_SQL                                                                                     #
#                                                                                                  #
# Authors: S.G.M. Neves                                                                            #
#                                                                                                  #
#**************************************************************************************************#

#%% 1. Overview
# No code

#--------------------------------------------------------------------------------------------------#

#%% 2. Register the DataFrame as a Table
import findspark
findspark.init()

import pyspark
from pyspark.sql import SQLContext

sc = pyspark.SparkContext()

sqlCtx = SQLContext(sc)

df = sqlCtx.read.json("census_2010.json")

df.registerTempTable('census2010')

tables = sqlCtx.tableNames()
print(tables)

#--------------------------------------------------------------------------------------------------#

#%% 3. Querying
sqlCtx.sql('SELECT age FROM census2010').show()

#--------------------------------------------------------------------------------------------------#

#%% 4. Filtering
sqlCtx.sql('SELECT males,females FROM census2010 WHERE age > 5 AND age < 15').show()

#--------------------------------------------------------------------------------------------------#

#%% 5. Mixing Functionality
sqlCtx.sql('SELECT males,females FROM census2010').describe().show()

#--------------------------------------------------------------------------------------------------#

#%% 6. Multiple tables
sqlCtx.read.json("census_1980.json").registerTempTable('census1980')
sqlCtx.read.json("census_1990.json").registerTempTable('census1990')
sqlCtx.read.json("census_2000.json").registerTempTable('census2000')

tables = sqlCtx.tableNames()
print(tables)

#--------------------------------------------------------------------------------------------------#

#%% 7. Joins
query = """
SELECT cl.total, cr.total
  FROM census2010 cl
       INNER JOIN census2000 cr
       ON cl.age = cr.age
"""

sqlCtx.sql(query).show()

#--------------------------------------------------------------------------------------------------#

#%% 8. SQL Functions
query = """
SELECT SUM(c2010.total), SUM(c2000.total), SUM(c1990.total)
  FROM census2010 c2010
       INNER JOIN census2000 c2000
       ON c2000.age = c2010.age
       INNER JOIN census1990 c1990
       ON c1990.age = c2010.age
"""

sqlCtx.sql(query).show()
