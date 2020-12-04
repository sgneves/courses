#**************************************************************************************************#
#                                                                                                  #
# 02_Nonlinear_activation_functions                                                                #
#                                                                                                  #
# Authors: S.G.M. Neves                                                                            #
#                                                                                                  #
#**************************************************************************************************#

#%% 1. Introduction To Activation Functions
# No code

#--------------------------------------------------------------------------------------------------#

#%% 2. ReLU Activation Function
import matplotlib.pyplot as plt
import numpy as np

def relu(x):

    y = x.copy()
    y[y < 0] = 0

    return y

x = np.linspace(-2, 2, 20)
relu_y = relu(x)

print(x)
print(relu_y)

plt.plot(x, relu_y)
plt.show()

#--------------------------------------------------------------------------------------------------#

#%% 3. Trigonometric Functions
x = np.linspace(-2*np.pi, 2*np.pi, 100)

tan_y = np.tan(x)

print(x)
print(tan_y)

plt.plot(x, tan_y)
plt.show()

#--------------------------------------------------------------------------------------------------#

#%% 4. Reflecting On The Tangent Function
# No code

#--------------------------------------------------------------------------------------------------#

#%% 5. Hyperbolic Tangent Function
x = np.linspace(-40, 40, 100)

tanh_y = np.tanh(x)

print(x)
print(tanh_y)

plt.plot(x, tanh_y)
plt.show()

#--------------------------------------------------------------------------------------------------#

#%% 6. Reflecting On The Hyperbolic Tangent Function
# No code
