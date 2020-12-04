#**************************************************************************************************#
#                                                                                                  #
# 02_Chi_squared_tests                                                                             #
#                                                                                                  #
# Authors: S.G.M. Neves                                                                            #
#                                                                                                  #
#**************************************************************************************************#

#%% 1.Observed and expected frequencies
# No code

#--------------------------------------------------------------------------------------------------#

#%% 2.Calculating differences
female_diff = (10771 - 16280.5) / 16280.5
male_diff = (21790 - 16280.5) / 16280.5

#--------------------------------------------------------------------------------------------------#

#%% 3.Updating the formula
female_diff = (10771 - 16280.5)**2 / 16280.5
male_diff = (21790 - 16280.5)**2 / 16280.5

gender_chisq = female_diff + male_diff

#--------------------------------------------------------------------------------------------------#

#%% 4.Generating a distribution
import numpy as np
import matplotlib.pyplot as plt

chi_squared_values = []
exp = 16280.5

for i in range(1000):

    n_pop = 32561

    numbers = np.random.rand(n_pop)

    n_male = np.sum([0 if number < 0.5 else 1 for number in numbers])
    n_female = n_pop - n_male

    chi_squared_values.append((n_male - exp)**2 / exp + (n_female - exp)**2 / exp)

plt.hist(chi_squared_values)

#--------------------------------------------------------------------------------------------------#

#%% 5.Statistical significance
# No code

#--------------------------------------------------------------------------------------------------#

#%% 6.Smaller samples
female_diff = (107.71 - 162.805)**2 / 162.805
male_diff = (217.90 - 162.805)**2 / 162.805

gender_chisq = female_diff + male_diff

#--------------------------------------------------------------------------------------------------#

chi_squared_values = []
exp = 150

for i in range(1000):

    n_pop = 300

    numbers = np.random.rand(n_pop)

    n_male = np.sum([0 if number < 0.5 else 1 for number in numbers])
    n_female = n_pop - n_male

    chi_squared_values.append((n_male - exp)**2 / exp + (n_female - exp)**2 / exp)

plt.hist(chi_squared_values)

#--------------------------------------------------------------------------------------------------#

#%% 8.Degrees of freedom
# No code

#--------------------------------------------------------------------------------------------------#

#%% 9.Increasing degrees of freedom
import numpy as np

obs = np.array([27816,3124,1039,311,271])
exp = np.array([26146.5,3939.9,944.3,260.5,1269.8])

race_chisq = ((obs - exp)**2 / exp).sum()

#--------------------------------------------------------------------------------------------------#

#%% 10.Using SciPy
from scipy.stats import chisquare

obs = np.array([27816,3124,1039,311,271])
exp = np.array([26146.5,3939.9,944.3,260.5,1269.8])

chisquare_value, race_pvalue = chisquare(obs, exp)
