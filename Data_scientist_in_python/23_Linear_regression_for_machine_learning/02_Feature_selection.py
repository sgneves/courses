#**************************************************************************************************#
#                                                                                                  #
# 02_Feature_selection                                                                             #
#                                                                                                  #
# Authors: S.G.M. Neves                                                                            #
#                                                                                                  #
#**************************************************************************************************#

#%% 1. Missing Values
import numpy as np
import pandas as pd

data = pd.read_csv('AmesHousing.txt', delimiter="\t")

train = data[0:1460]
test = data[1460:]

numerical_train = train.select_dtypes(np.number).copy()

cols = ['PID','Year Built','Year Remod/Add','Garage Yr Blt','Mo Sold','Yr Sold']
numerical_train.drop(cols, axis=1, inplace=True)

null_series = numerical_train.isnull().sum()

full_cols_series = null_series[null_series == 0]
print(full_cols_series)

#--------------------------------------------------------------------------------------------------#

#%% 2. Correlating Feature Columns With Target Column
train_subset = train[full_cols_series.index].copy()

sorted_corrs = train_subset.corr()["SalePrice"].abs().sort_values()

#--------------------------------------------------------------------------------------------------#

#%% 3. Correlation Matrix Heatmap
import seaborn as sns

strong_corrs = sorted_corrs[sorted_corrs > 0.3]

train_subset = train_subset[strong_corrs.index].copy()

sns.heatmap(train_subset.corr())

#--------------------------------------------------------------------------------------------------#

#%% 4. Train And Test Model
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

final_corr_cols = strong_corrs.drop(['Garage Cars', 'TotRms AbvGrd'])
features = final_corr_cols.drop(['SalePrice']).index
target = 'SalePrice'

train = train[final_corr_cols.index].copy()

test = test[final_corr_cols.index].copy()
test.dropna(inplace=True)

lr = LinearRegression()

lr.fit(train[features], train[target])

predictions  = lr.predict(train[features])
train_rmse = np.sqrt(mean_squared_error(train[target], predictions))

predictions  = lr.predict(test[features])
test_rmse = np.sqrt(mean_squared_error(test[target], predictions))

#--------------------------------------------------------------------------------------------------#

#%% 5. Removing Low Variance Features
unit_train = train[features]
unit_train = (unit_train - unit_train.min()) / (unit_train.max() - unit_train.min())

print(unit_train.max())
print(unit_train.min())

#--------------------------------------------------------------------------------------------------#

#%% 6. Final Model
clean_test = test[final_corr_cols.index].dropna()

features = features.drop("Open Porch SF")

lr.fit(train[features], train[target])

predictions  = lr.predict(train[features])
train_rmse_2 = np.sqrt(mean_squared_error(train[target], predictions))

predictions  = lr.predict(clean_test[features])
test_rmse_2 = np.sqrt(mean_squared_error(clean_test[target], predictions))
