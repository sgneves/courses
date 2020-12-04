#**************************************************************************************************#
#                                                                                                  #
# 03_Multivariate__K_nearest_neighbors                                                             #
#                                                                                                  #
# Authors: S.G.M. Neves                                                                            #
#                                                                                                  #
#**************************************************************************************************#

#%% 1. Recap
import pandas as pd
import numpy as np
np.random.seed(1)

dc_listings = pd.read_csv('dc_airbnb.csv')
dc_listings = dc_listings.loc[np.random.permutation(len(dc_listings))]
stripped_commas = dc_listings['price'].str.replace(',', '')
stripped_dollars = stripped_commas.str.replace('$', '')
dc_listings['price'] = stripped_dollars.astype('float')

dc_listings.info()

#--------------------------------------------------------------------------------------------------#

#%% 2. Removing features
dc_listings.drop(["room_type", "city", "state", "latitude", "longitude", "zipcode",
                  "host_response_rate", "host_acceptance_rate", "host_listings_count"], axis=1,
                 inplace = True)

#--------------------------------------------------------------------------------------------------#

#%% 3. Handling missing values
dc_listings.drop(["cleaning_fee", "security_deposit"], axis=1,
                 inplace = True)

dc_listings.dropna(inplace = True)

dc_listings.info()

#--------------------------------------------------------------------------------------------------#

#%% 4. Normalize columns
normalized_listings = (dc_listings - dc_listings.mean()) / (dc_listings.std())

normalized_listings["price"] = dc_listings["price"]

print(normalized_listings.head(3))

#--------------------------------------------------------------------------------------------------#

#%% 5. Euclidean distance for multivariate case
from scipy.spatial import distance

cols = [normalized_listings.columns.get_loc("accommodates"),
        normalized_listings.columns.get_loc("bathrooms")]


first_fifth_distance = distance.euclidean(normalized_listings.iloc[0,cols],
                                          normalized_listings.iloc[4,cols])

#--------------------------------------------------------------------------------------------------#

#%% 6. Introduction to scikit-learn
# No code

#--------------------------------------------------------------------------------------------------#

#%% 7. Fitting a model and making predictions
from sklearn.neighbors import KNeighborsRegressor

# Divide dataset into training and test data
train_df = normalized_listings.iloc[0:2792]
test_df = normalized_listings.iloc[2792:]

# Instantiate an empty model
knn = KNeighborsRegressor(algorithm='brute')

# Fit the model using the training data and target values
knn.fit(train_df[["accommodates","bathrooms"]], train_df["price"])

# Predicted the values for the test set
predictions = knn.predict(test_df[['accommodates', 'bathrooms']])

#--------------------------------------------------------------------------------------------------#

#%% 8. Calculating MSE using Scikit-Learn
import sklearn

two_features_mse = sklearn.metrics.mean_squared_error(test_df["price"], predictions)
print(two_features_mse)

two_features_rmse = np.sqrt(two_features_mse)
print(two_features_rmse)

#--------------------------------------------------------------------------------------------------#

#%% 9. 9.Using more features
features = ['accommodates', 'bedrooms', 'bathrooms', 'number_of_reviews']

knn.fit(train_df[features], train_df["price"])

four_predictions  = knn.predict(test_df[features])

four_mse = sklearn.metrics.mean_squared_error(test_df["price"], four_predictions)
print(four_mse)

four_rmse  = np.sqrt(four_mse)
print(four_rmse)

#--------------------------------------------------------------------------------------------------#

#%% 10. Using all features
features = train_df.columns.drop("price")

knn.fit(train_df[features], train_df["price"])

all_features_predictions = knn.predict(test_df[features])

all_features_mse  = sklearn.metrics.mean_squared_error(test_df["price"], all_features_predictions)
print(all_features_mse)

all_features_rmse  = np.sqrt(all_features_mse)
print(all_features_rmse)
