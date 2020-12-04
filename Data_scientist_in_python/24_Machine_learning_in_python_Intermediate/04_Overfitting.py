#**************************************************************************************************#
#                                                                                                  #
# 04_Overfitting                                                                                   #
#                                                                                                  #
# Authors: S.G.M. Neves                                                                            #
#                                                                                                  #
#**************************************************************************************************#

#%% 1. Introduction
import pandas as pd

columns = ["mpg", "cylinders", "displacement", "horsepower", "weight", "acceleration", "model year", "origin", "car name"]

cars = pd.read_table("auto-mpg.data", sep='\s+', names=columns)

filtered_cars = cars[cars['horsepower'] != '?'].copy()
filtered_cars['horsepower'] = filtered_cars['horsepower'].astype('float')

#--------------------------------------------------------------------------------------------------#

#%% 2. Bias and Variance
# No code

#--------------------------------------------------------------------------------------------------#

#%% 3. Bias-variance tradeoff
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

def train_and_test(cols):

    lr = LinearRegression()

    lr.fit(filtered_cars[cols], filtered_cars['mpg'])

    predictions = lr.predict(filtered_cars[cols])

    mse = mean_squared_error(filtered_cars['mpg'], predictions)

    var = predictions.var()

    return mse, var

cyl_mse, cyl_var = train_and_test(['cylinders'])

weight_mse, weight_var = train_and_test(['weight'])

#--------------------------------------------------------------------------------------------------#

#%% 4. Multivariate models
two_mse, two_var = train_and_test(['cylinders', 'displacement'])
print(two_mse, two_var)

three_mse, three_var = train_and_test(['cylinders', 'displacement', 'horsepower'])
print(three_mse, three_var)

four_mse, four_var = train_and_test(['cylinders', 'displacement', 'horsepower', 'weight'])
print(four_mse, four_var)

five_mse, five_var = train_and_test(['cylinders', 'displacement', 'horsepower', 'weight',
                                     'acceleration'])
print(five_mse, five_var)

six_mse, six_var = train_and_test(['cylinders', 'displacement', 'horsepower', 'weight',
                                   'acceleration', 'model year'])
print(six_mse, six_var)

seven_mse, seven_var = train_and_test(['cylinders', 'displacement', 'horsepower', 'weight',
                                       'acceleration', 'model year', 'origin'])
print(seven_mse, seven_var)

#--------------------------------------------------------------------------------------------------#

#%% 5. Cross validation
from sklearn.model_selection import KFold
import numpy as np

def train_and_cross_val(cols):

    lr = LinearRegression()

    kf = KFold(10, shuffle=True, random_state=3)

    mses = []
    variances = []

    for train_idx, test_idx in kf.split(filtered_cars):

        lr.fit(filtered_cars.loc[train_idx, cols], filtered_cars.loc[train_idx, 'mpg'])

        predictions = lr.predict(filtered_cars.loc[test_idx, cols])

        mses.append(mean_squared_error(filtered_cars.loc[test_idx, 'mpg'], predictions))

        variances.append(predictions.var())

    return np.mean(mses), np.mean(variances)

filtered_cars.reset_index(drop=True, inplace=True)

two_mse, two_var = train_and_cross_val(['cylinders', 'displacement'])
print(two_mse, two_var)

three_mse, three_var = train_and_cross_val(['cylinders', 'displacement', 'horsepower'])
print(three_mse, three_var)

four_mse, four_var = train_and_cross_val(['cylinders', 'displacement', 'horsepower', 'weight'])
print(four_mse, four_var)

five_mse, five_var = train_and_cross_val(['cylinders', 'displacement', 'horsepower', 'weight',
                                     'acceleration'])
print(five_mse, five_var)

six_mse, six_var = train_and_cross_val(['cylinders', 'displacement', 'horsepower', 'weight',
                                   'acceleration', 'model year'])
print(six_mse, six_var)

seven_mse, seven_var = train_and_cross_val(['cylinders', 'displacement', 'horsepower', 'weight',
                                       'acceleration', 'model year', 'origin'])
print(seven_mse, seven_var)

#--------------------------------------------------------------------------------------------------#

#%% 6. Plotting cross-validation error vs. cross-validation variance
import matplotlib.pyplot as plt

n_features = range(2, 8)
mses = [two_mse, three_mse, four_mse, five_mse, six_mse, seven_mse]
variances = [two_var, three_var, four_var, five_var, six_var, seven_var]

plt.scatter(n_features, mses, color='red')
plt.scatter(n_features, variances, color='blue')
plt.show()

#--------------------------------------------------------------------------------------------------#

#%% 7. Conclusion
# No code
