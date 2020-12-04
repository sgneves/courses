#**************************************************************************************************#
#                                                                                                  #
# 03_Multiclass_classification                                                                     #
#                                                                                                  #
# Authors: S.G.M. Neves                                                                            #
#                                                                                                  #
#**************************************************************************************************#

#%% 1. Introduction to the data
import pandas as pd

cars = pd.read_csv("auto.csv")

unique_regions = cars['origin'].unique()
print(unique_regions)

#--------------------------------------------------------------------------------------------------#

#%% 2. Dummy variables
cars = pd.concat([cars, pd.get_dummies(cars["cylinders"], prefix="cyl")], axis=1)

cars = pd.concat([cars, pd.get_dummies(cars["year"], prefix="year")], axis=1)

cars.drop(['cylinders','year'], axis=1, inplace=True)

#--------------------------------------------------------------------------------------------------#

#%% 3. Multiclass classification
import numpy as np

shuffled_rows = np.random.permutation(cars.index)
shuffled_cars = cars.iloc[shuffled_rows]

k_row = round(0.7 * shuffled_cars.shape[0])
train = shuffled_cars[:k_row]
test = shuffled_cars[k_row:]

#--------------------------------------------------------------------------------------------------#

#%% 4. Training a multiclass logistic regression model
from sklearn.linear_model import LogisticRegression

unique_origins = cars["origin"].unique()
unique_origins.sort()

features = ([col for col in cars.columns if 'cyl' in col]
            + [col for col in cars.columns if 'year' in col])

models = {}

for origin in unique_origins:

    model = LogisticRegression()

    models[origin] = model.fit(cars[features], cars['origin'] == origin)

#--------------------------------------------------------------------------------------------------#

#%% 5. Testing the models
testing_probs = pd.DataFrame(columns=unique_origins)

for origin in unique_origins:

    testing_probs[origin] = models[origin].predict_proba(test[features])[:,1]

#--------------------------------------------------------------------------------------------------#

#%% 6. Choose the origin
predicted_origins = testing_probs.idxmax(1)
print(predicted_origins)
