#**************************************************************************************************#
#                                                                                                  #
# 01_The_linear_regression_model                                                                   #
#                                                                                                  #
# Authors: S.G.M. Neves                                                                            #
#                                                                                                  #
#**************************************************************************************************#

#%% 1. Instance Based Learning Vs. Model Based Learning
# No code

#--------------------------------------------------------------------------------------------------#

#%% 2. Introduction To The Data
import pandas as pd

data = pd.read_csv('AmesHousing.txt', delimiter='\t')

train = data[:1460]
test = data[1460:]

data.info()

target = 'SalePrice'

#--------------------------------------------------------------------------------------------------#

#%% 3. Simple Linear Regression
import matplotlib.pyplot as plt

fig, axs = plt.subplots(3, 1, figsize=(7,15))
train.plot.scatter(x="Garage Area", y=target, ax=axs[0])
train.plot.scatter(x="Gr Liv Area", y=target, ax=axs[1])
train.plot.scatter(x="Overall Cond", y=target, ax=axs[2])
plt.show()

#--------------------------------------------------------------------------------------------------#

#%% 4. Least Squares
# No code

#--------------------------------------------------------------------------------------------------#

#%% 5. Using Scikit-Learn To Train And Predict
from sklearn.linear_model import LinearRegression

lr = LinearRegression()

lr.fit(train[['Gr Liv Area']], train[target])

a1 = lr.coef_
a0 = lr.intercept_

#--------------------------------------------------------------------------------------------------#

#%% 6. Making Predictions
import numpy as np
from sklearn.metrics import mean_squared_error

predictions  = lr.predict(train[['Gr Liv Area']])
train_rmse = np.sqrt(mean_squared_error(train[target], predictions))

predictions  = lr.predict(test[['Gr Liv Area']])
test_rmse = np.sqrt(mean_squared_error(test[target], predictions))

#--------------------------------------------------------------------------------------------------#

#%% 7. Multiple Linear Regression
cols = ['Overall Cond', 'Gr Liv Area']

lr.fit(train[cols], train[target])

predictions  = lr.predict(train[cols])
train_rmse_2 = np.sqrt(mean_squared_error(train[target], predictions))

predictions  = lr.predict(test[cols])
test_rmse_2 = np.sqrt(mean_squared_error(test[target], predictions))
