#**************************************************************************************************#
#                                                                                                  #
# 06_Querying_SQLite_from_python                                                                   #
#                                                                                                  #
# Authors: S.G.M. Neves                                                                            #
#                                                                                                  #
#**************************************************************************************************#

#%% 1.Overview
# No code

#--------------------------------------------------------------------------------------------------#

#%% 2.Introduction to the Data
# No code

#--------------------------------------------------------------------------------------------------#

#%% 3.Connecting to the Database
import sqlite3

conn = sqlite3.connect('jobs.db')

#--------------------------------------------------------------------------------------------------#

#%% 4.Introduction to Cursor Objects and Tuples
# No code

#--------------------------------------------------------------------------------------------------#

#%% 5.Working With Sequences of Values as Tuples
# No code

#--------------------------------------------------------------------------------------------------#

#%% 6.Creating a Cursor and Running a Query

# Connect to jobs.db
conn = sqlite3.connect('jobs.db')
cursor = conn.cursor()

# SQL Query as a string
query = "SELECT Major FROM recent_grads;"

# Execute the query, convert the results to tuples, and store as a local variable
cursor.execute(query)

# Fetch the full results set as a list of tuples
majors = cursor.fetchall()

# Display the first three results
print(majors[0:3])

#--------------------------------------------------------------------------------------------------#

#%% 7.Execute as a Shortcut for Running a Query
# No code

#--------------------------------------------------------------------------------------------------#

#%% 8.Fetching a Specific Number of Results
query = "SELECT Major, Major_category FROM recent_grads;"

five_results = conn.execute(query).fetchmany(5)

#--------------------------------------------------------------------------------------------------#

#%% 9.Closing the Database Connection
conn.close()

#--------------------------------------------------------------------------------------------------#

#%% 10.Practice
conn = sqlite3.connect('jobs2.db')

query = "SELECT Major FROM recent_grads ORDER BY 1 DESC;"

reverse_alphabetical = conn.execute(query).fetchall()

conn.close()
