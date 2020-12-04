#**************************************************************************************************#
#                                                                                                  #
# 04_Hyperparameter_optimization                                                                   #
#                                                                                                  #
# Authors: S.G.M. Neves                                                                            #
#                                                                                                  #
#**************************************************************************************************#

#%% 1. Recap
import pandas as pd

train_df = pd.read_csv("dc_airbnb_train.csv")

test_df = pd.read_csv("dc_airbnb_test.csv")

#--------------------------------------------------------------------------------------------------#

#%% 2. Hyperparameter optimization
import sklearn

features = ['accommodates', 'bedrooms', 'bathrooms', 'number_of_reviews']
mse_values = []

for i in range(1,6):

    knn = sklearn.neighbors.KNeighborsRegressor(n_neighbors=i, algorithm='brute')

    knn.fit(train_df[features], train_df["price"])

    predictions  = knn.predict(test_df[features])

    mse_values.append(sklearn.metrics.mean_squared_error(test_df["price"], predictions))

print(mse_values)

#--------------------------------------------------------------------------------------------------#

#%% 3. Expanding grid search
mse_values = []

for i in range(1,21):

    knn = sklearn.neighbors.KNeighborsRegressor(n_neighbors=i, algorithm='brute')

    knn.fit(train_df[features], train_df["price"])

    predictions  = knn.predict(test_df[features])

    mse_values.append(sklearn.metrics.mean_squared_error(test_df["price"], predictions))

print(mse_values)

#--------------------------------------------------------------------------------------------------#

#%% 4. Visualizing hyperparameter values
import matplotlib.pyplot as plt

plt.scatter(range(1,21), mse_values)
plt.show()

#--------------------------------------------------------------------------------------------------#

#%% 5. Varying Hyperparameters
features = train_df.columns.drop("price")
mse_values = []

for i in range(1,21):

    knn = sklearn.neighbors.KNeighborsRegressor(n_neighbors=i, algorithm='brute')

    knn.fit(train_df[features], train_df["price"])

    predictions  = knn.predict(test_df[features])

    mse_values.append(sklearn.metrics.mean_squared_error(test_df["price"], predictions))

plt.scatter(range(1,21), mse_values)
plt.show()

#--------------------------------------------------------------------------------------------------#

#%% 6. Practice the workflow
import numpy as np

features = ['accommodates', 'bathrooms']
mse_values = []

for i in range(1,21):

    knn = sklearn.neighbors.KNeighborsRegressor(n_neighbors=i, algorithm='brute')

    knn.fit(train_df[features], train_df["price"])

    predictions  = knn.predict(test_df[features])

    mse_values.append(sklearn.metrics.mean_squared_error(test_df["price"], predictions))

two_hyp_mse = {np.argmin(mse_values) + 1: np.min(mse_values)}

features = ['accommodates', 'bathrooms', 'bedrooms']
mse_values = []

for i in range(1,21):

    knn = sklearn.neighbors.KNeighborsRegressor(n_neighbors=i, algorithm='brute')

    knn.fit(train_df[features], train_df["price"])

    predictions  = knn.predict(test_df[features])

    mse_values.append(sklearn.metrics.mean_squared_error(test_df["price"], predictions))

three_hyp_mse = {np.argmin(mse_values) + 1: np.min(mse_values)}
