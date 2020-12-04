#**************************************************************************************************#
#                                                                                                  #
# 05_Z_scores                                                                                      #
#                                                                                                  #
# Authors: S.G.M. Neves                                                                            #
#                                                                                                  #
#**************************************************************************************************#

#%% 1. Individual Values
import matplotlib.pyplot as plt
import pandas as pd

houses = pd.read_table('AmesHousing_1.txt')

std = houses["SalePrice"].std(ddof=0)
mean = houses["SalePrice"].mean()

houses["SalePrice"].plot.kde(xlim=(min(houses["SalePrice"]),max(houses["SalePrice"])))
plt.axvline(mean, color="black", label="Mean")
plt.axvline(mean + std, color="red", label="Standard deviation")
plt.axvline(220000, color="orange", label="220000")
plt.legend()

very_expensive = False

#--------------------------------------------------------------------------------------------------#

#%% 2. Number of Standard Deviations
st_devs_away = (220000 - mean) / std

#--------------------------------------------------------------------------------------------------#

#%% 3. Z-scores
import numpy as np

def z_score(val, vector):

    return (val - np.mean(vector)) / np.std(vector)

min_val = houses['SalePrice'].min()
mean_val = houses['SalePrice'].mean()
max_val = houses['SalePrice'].max()

min_z = z_score(min_val, houses['SalePrice'])
mean_z = z_score(mean_val, houses['SalePrice'])
max_z = z_score(max_val, houses['SalePrice'])

#--------------------------------------------------------------------------------------------------#

#%% 4. Locating Values in Different Distributions
neighborhoods = ["NAmes", "CollgCr", "OldTown", "Edwards", "Somerst"]

z_scores = [z_score(200000, houses.loc[houses["Neighborhood"] == i,"SalePrice"]) for i in neighborhoods]

lowest = neighborhoods[np.argmin(np.abs(z_scores))]

best_investment = "College Creek"

#--------------------------------------------------------------------------------------------------#

#%% 5. Transforming Distributions
mean = houses['SalePrice'].mean()
st_dev = houses['SalePrice'].std(ddof = 0)

houses['z_prices'] = houses['SalePrice'].apply(lambda x: ((x - mean) / st_dev))

z_mean_price = houses['z_prices'].mean()
z_stdev_price = houses['z_prices'].std(ddof = 0)

mean = houses['Lot Area'].mean()
st_dev = houses['Lot Area'].std(ddof = 0)

houses['z_area'] = houses['Lot Area'].apply(lambda x: ((x - mean) / st_dev))

z_mean_area = houses['z_area'].mean()
z_stdev_area = houses['z_area'].std(ddof = 0)

#--------------------------------------------------------------------------------------------------#

#%% 6. The Standard Distribution
from numpy import std, mean

population = [0,8,0,8]

z_population = [(x - mean(population)) / std(population) for x in population]

mean_z = mean(z_population)
stdev_z = std(z_population)

#--------------------------------------------------------------------------------------------------#

#%% 7. Standardizing Samples
sample = [0,8,0,8]

x_bar = mean(sample)
s = std(sample, ddof = 1)

standardized_sample = [(val - x_bar) / s for val in sample]

stdev_sample = std(standardized_sample, ddof=1)

#--------------------------------------------------------------------------------------------------#

#%% 8. Using Standardization for Comparisons
z_1 = [(x - mean(houses["index_1"])) / std(houses["index_1"]) for x in houses["index_1"]]
print(z_1[:2])

z_2 = [(x - mean(houses["index_2"])) / std(houses["index_2"]) for x in houses["index_2"]]
print(z_2[:2])

better = "first"

#--------------------------------------------------------------------------------------------------#

#%% 9. Converting Back from Z-scores
index = houses["z_merged"] * 10 + 50

mean_transformed = mean(index)

stdev_transformed = std(index)
