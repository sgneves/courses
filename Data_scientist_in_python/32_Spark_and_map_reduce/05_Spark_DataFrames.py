#**************************************************************************************************#
#                                                                                                  #
# 05_Spark_DataFrames                                                                              #
#                                                                                                  #
# Authors: S.G.M. Neves                                                                            #
#                                                                                                  #
#**************************************************************************************************#

#%% 1. The Spark DataFrame: An Introduction
import findspark
findspark.init()

import pyspark

sc = pyspark.SparkContext()

census_2010 = sc.textFile("census_2010.json")

census_2010.take(10)

#--------------------------------------------------------------------------------------------------#

#%% 2. Reading in Data

# Import SQLContext
from pyspark.sql import SQLContext

# Pass in the SparkContext object `sc`
sqlCtx = SQLContext(sc)

# Read JSON data into a DataFrame object `df`
df = sqlCtx.read.json("census_2010.json")

# Print the type
print(type(df))

#--------------------------------------------------------------------------------------------------#

#%% 3. Schema
df.printSchema()

#--------------------------------------------------------------------------------------------------#

#%% 4. Pandas vs Spark DataFrames
df.show(5)

#--------------------------------------------------------------------------------------------------#

#%% 5. Row Objects
first_five = df.head(5)

for row in first_five:
    print(row.age)

#--------------------------------------------------------------------------------------------------#

#%% 6. Selecting Columns
df[['age','males','females']].show()

df.select('age', 'males', 'females').show()

#--------------------------------------------------------------------------------------------------#

#%% 7. Filtering Rows
five_plus = df[df.age > 5]

five_plus.show()

#--------------------------------------------------------------------------------------------------#

#%% 8. Using Column Comparisons as Filters
df[df.females < df.males].show()

#--------------------------------------------------------------------------------------------------#

#%% 9. Converting Spark DataFrames to pandas DataFrames
pandas_df = df.toPandas()

pandas_df['total'].hist()
