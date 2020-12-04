#**************************************************************************************************#
#                                                                                                  #
# 03_Multi_category_chi_squared_tests                                                              #
#                                                                                                  #
# Authors: S.G.M. Neves                                                                            #
#                                                                                                  #
#**************************************************************************************************#

#%% 1.Multiple categories
# No code

#--------------------------------------------------------------------------------------------------#

#%% 2.Calculating expected values
males_over50k = 0.67 * 0.241 * 32561

males_under50k = 0.67 * 0.759 * 32561

females_over50k = 0.33 * 0.241 * 32561

females_under50k = 0.33 * 0.759 * 32561

#--------------------------------------------------------------------------------------------------#

#%% 3.Calculating chi-squared
chisq_gender_income = (6662 - 5257.6)**2 / 5257.6 + (1179 - 2589.6)**2 / 2589.6 + (15128 - 16558.2)**2 / 16558.2 + (9592 - 8155.6)**2 / 8155.6
#--------------------------------------------------------------------------------------------------#

#%% 4.Finding statistical significance
from scipy.stats import chisquare
import numpy as np

obs = np.array([6662, 1179, 15128, 9592])
exp = np.array([5257.6, 2589.6,  16558.2, 8155.6])

chisquare_value, pvalue_gender_income = chisquare(obs, exp)

#--------------------------------------------------------------------------------------------------#

#%% 5.Cross tables
import pandas as pd

income = pd.read_csv("income.csv")

table = pd.crosstab(income["sex"], [income["race"]])
print(table)

#--------------------------------------------------------------------------------------------------#

#%% 6.Finding expected values
from scipy.stats import chi2_contingency

chisq_value, pvalue_gender_race, df, expected = chi2_contingency(table)

#--------------------------------------------------------------------------------------------------#

#%% 7.Caveats
# No code
