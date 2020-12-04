#**************************************************************************************************#
#                                                                                                  #
# 01_Introduction_to_K_nearest_neighbors                                                           #
#                                                                                                  #
# Authors: S.G.M. Neves                                                                            #
#                                                                                                  #
#**************************************************************************************************#

#%% 1. Problem definition
# No code

#--------------------------------------------------------------------------------------------------#

#%% 2. Introduction to the data
import pandas as pd

dc_listings = pd.read_csv("dc_airbnb.csv")
print(dc_listings.iloc[0,:])

#--------------------------------------------------------------------------------------------------#

#%% 3. K-nearest neighbors
# No code

#--------------------------------------------------------------------------------------------------#

#%% 4. Euclidean distance
first_distance  = abs(dc_listings.loc[0,"accommodates"] - 3)
print(first_distance)

#--------------------------------------------------------------------------------------------------#

#%% 5. Calculate distance for all observations
dc_listings["distance"] = (dc_listings["accommodates"] - 3).abs()

print(dc_listings["distance"].value_counts())

#--------------------------------------------------------------------------------------------------#

#%% 6. Randomizing, and sorting
import numpy as np

np.random.seed(1)

dc_listings = dc_listings.iloc[np.random.permutation(dc_listings.shape[0])]

dc_listings = dc_listings.sort_values('distance')

print(dc_listings.iloc[:10,dc_listings.columns.get_loc("price")])

#--------------------------------------------------------------------------------------------------#

#%% 7. Average price
dc_listings["price"] = dc_listings["price"].str.replace(r"[$,]","").astype(float)

mean_price = dc_listings.iloc[:5,dc_listings.columns.get_loc("price")].mean()

print(mean_price)

#--------------------------------------------------------------------------------------------------#

#%% 8. Function to make predictions
dc_listings = pd.read_csv('dc_airbnb.csv')
stripped_commas = dc_listings['price'].str.replace(',', '')
stripped_dollars = stripped_commas.str.replace('$', '')
dc_listings['price'] = stripped_dollars.astype('float')
dc_listings = dc_listings.loc[np.random.permutation(len(dc_listings))]

def predict_price(new_listing):

    temp_df = dc_listings.copy()

    temp_df["distance"] = (temp_df["accommodates"] - new_listing).abs()

    temp_df = temp_df.sort_values('distance')

    mean_price = temp_df.iloc[:5,temp_df.columns.get_loc("price")].mean()

    return mean_price

acc_one = predict_price(1)
acc_two = predict_price(2)
acc_four = predict_price(4)
