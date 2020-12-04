#**************************************************************************************************#
#                                                                                                  #
# 01_Introduction_to_Numpy                                                                         #
#                                                                                                  #
# Authors: S.G.M. Neves                                                                            #
#                                                                                                  #
#**************************************************************************************************#

# 1. Introduction
import numpy as np

data_ndarray = np.array([10, 20, 30])

#--------------------------------------------------------------------------------------------------#

# 2. Introduction to Ndarrays
import numpy as np

data_ndarray = np.array([10, 20, 30])

#--------------------------------------------------------------------------------------------------#

# 3. Understanding Vectorization
# No code

#--------------------------------------------------------------------------------------------------#

# 4. NYC Taxi-Airport Data
import csv

# Import nyc_taxi.csv as a list of lists
f = open("nyc_taxis.csv", "r")
taxi_list = list(csv.reader(f))

# Remove the header row
taxi_list = taxi_list[1:]

# Convert all values to floats
converted_taxi_list = []

for row in taxi_list:

    converted_row = []

    for item in row:

        converted_row.append(float(item))

    converted_taxi_list.append(converted_row)

# Convert to a NumPy ndarray
taxi = np.array(converted_taxi_list)

#--------------------------------------------------------------------------------------------------#

# 5. Array Shapes
taxi_shape = taxi.shape

#--------------------------------------------------------------------------------------------------#

# 6. Selecting and Slicing Rows and Items from ndarrays
row_0 = taxi[0]

rows_391_to_500 = taxi[391:501]

row_21_column_5 = taxi[21,5]

#--------------------------------------------------------------------------------------------------#

# 7. Selecting Columns and Custom Slicing ndarrays
columns_1_4_7 = taxi[:, [1,4,7]]

row_99_columns_5_to_8 = taxi[99, 5:9]

rows_100_to_200_column_14 = taxi[100:201, 14]

#--------------------------------------------------------------------------------------------------#

# 8. Vector Math
fare_and_fees = taxi[:,9] + taxi[:,10]

#--------------------------------------------------------------------------------------------------#

# 9. Vector Math Continued
trip_distance_miles = taxi[:,7]
trip_length_seconds = taxi[:,8]

trip_length_hours = trip_length_seconds / 3600 # 3600 seconds is one hour

trip_mph = trip_distance_miles / trip_length_hours

#--------------------------------------------------------------------------------------------------#

# 10. Calculating Statistics For 1D ndarrays
mph_min = trip_mph.min()
mph_max = trip_mph.max()
mph_mean = trip_mph.mean()

#--------------------------------------------------------------------------------------------------#

# 11. Calculating Statistics For 1D ndarrays Continued
# No code

#--------------------------------------------------------------------------------------------------#

# 12. Calculating Statistics For 2D ndarrays
fare_components = taxi[:5,9:13]

fare_sums = fare_components.sum(axis=1)
fare_totals = taxi[:5,13]

print(fare_sums)
print(fare_totals)
