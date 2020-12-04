#**************************************************************************************************#
#                                                                                                  #
# 03_Applying_decision_trees                                                                       #
#                                                                                                  #
# Authors: S.G.M. Neves                                                                            #
#                                                                                                  #
#**************************************************************************************************#

#%% 1. Introduction to the Data Set
# No code

#--------------------------------------------------------------------------------------------------#

#%% 2. Using Decision Trees With scikit-learn
import pandas as pd
from sklearn.tree import DecisionTreeClassifier

# Read the dataset
income = pd.read_csv("income.csv", index_col=False)

cols = income.select_dtypes('object').columns
income[cols] = income[cols].apply(lambda col: pd.Categorical(col).codes)

# A list of columns to train with
columns = ["age", "workclass", "education_num", "marital_status", "occupation", "relationship", "race", "sex", "hours_per_week", "native_country"]

# Instantiate the classifier
# Set random_state to 1 to make sure the results are consistent
clf = DecisionTreeClassifier(random_state=1)

# We've already loaded the variable "income," which contains all of the income data
clf.fit(income[columns], income['high_income'])

#--------------------------------------------------------------------------------------------------#

#%% 3. Splitting the Data into Train and Test Sets
import numpy as np
import math

# Set a random seed so the shuffle is the same every time
np.random.seed(1)

# Shuffle the rows
# This permutes the index randomly using numpy.random.permutation
# Then, it reindexes the dataframe with the result
# The net effect is to put the rows into random order
income = income.reindex(np.random.permutation(income.index))

train_max_row = math.floor(income.shape[0] * .8)

train = income.iloc[:train_max_row]
test = income.iloc[train_max_row:]

#--------------------------------------------------------------------------------------------------#

#%% 4. Evaluating Error With AUC
from sklearn.metrics import roc_auc_score

clf = DecisionTreeClassifier(random_state=1)

clf.fit(train[columns], train["high_income"])

predictions = clf.predict(test[columns])

error = roc_auc_score(test['high_income'], predictions)
print(error)

#--------------------------------------------------------------------------------------------------#

#%% 5. Computing Error on the Training Set
predictions = clf.predict(train[columns])

error = roc_auc_score(train['high_income'], predictions)
print(error)

#--------------------------------------------------------------------------------------------------#

#%% 6. Decision Tree Overfitting
# No code

#--------------------------------------------------------------------------------------------------#

#%% 7. Reducing Overfitting With a Shallower Tree
clf = DecisionTreeClassifier(min_samples_split=13, random_state=1)

clf.fit(train[columns], train["high_income"])

train_auc = roc_auc_score(train['high_income'], clf.predict(train[columns]))
print(train_auc)

test_auc = roc_auc_score(test['high_income'], clf.predict(test[columns]))
print(test_auc)

#--------------------------------------------------------------------------------------------------#

#%% 8. Tweaking Parameters to Adjust AUC
clf = DecisionTreeClassifier(min_samples_split=13, max_depth=7, random_state=1)

clf.fit(train[columns], train["high_income"])

train_auc = roc_auc_score(train['high_income'], clf.predict(train[columns]))
print(train_auc)

test_auc = roc_auc_score(test['high_income'], clf.predict(test[columns]))
print(test_auc)

#--------------------------------------------------------------------------------------------------#

#%% 9. Tweaking Tree Depth to Adjust AUC
clf = DecisionTreeClassifier(min_samples_split=100, max_depth=2, random_state=1)

clf.fit(train[columns], train["high_income"])

train_auc = roc_auc_score(train['high_income'], clf.predict(train[columns]))
print(train_auc)

test_auc = roc_auc_score(test['high_income'], clf.predict(test[columns]))
print(test_auc)

#--------------------------------------------------------------------------------------------------#

#%% 10. Underfitting in Simplistic Trees
# No code

#--------------------------------------------------------------------------------------------------#

#%% 11. The Bias-Variance Tradeoff
# No code

#--------------------------------------------------------------------------------------------------#

#%% 12. Exploring Decision Tree Variance
np.random.seed(1)

# Generate a column containing random numbers from 0 to 4
income["noise"] = np.random.randint(4, size=income.shape[0])

# Adjust "columns" to include the noise column
columns = ["noise", "age", "workclass", "education_num", "marital_status", "occupation",
           "relationship", "race", "sex", "hours_per_week", "native_country"]

# Make new train and test sets
train_max_row = math.floor(income.shape[0] * .8)
train = income.iloc[:train_max_row]
test = income.iloc[train_max_row:]

# Initialize the classifier
clf = DecisionTreeClassifier(random_state=1)

# Fit the classifier to the training data
clf.fit(train[columns], train["high_income"])

# Make predictions on the training set and compute the AUC
train_auc = roc_auc_score(train['high_income'], clf.predict(train[columns]))
print(train_auc)

# Make predictions on the test set and compute the AUC
test_auc = roc_auc_score(test['high_income'], clf.predict(test[columns]))
print(test_auc)

#--------------------------------------------------------------------------------------------------#

#%% 13. Pruning Leaves to Prevent Overfitting
# No code

#--------------------------------------------------------------------------------------------------#

#%% 14. Knowing When to Use Decision Trees
# No code
