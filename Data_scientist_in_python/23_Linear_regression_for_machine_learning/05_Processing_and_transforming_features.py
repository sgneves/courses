#**************************************************************************************************#
#                                                                                                  #
# 05_Processing_and_transforming_features                                                          #
#                                                                                                  #
# Authors: S.G.M. Neves                                                                            #
#                                                                                                  #
#**************************************************************************************************#

#%% 1. Introduction
import pandas as pd

data = pd.read_csv('AmesHousing.txt', delimiter="\t")
train = data[0:1460].copy()
test = data[1460:].copy()

train_null_counts = train.isnull().sum()
print(train_null_counts)

df_no_mv = train.loc[:,train_null_counts == 0]

#--------------------------------------------------------------------------------------------------#

#%% 2. Categorical Features
text_cols = df_no_mv.select_dtypes(include=['object']).columns

for col in text_cols:

    print(col+":", len(train[col].unique()))

    train[col] = train[col].astype('category')

print(train['Utilities'].cat.codes.value_counts())

#--------------------------------------------------------------------------------------------------#

#%% 3. Dummy Coding
for col in text_cols:

    train = pd.concat([train, pd.get_dummies(train[col])], axis=1)
    del train[col]

#--------------------------------------------------------------------------------------------------#

#%% 4. Transforming Improper Numerical Features
train['years_until_remod'] = train['Year Remod/Add'] - train['Year Built']

#--------------------------------------------------------------------------------------------------#

#%% 5. Missing Values
train_null_counts = train.isnull().sum()

df_missing_values = train.loc[:,(train_null_counts > 0) & (train_null_counts < 584)]

print(train_null_counts)
print(train.dtypes)

#--------------------------------------------------------------------------------------------------#

#%% 6. Imputing Missing Values
float_cols = df_missing_values.select_dtypes(include=['float'])

float_cols = float_cols.fillna(float_cols.mean())
