#**************************************************************************************************#
#                                                                                                  #
# 01_Understanding_linear_and_nonlinear_functions                                                  #
#                                                                                                  #
# Authors: S.G.M. Neves                                                                            #
#                                                                                                  #
#**************************************************************************************************#

#%% 1. Why Learn Calculus?
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 3, 100)

y = -x**2 + 3*x - 1

plt.plot(x, y)

#--------------------------------------------------------------------------------------------------#

#%% 2. Linear Function
# No code

#--------------------------------------------------------------------------------------------------#

#%% 3. Slope and y-intercept
# No code

#--------------------------------------------------------------------------------------------------#

#%% 4. Math Behind Slope
def slope(x1,x2,y1,y2):

    return (y2 - y1) / (x2 - x1)

slope_one = slope(0,4,1,13)
slope_two = slope(5,-1,16,-2)

#--------------------------------------------------------------------------------------------------#

#%% 5. Nonlinear function
# No code

#--------------------------------------------------------------------------------------------------#

#%% 6. Secant Lines
import seaborn

seaborn.set(style='darkgrid')

def draw_secant(x_vals):

    x_vals = np.array(x_vals)
    plt.figure()

    x = np.linspace(-20, 30, 100)
    y = -x**2 + 3*x - 1
    plt.plot(x, y)

    y_vals = -x_vals**2 + 3*x_vals - 1

    m = slope(x_vals[0], x_vals[1], y_vals[0], y_vals[1])
    b = y_vals[0] - m * x_vals[0]
    y = m*x + b
    plt.plot(x, y, color='green')


    plt.show()

draw_secant([3, 5])
draw_secant([3, 10])
draw_secant([3, 15])

#--------------------------------------------------------------------------------------------------#

#%% 7. Secant Lines And Slope
# No code

#--------------------------------------------------------------------------------------------------#

#%% 8. Tangent Line
# No code
