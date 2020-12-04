#**************************************************************************************************#
#                                                                                                  #
# 04_Permutations_and_combinations                                                                 #
#                                                                                                  #
# Authors: S.G.M. Neves                                                                            #
#                                                                                                  #
#**************************************************************************************************#

#%% 1. The Rule of Product
n_outcomes = 6**2

p_six_six = 1 / n_outcomes

p_not_five_five = 1 - 1 / n_outcomes

#--------------------------------------------------------------------------------------------------#

#%% 2. Extended Rule of Product
total_outcomes = 6**3 * 52

p_666_ace_diamonds = 1 / total_outcomes

p_no_666_ace_diamonds = 1 - p_666_ace_diamonds

#--------------------------------------------------------------------------------------------------#

#%% 3. Example Walkthrough
p_crack_4 = 1 / 10**4

p_crack_6 = 1 / 10**6

#--------------------------------------------------------------------------------------------------#

#%% 4. Permutations
def factorial(n):

    product = 1

    for i in range(2, n+1):
        product *= i

    return product

permutations_1 = factorial(6)

permutations_2 = factorial(52)

#--------------------------------------------------------------------------------------------------#

#%% 5. More About Permutations
perm_3_52 = 52 * 51 * 50

perm_4_20 = 20 * 19 * 18 * 17

perm_4_27 = 27 * 26 * 25 * 24

#--------------------------------------------------------------------------------------------------#

#%% 6. Permutations Formulas
def permutation(n, k):

    return factorial(n) / factorial(n - k)

p_crack_pass = 1 / permutation(127,  16)

#--------------------------------------------------------------------------------------------------#

#%% 7. Unique Arrangements
c = permutation(52,  5) / factorial(5)

p_aces_7 = 1 / c

c_lottery = permutation(49,  6) / factorial(6)

p_big_prize = 1 / c_lottery

#--------------------------------------------------------------------------------------------------#

#%% 8. Combinations
def combinations(n, k):

    return factorial(n) / (factorial(k) * factorial(n - k))

c_18 = combinations(34, 18)

p_non_Y = 1 - 1/c_18
