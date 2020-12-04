#**************************************************************************************************#
#                                                                                                  #
# 05_Cross_validation                                                                              #
#                                                                                                  #
# Authors: S.G.M. Neves                                                                            #
#                                                                                                  #
#**************************************************************************************************#

#%% 1. Introduction
import numpy as np
import pandas as pd

dc_listings = pd.read_csv("dc_airbnb.csv")
stripped_commas = dc_listings['price'].str.replace(',', '')
stripped_dollars = stripped_commas.str.replace('$', '')
dc_listings['price'] = stripped_dollars.astype('float')

dc_listings = dc_listings.iloc[np.random.permutation(dc_listings.shape[0])]

split_one = dc_listings.iloc[:1862].copy()
split_two = dc_listings.iloc[1862:].copy()

#--------------------------------------------------------------------------------------------------#

#%% 2. Holdout Validation
from sklearn.neighbors import KNeighborsRegressor
from sklearn.metrics import mean_squared_error

train_one = split_one
test_one = split_two
train_two = split_two
test_two = split_one

model = KNeighborsRegressor()

model.fit(train_one[["accommodates"]], train_one["price"])

predictions = model.predict(test_one[["accommodates"]])

iteration_one_rmse = np.sqrt(mean_squared_error(test_one["price"], predictions))

model.fit(train_two[["accommodates"]], train_two["price"])

predictions = model.predict(test_two[["accommodates"]])

iteration_two_rmse = np.sqrt(mean_squared_error(test_two["price"], predictions))

avg_rmse = np.mean([iteration_one_rmse, iteration_two_rmse])

#--------------------------------------------------------------------------------------------------#

#%% 3. K-Fold Cross Validation
dc_listings.loc[dc_listings.index[0:745], "fold"] = 1
dc_listings.loc[dc_listings.index[745:1490], "fold"] = 2
dc_listings.loc[dc_listings.index[1490:2234], "fold"] = 3
dc_listings.loc[dc_listings.index[2234:2978], "fold"] = 4
dc_listings.loc[dc_listings.index[2978:3723], "fold"] = 5

print(dc_listings["fold"].value_counts())

print(dc_listings["fold"].isnull().sum())

#--------------------------------------------------------------------------------------------------#

#%% 4. First iteration
model = KNeighborsRegressor()

train = dc_listings.loc[dc_listings["fold"].isin(range(2,6))]
test = dc_listings[dc_listings["fold"] == 1]

model.fit(train[["accommodates"]], train["price"])

predictions = model.predict(test[["accommodates"]])

iteration_one_rmse = np.sqrt(mean_squared_error(test["price"], predictions))

#--------------------------------------------------------------------------------------------------#

#%% 5. Function for training models
def train_and_validate(df, folds):

    rmses  = []

    for fold in folds:

        train = df.loc[df["fold"].isin([x for x in folds if x != fold])]
        test = df[df["fold"] == fold]

        model.fit(train[["accommodates"]], train["price"])

        predictions = model.predict(test[["accommodates"]])

        rmses.append(np.sqrt(mean_squared_error(test["price"], predictions)))

    return rmses

rmses = train_and_validate(dc_listings, list(range(1,6)))
print(rmses)

avg_rmse = np.mean(rmses)
print(avg_rmse)

#--------------------------------------------------------------------------------------------------#

#%% 6. Performing K-Fold Cross Validation Using Scikit-Learn
from sklearn.model_selection import cross_val_score, KFold

kf = KFold(5, shuffle=True, random_state=1)

knn = KNeighborsRegressor()

mses = cross_val_score(knn, dc_listings[["accommodates"]], dc_listings["price"],
                       scoring="neg_mean_squared_error", cv=kf)

avg_rmse = np.sqrt(abs(mses)).mean()

#--------------------------------------------------------------------------------------------------#

#%% 7. Exploring Different K Values
from sklearn.model_selection import cross_val_score, KFold

num_folds = [3, 5, 7, 9, 10, 11, 13, 15, 17, 19, 21, 23]

for fold in num_folds:
    kf = KFold(fold, shuffle=True, random_state=1)
    model = KNeighborsRegressor()
    mses = cross_val_score(model, dc_listings[["accommodates"]], dc_listings["price"], scoring="neg_mean_squared_error", cv=kf)
    rmses = np.sqrt(np.absolute(mses))
    avg_rmse = np.mean(rmses)
    std_rmse = np.std(rmses)
    print(str(fold), "folds: ", "avg RMSE: ", str(avg_rmse), "std RMSE: ", str(std_rmse))

#--------------------------------------------------------------------------------------------------#

#%% 8. Bias-Variance Tradeoff
# No code
