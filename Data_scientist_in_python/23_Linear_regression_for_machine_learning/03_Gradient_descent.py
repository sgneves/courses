#**************************************************************************************************#
#                                                                                                  #
# 03_Gradient_descent                                                                              #
#                                                                                                  #
# Authors: S.G.M. Neves                                                                            #
#                                                                                                  #
#**************************************************************************************************#

#%% 1. Introduction
# No code

#--------------------------------------------------------------------------------------------------#

#%% 2. Single Variable Gradient Descent
# No code

#--------------------------------------------------------------------------------------------------#

#%% 3. Derivative Of The Cost Function
import pandas as pd

data = pd.read_csv('AmesHousing.txt', delimiter='\t')

train = data[:1460]
test = data[1460:]

def derivative(a1, xi_list, yi_list):

    return 2 / len(xi_list) * (xi_list * (a1 * xi_list - yi_list)).sum()

def gradient_descent(xi_list, yi_list, max_iterations, alpha, a1_initial):

    a1_list = [a1_initial]

    for i in range(0, max_iterations):
        a1 = a1_list[i]
        deriv = derivative(a1, xi_list, yi_list)
        a1_new = a1 - alpha*deriv
        a1_list.append(a1_new)

    return(a1_list)

param_iterations = gradient_descent(train['Gr Liv Area'], train['SalePrice'], 20, .0000003, 150)
final_param = param_iterations[-1]

#--------------------------------------------------------------------------------------------------#

#%% 4. Understanding Multi Parameter Gradient Descent
# No code

#--------------------------------------------------------------------------------------------------#

#%% 5. Gradient Of The Cost Function
def a1_derivative(a0, a1, xi_list, yi_list):

    len_data = len(xi_list)
    error = 0
    for i in range(0, len_data):
        error += xi_list[i]*(a0 + a1*xi_list[i] - yi_list[i])
    deriv = 2*error/len_data
    return deriv

def a0_derivative(a0, a1, xi_list, yi_list):

    return 2 / len(xi_list) * (a0 + a1 * xi_list - yi_list).sum()

def gradient_descent(xi_list, yi_list, max_iterations, alpha, a1_initial, a0_initial):

    a1_list = [a1_initial]
    a0_list = [a0_initial]

    for i in range(0, max_iterations):
        a1 = a1_list[i]
        a0 = a0_list[i]

        a1_deriv = a1_derivative(a0, a1, xi_list, yi_list)
        a0_deriv = a0_derivative(a0, a1, xi_list, yi_list)

        a1_new = a1 - alpha*a1_deriv
        a0_new = a0 - alpha*a0_deriv

        a1_list.append(a1_new)
        a0_list.append(a0_new)
    return(a0_list, a1_list)

a0_params, a1_params = gradient_descent(train['Gr Liv Area'], train['SalePrice'], 20, .0000003,
                                        150, 1000)

#--------------------------------------------------------------------------------------------------#

#%% 6. Gradient Descent For Higher Dimensions
# No code
