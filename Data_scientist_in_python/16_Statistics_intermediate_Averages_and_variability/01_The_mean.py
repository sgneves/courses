#**************************************************************************************************#
#                                                                                                  #
# 01_The_mean                                                                                      #
#                                                                                                  #
# Authors: S.G.M. Neves                                                                            #
#                                                                                                  #
#**************************************************************************************************#

#%% 1. Introduction
# No code

#--------------------------------------------------------------------------------------------------#

#%% 2. The Mean
import numpy as np

distribution = [0,2,3,3,3,4,13]
distribution = np.array(distribution)

mean = distribution.mean()

center = False

distances = distribution - mean

print(distances[distances < 0].sum())
print(distances[distances > 0].sum())

equal_distances = True

#--------------------------------------------------------------------------------------------------#

#%% 3. The Mean as a Balance Point
equal_distances = 0

for i in range(5000):

    np.random.seed(i)

    distribution = np.random.randint(0, 1000, 10)

    mean = distribution.mean()

    distances = distribution - mean

    if abs(distances[distances < 0].sum() + distances[distances > 0].sum()) < 1E-10:
        equal_distances = equal_distances + 1

#--------------------------------------------------------------------------------------------------#

#%% 4. Defining the Mean Algebraically
one = False
two = False
three = False

#--------------------------------------------------------------------------------------------------#

#%% 5. An Alternative Definition
def mean(vector):

    vector_sum = 0

    for val in vector:
        vector_sum += val

    return vector_sum / len(vector)

distribution_1 = [42, 24, 32, 11]
distribution_2 = [102, 32, 74, 15, 38, 45, 22]
distribution_3 = [3, 12, 7, 2, 15, 1, 21]

mean_1 = mean(distribution_1)
mean_2 = mean(distribution_2)
mean_3 = mean(distribution_3)
mean_1 = mean(distribution_1)

#--------------------------------------------------------------------------------------------------#

#%% 6. Introducing the Data
import pandas as pd

houses = pd.read_csv("AmesHousing_1.txt", sep = '\t')

one = True
two = False
three = True

#--------------------------------------------------------------------------------------------------#

#%% 7. Mean House Prices
function_mean = mean(houses['SalePrice'])

pandas_mean = houses['SalePrice'].mean()

means_are_equal = function_mean == pandas_mean

#--------------------------------------------------------------------------------------------------#

#%% 8. Estimating the Population Mean
import matplotlib.pyplot as plt

population_mean = houses['SalePrice'].mean()
samples_sizes = []
samples_means = []
samples_errors = []

for i in range(101):

    sample_size = 5 + 29 * i
    samples_sizes.append(sample_size)

    samples_mean = houses['SalePrice'].sample(sample_size, random_state=i).mean()

    samples_means.append(samples_mean)

    samples_errors.append(population_mean - samples_mean)

plt.scatter(samples_sizes, samples_errors)
plt.axhline(0, color="red")
plt.axvline(2930, color="red")
plt.xlabel("Sample size")
plt.ylabel("Sampling error")

#--------------------------------------------------------------------------------------------------#

#%% 9. Estimates from Low-Sized Samples
samples_means = [houses['SalePrice'].sample(100, random_state=i).mean() for i in range(10000)]

plt.hist(samples_means)
plt.axvline(houses['SalePrice'].mean(), color="red")
plt.xlim(0,500000)
plt.xlabel("Sample mean")
plt.ylabel("Frequency")

#--------------------------------------------------------------------------------------------------#

#%% 10. Variability Around the Population Mean
# No code

#--------------------------------------------------------------------------------------------------#

#%% 11. The Sample Mean as an Unbiased Estimator
population = [3, 7, 2]
means = []

for i in population:

    aux = population.copy()
    aux.remove(i)

    for j in aux:

        means.append((i + j) / 2)

unbiased = sum(population) / 3 == sum(means) / len(means)
