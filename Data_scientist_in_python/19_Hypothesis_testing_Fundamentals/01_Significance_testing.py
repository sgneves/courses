#**************************************************************************************************#
#                                                                                                  #
# 01_Significance_testing                                                                          #
#                                                                                                  #
# Authors: S.G.M. Neves                                                                            #
#                                                                                                  #
#**************************************************************************************************#

#%% 1.Hypothesis testing
# No code

#--------------------------------------------------------------------------------------------------#

#%% 2.Research design
# No code

#--------------------------------------------------------------------------------------------------#

#%% 3.Statistical significance
import numpy as np
import pandas as pd

weight_lost = pd.read_csv("weight_loss.csv",  header=None)

weight_lost_a = np.array(weight_lost[0])
weight_lost_b = np.array(weight_lost[1])

mean_group_a = weight_lost_a.mean()
print(mean_group_a)

mean_group_b = weight_lost_b.mean()
print(mean_group_b)

#--------------------------------------------------------------------------------------------------#

#%% 4.Test statistic
mean_difference = mean_group_b - mean_group_a
print(mean_difference)

#--------------------------------------------------------------------------------------------------#

#%% 5.Permutation test
import matplotlib.pyplot as plt

all_values = [j for i in weight_lost.values.tolist() for j in i]

mean_differences = []

for i in range(1000):

    group_a = []
    group_b = []

    for val in all_values:

        if np.random.rand() >= 0.5:

            group_a.append(val)

        else:
            group_b.append(val)

    mean_differences.append(np.mean(group_b) - np.mean(group_a))

plt.hist(mean_differences)

#--------------------------------------------------------------------------------------------------#

#%% 6.Sampling distribution
# No code

#--------------------------------------------------------------------------------------------------#

#%% 7.Dictionary representation of a distribution
sampling_distribution = {}

for val in mean_differences:

    if val in sampling_distribution:
        sampling_distribution[val] += 1

    else:
        sampling_distribution[val] = 1

#--------------------------------------------------------------------------------------------------#

#%% 8.P value
frequencies = []

for key in sampling_distribution.keys():

    if key >= 2.52:
        frequencies.append(sampling_distribution[key])

p_value = np.sum(frequencies) / 1000

#--------------------------------------------------------------------------------------------------#

#%% 9.Caveats
# No code
