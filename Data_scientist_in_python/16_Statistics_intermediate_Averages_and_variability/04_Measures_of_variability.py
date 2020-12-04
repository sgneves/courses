#**************************************************************************************************#
#                                                                                                  #
# 04_Measures_of_variability                                                                       #
#                                                                                                  #
# Authors: S.G.M. Neves                                                                            #
#                                                                                                  #
#**************************************************************************************************#

#%% 1. The Range
import pandas as pd

houses = pd.read_table('AmesHousing_1.txt')

def calc_range(vector):

    return max(vector) - min(vector)

range_by_year = {}

for year in sorted(houses["Yr Sold"].unique()):

    range_by_year[year] = calc_range(houses.loc[houses["Yr Sold"] == year, "SalePrice"])

one = False
two = True

#--------------------------------------------------------------------------------------------------#

#%% 2. The Average Distance
def avg_deviation(vector):

    mean = sum(vector) / len(vector)

    diff = [val - mean for val in vector]

    return sum(diff) / len(diff)

C = [1,1,1,1,1,1,1,1,1,21]

avg_distance = avg_deviation(C)
print(avg_distance)

#--------------------------------------------------------------------------------------------------#

#%% 3. Mean Absolute Deviation
def avg_abs_deviation(vector):

    mean = sum(vector) / len(vector)

    diff = [abs(val - mean) for val in vector]

    return sum(diff) / len(diff)

C = [1,1,1,1,1,1,1,1,1,21]

mad = avg_abs_deviation(C)
print(mad)

#--------------------------------------------------------------------------------------------------#

#%% 4. Variance
def variance(vector):

    mean = sum(vector) / len(vector)

    diff = [abs(val - mean)**2 for val in vector]

    return sum(diff) / len(diff)

C = [1,1,1,1,1,1,1,1,1,21]

variance_C = variance(C)
print(variance_C)

#--------------------------------------------------------------------------------------------------#

#%% 5. Standard Deviation
from math import sqrt

def std(vector):

    mean = sum(vector) / len(vector)

    diff = [abs(val - mean)**2 for val in vector]

    return sqrt(sum(diff) / len(diff))

C = [1,1,1,1,1,1,1,1,1,21]

standard_deviation_C = std(C)
print(standard_deviation_C)

#--------------------------------------------------------------------------------------------------#

#%% 6. Average Variability Around the Mean
year_std = [std(houses.loc[houses["Yr Sold"] == year, "SalePrice"]) for year in range_by_year.keys()]

greatest_variability = list(range_by_year.keys())[year_std.index(max(year_std))]

lowest_variability = list(range_by_year.keys())[year_std.index(min(year_std))]

#--------------------------------------------------------------------------------------------------#

#%% 7. A Measure of Spread
sample1 = houses['Year Built'].sample(50, random_state = 1)
sample2 = houses['Year Built'].sample(50, random_state = 2)

bigger_spread = "sample 2"

st_dev1 = std(sample1)
st_dev2 = std(sample2)

#--------------------------------------------------------------------------------------------------#

#%% 8. The Sample Standard Deviation
import matplotlib.pyplot as plt

stds = [std(houses["SalePrice"].sample(10, random_state=i)) for i in range(5000)]

plt.hist(stds)

plt.axvline(std(houses["SalePrice"]))

#--------------------------------------------------------------------------------------------------#

#%% 9. Bessel's Correction
def std(vector):

    mean = sum(vector) / len(vector)

    diff = [abs(val - mean)**2 for val in vector]

    return sqrt(sum(diff) / (len(diff) - 1))

st_devs = [std(houses["SalePrice"].sample(10, random_state=i)) for i in range(5000)]

plt.hist(st_devs)

plt.axvline(std(houses["SalePrice"]))

#--------------------------------------------------------------------------------------------------#

#%% 10. Standard Notation
from numpy import std, var

sample = houses.sample(100, random_state = 1)

pandas_stdev = sample["SalePrice"].std()

numpy_stdev = std(sample["SalePrice"], ddof=1)

equal_stdevs = pandas_stdev == numpy_stdev

pandas_var = sample["SalePrice"].var()

numpy_var = var(sample["SalePrice"], ddof=1)

equal_vars = pandas_var == numpy_var

#--------------------------------------------------------------------------------------------------#

#%% 11. Sample Variance — Unbiased Estimator
from numpy import mean

population = [0, 3, 6]

samples = [[0,3], [0,6],
           [3,0], [3,6],
           [6,0], [6,3]
          ]

equal_var = mean([var(sample) for sample in samples]) == var(population)

equal_stdev = mean([std(sample) for sample in samples]) == std(population)
