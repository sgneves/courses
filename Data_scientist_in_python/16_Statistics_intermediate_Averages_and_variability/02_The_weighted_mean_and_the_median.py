#**************************************************************************************************#
#                                                                                                  #
# 02_The_weighted_mean_and_the_median                                                              #
#                                                                                                  #
# Authors: S.G.M. Neves                                                                            #
#                                                                                                  #
#**************************************************************************************************#

#%% 1. Introduction
mean_new = houses_per_year["Mean Price"].mean()

mean_original = houses["SalePrice"].mean()

difference = mean_original - mean_new

#--------------------------------------------------------------------------------------------------#

#%% 2. Different Weights
weighted_mean = (houses_per_year["Mean Price"] * houses_per_year["Houses Sold"]).sum() / houses_per_year["Houses Sold"].sum()

mean_original = houses["SalePrice"].mean()

difference = mean_original - weighted_mean

#--------------------------------------------------------------------------------------------------#

#%% 3. The Weighted Mean
import numpy as np

def weighted_mean(means, weights):

    aux = 0

    for i in range(len(means)):

        aux += means[i] * weights[i]

    return aux / sum(weights)

weighted_mean_function = weighted_mean(houses_per_year["Mean Price"], houses_per_year["Houses Sold"])

weighted_mean_numpy = np.average(houses_per_year["Mean Price"], weights=houses_per_year["Houses Sold"])

equal = weighted_mean_function == weighted_mean_numpy

#--------------------------------------------------------------------------------------------------#

#%% 4. The Median for Open-ended Distributions
distribution1 = [23, 24, 22, '20 years or lower,', 23, 42, 35]
distribution2 = [55, 38, 123, 40, 71]
distribution3 = [45, 22, 7, '5 books or lower', 32, 65, '100 books or more']

median1 = 23
median2 = 55
median3 = 32

#--------------------------------------------------------------------------------------------------#

#%% 5. Distributions with Even Number of Values
import pandas as pd

houses = pd.read_csv("AmesHousing_1.txt", sep = '\t')

n_rooms = houses["TotRms AbvGrd"].copy().str.replace("10 or more", "10").astype("int").sort_values()

median = n_rooms.iloc[[1464, 1465]].mean()

#--------------------------------------------------------------------------------------------------#

#%% 6. The Median as a Resistant Statistic
import matplotlib.pyplot as plt

plt.subplot(1, 2, 1)
houses["Lot Area"].plot.box()
plt.subplot(1, 2, 2)
houses["SalePrice"].plot.box()

lotarea_mean = houses["Lot Area"].mean()
lotarea_median = houses["Lot Area"].median()

saleprice_mean = houses["SalePrice"].mean()
saleprice_median = houses["SalePrice"].median()

lotarea_difference = lotarea_mean - lotarea_median
saleprice_difference = saleprice_mean - saleprice_median

#--------------------------------------------------------------------------------------------------#

#%% 7. The Median for Ordinal Scales
mean = houses["Overall Cond"].mean()

median = houses["Overall Cond"].median()

houses["Overall Cond"].plot.hist()

more_representative = "mean"

#--------------------------------------------------------------------------------------------------#

#%% 8. Sensitivity to Changes
# No code
