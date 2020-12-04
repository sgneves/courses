#**************************************************************************************************#
#                                                                                                  #
# 04_Ordinary_least_squares                                                                        #
#                                                                                                  #
# Authors: S.G.M. Neves                                                                            #
#                                                                                                  #
#**************************************************************************************************#

#%% 1. Introduction
import numpy as np
import pandas as pd

data = pd.read_csv('AmesHousing.txt', delimiter="\t")

train = data[0:1460]
test = data[1460:]

features = ['Wood Deck SF', 'Fireplaces', 'Full Bath', '1st Flr SF', 'Garage Area',
       'Gr Liv Area', 'Overall Qual']

X = pd.concat([pd.Series([1]*train.shape[0], name='bias'), train[features]], axis=1)

y = train['SalePrice']

ols_estimation = np.dot(np.dot(np.linalg.inv(np.dot(X.transpose(), X)), X.transpose()), y)

#--------------------------------------------------------------------------------------------------#

#%% 2. Cost Function
# No code

#--------------------------------------------------------------------------------------------------#

#%% 3. Derivative Of The Cost Function
# No code

#--------------------------------------------------------------------------------------------------#

#%% 4. Gradient Descent vs. Ordinary Least Squares
# No code
