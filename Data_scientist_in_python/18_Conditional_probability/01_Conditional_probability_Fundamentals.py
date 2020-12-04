#**************************************************************************************************#
#                                                                                                  #
# 01_Conditional_probability_Fundamentals                                                          #
#                                                                                                  #
# Authors: S.G.M. Neves                                                                            #
#                                                                                                  #
#**************************************************************************************************#

#%% 1.Introduction
# No code

#--------------------------------------------------------------------------------------------------#

#%% 2.Brief Recap
p_2 = 1/6

p_odd = 3/6

p_2_or_4 = 2/6

#--------------------------------------------------------------------------------------------------#

#%% 3.Updating Probabilities
p_3 = 1/4

p_6 = 0

p_odd = 2/4

p_even = 2/4

#--------------------------------------------------------------------------------------------------#

#%% 4.Conditional Probability
p_december = 1/3

p_summer = 0

p_ends_r = 1/3

#--------------------------------------------------------------------------------------------------#

#%% 5.Conditional Probability Formula
import numpy as np

A = np.arange(2,8)
A = A.reshape(1, len(A))

for i in range(5): A = np.vstack((A, A[-1,:] + 1))

card_b = 21

card_a_and_b = 9

p_a_given_b = card_a_and_b / card_b

#--------------------------------------------------------------------------------------------------#

#%% 6.Example Walkthough
p_negative_given_non_hiv = 6/30
print(p_negative_given_non_hiv)
#--------------------------------------------------------------------------------------------------#

#%% 7.Probability Formula
p_premium_given_chrome = 158/2762

p_basic_given_safari = 274/1288

p_free_given_firefox = 2103/2285

more_likely_premium = "Safari"
