#**************************************************************************************************#
#                                                                                                  #
# 07_Predicting_the_stock_market                                                                   #
#                                                                                                  #
# Authors: S.G.M. Neves                                                                            #
#                                                                                                  #
#**************************************************************************************************#

#%% 1. The dataset
target = 'Close'

#--------------------------------------------------------------------------------------------------#

#%% 2. Reading in the data
import pandas as pd

sp500 = pd.read_csv('sphist.csv', parse_dates=['Date'])

sp500 = sp500.sort_values('Date').reset_index(drop=True)

#--------------------------------------------------------------------------------------------------#

#%% 3. Generating indicators
sp500['avg_5_day'] = sp500[target].rolling(5).mean().shift()
sp500['avg_365_day'] = sp500[target].rolling(365).mean().shift()
sp500['ratio_5_365'] = sp500['avg_5_day'] / sp500['avg_365_day']

#--------------------------------------------------------------------------------------------------#

#%% 4. Splitting up the data
from datetime import datetime

sp500 = sp500.dropna().reset_index(drop=True)

condition = sp500['Date'] < datetime(2013, 1, 1)

train = sp500[condition]
test = sp500[~condition]

#--------------------------------------------------------------------------------------------------#

#%% 5. Making predictions
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error
import matplotlib.pyplot as plt

features = ['avg_5_day','avg_365_day','ratio_5_365']
lr = LinearRegression()

lr.fit(train[features], train[target])

predictions = lr.predict(test[features])

mae = mean_absolute_error(test[target], predictions)

plt.plot(test['Date'], test[target], color='blue', label='actual')
plt.plot(test['Date'], predictions, color='red', label='predicted')
plt.legend()
plt.show()

#--------------------------------------------------------------------------------------------------#

#%% 6. Improving error
