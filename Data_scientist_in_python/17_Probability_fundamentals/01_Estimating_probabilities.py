#**************************************************************************************************#
#                                                                                                  #
# 01_Estimating_probabilities                                                                      #
#                                                                                                  #
# Authors: S.G.M. Neves                                                                            #
#                                                                                                  #
#**************************************************************************************************#

#%% 1. Introduction
# No code

#--------------------------------------------------------------------------------------------------#

#%% 2. The Empirical Probability
p_tail = 1 - 0.56
print(p_tail)

p_six = 28 / 200
print(p_six)

p_odd = 102 / 200
print(p_odd)

#--------------------------------------------------------------------------------------------------#

#%% 3. Probability as Relative Frequency
p_heads_1 = 1 - 162 / 300

percentage_1 = p_heads_1 * 100

p_heads_2 = 1 - 2450 / 5000

percentage_2 = p_heads_2 * 100

#--------------------------------------------------------------------------------------------------#

#%% 4. Repeating an Experiment
from numpy.random import seed, randint

n = 10000
seed(1)
heads = 0
probabilities = []

def coin_toss():
    if randint(0,2) == 1:
        return 'HEAD'
    else:
        return 'TAIL'

for i in range(1,10001):

    outcome = coin_toss()

    if outcome == 'HEAD': heads += 1

    current_probability = heads / i
    probabilities.append(current_probability)

print(probabilities[:10])
print(probabilities[-10:])

#--------------------------------------------------------------------------------------------------#

#%% 5. The True Probability Value
p_l = 87 / 200

p_l_and_c = 40 / 200

p_h = 63 / 200

p_no = 1 - 160 / 200

#--------------------------------------------------------------------------------------------------#

#%% 6. The Theoretical Probability
p_5 = 1 / 6

p_ht = 1 / 4

p_tt = 1 / 4

#--------------------------------------------------------------------------------------------------#

#%% 7. Events vs. Outcomes
p_even = 3 / 6

p_odd_no_3 = 2 / 6

p_odd_greater_5 = 0

#--------------------------------------------------------------------------------------------------#

#%% 8. A Biased Die
p_blue = 10 / 100

p_red = 90 / 100
