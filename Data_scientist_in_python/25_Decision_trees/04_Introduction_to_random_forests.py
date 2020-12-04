#**************************************************************************************************#
#                                                                                                  #
# 04_Introduction_to_random_forests                                                                #
#                                                                                                  #
# Authors: S.G.M. Neves                                                                            #
#                                                                                                  #
#**************************************************************************************************#

#%% 1. Introduction
# No code

#--------------------------------------------------------------------------------------------------#

#%% 2. Combining Model Predictions With Ensembles
import math
import numpy as np
import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import roc_auc_score

income = pd.read_csv("income.csv", index_col=False)

cols = income.select_dtypes('object').columns
income[cols] = income[cols].apply(lambda col: pd.Categorical(col).codes)

np.random.seed(1)

income = income.reindex(np.random.permutation(income.index))

train_max_row = math.floor(income.shape[0] * .8)

train = income.iloc[:train_max_row]
test = income.iloc[train_max_row:]

columns = ["age", "workclass", "education_num", "marital_status", "occupation", "relationship", "race", "sex", "hours_per_week", "native_country"]

clf = DecisionTreeClassifier(random_state=1, min_samples_leaf=2)
clf.fit(train[columns], train["high_income"])

clf2 = DecisionTreeClassifier(random_state=1, max_depth=5)
clf2.fit(train[columns], train["high_income"])

print(roc_auc_score(test['high_income'], clf.predict(test[columns])))

print(roc_auc_score(test['high_income'], clf2.predict(test[columns])))

#--------------------------------------------------------------------------------------------------#

#%% 3. Combining Our Predictions
# No code

#--------------------------------------------------------------------------------------------------#

#%% 4. Combining Our Predictions
predictions = clf.predict_proba(test[columns])[:,1]
predictions2 = clf2.predict_proba(test[columns])[:,1]

print(roc_auc_score(test['high_income'], np.round((predictions + predictions2)/2)))

#--------------------------------------------------------------------------------------------------#

#%% 5. Why Ensembling Works
# No code

#--------------------------------------------------------------------------------------------------#

#%% 6. Introducing Variation With Bagging

# We'll build 10 trees
tree_count = 10

# Each "bag" will have 60% of the number of original rows
bag_proportion = .6

predictions = []

for i in range(tree_count):

    # We select 60% of the rows from train, sampling with replacement
    # We set a random state to ensure we'll be able to replicate our results
    # We set it to i instead of a fixed value so we don't get the same sample in every loop
    # That would make all of our trees the same
    bag = train.sample(frac=bag_proportion, replace=True, random_state=i)

    # Fit a decision tree model to the "bag"
    clf = DecisionTreeClassifier(random_state=1, min_samples_leaf=2)
    clf.fit(bag[columns], bag["high_income"])

    # Using the model, make predictions on the test data
    predictions.append(clf.predict_proba(test[columns])[:,1])

print(roc_auc_score(test['high_income'], np.round(pd.DataFrame(predictions).mean())))

#--------------------------------------------------------------------------------------------------#

#%% 7. Selecting Random Features

# Create the data set that we used two missions ago
data = pd.DataFrame([
    [0,4,20,0],
    [0,4,60,2],
    [0,5,40,1],
    [1,4,25,1],
    [1,5,35,2],
    [1,5,55,1]
    ])

data.columns = ["high_income", "employment", "age", "marital_status"]

# Set a random seed to make the results reproducible
np.random.seed(1)

# The dictionary to store our tree
tree = {}
nodes = []

def calc_entropy(column):
    """
    Calculate entropy given a pandas series, list, or numpy array.
    """
    # Compute the counts of each unique value in the column
    counts = np.bincount(column)
    # Divide by the total column length to get a probability
    probabilities = counts / len(column)

    # Initialize the entropy to 0
    entropy = 0
    # Loop through the probabilities, and add each one to the total entropy
    for prob in probabilities:
        if prob > 0:
            entropy += prob * math.log(prob, 2)

    return -entropy

def calc_information_gain(data, split_name, target_name):
    """
    Calculate information gain given a data set, column to split on, and target
    """
    # Calculate the original entropy
    original_entropy = calc_entropy(data[target_name])

    # Find the median of the column we're splitting
    column = data[split_name]
    median = column.median()

    # Make two subsets of the data, based on the median
    left_split = data[column <= median]
    right_split = data[column > median]

    # Loop through the splits and calculate the subset entropies
    to_subtract = 0
    for subset in [left_split, right_split]:
        prob = (subset.shape[0] / data.shape[0])
        to_subtract += prob * calc_entropy(subset[target_name])

    # Return information gain
    return original_entropy - to_subtract

# The function to find the column to split on
def find_best_column(data, target_name, columns):
    information_gains = []

    columns_sample = np.random.choice(columns, 2)

    for col in columns_sample:
        information_gain = calc_information_gain(data, col, "high_income")
        information_gains.append(information_gain)

    # Find the name of the column with the highest gain
    highest_gain_index = information_gains.index(max(information_gains))
    highest_gain = columns_sample[highest_gain_index]
    return highest_gain

# The function to construct an ID3 decision tree
def id3(data, target, columns, tree):
    unique_targets = pd.unique(data[target])
    nodes.append(len(nodes) + 1)
    tree["number"] = nodes[-1]

    if len(unique_targets) == 1:
        if 0 in unique_targets:
            tree["label"] = 0
        elif 1 in unique_targets:
            tree["label"] = 1
        return

    best_column = find_best_column(data, target, columns)
    column_median = data[best_column].median()

    tree["column"] = best_column
    tree["median"] = column_median

    left_split = data[data[best_column] <= column_median]
    right_split = data[data[best_column] > column_median]
    split_dict = [["left", left_split], ["right", right_split]]

    for name, split in split_dict:
        tree[name] = {}
        id3(split, target, columns, tree[name])

# Run the ID3 algorithm on our data set and print the resulting tree
id3(data, "high_income", ["employment", "age", "marital_status"], tree)
print(tree)

#--------------------------------------------------------------------------------------------------#

#%% 8. Random Subsets in scikit-learn

# We'll build 10 trees
tree_count = 10

# Each "bag" will have 60% of the number of original rows
bag_proportion = .6

predictions = []

for i in range(tree_count):
    # We select 60% of the rows from train, sampling with replacement
    # We set a random state to ensure we'll be able to replicate our results
    # We set it to i instead of a fixed value so we don't get the same sample every time
    bag = train.sample(frac=bag_proportion, replace=True, random_state=i)

    # Fit a decision tree model to the "bag"
    clf = DecisionTreeClassifier(random_state=1, min_samples_leaf=2, splitter='random',
                                 max_features='auto')

    clf.fit(bag[columns], bag["high_income"])

    # Using the model, make predictions on the test data
    predictions.append(clf.predict_proba(test[columns])[:,1])

combined = np.sum(predictions, axis=0) / 10
rounded = np.round(combined)

print(roc_auc_score(test["high_income"], rounded))

#--------------------------------------------------------------------------------------------------#

#%% 9. Practice Putting it All Together
from sklearn.ensemble import RandomForestClassifier

clf = RandomForestClassifier(n_estimators=5, random_state=1, min_samples_leaf=2)

clf.fit(train[columns], train["high_income"])

print(roc_auc_score(test['high_income'], clf.predict(test[columns])))

#--------------------------------------------------------------------------------------------------#

#%% 10. Tweaking Parameters to Increase Accuracy
clf = RandomForestClassifier(n_estimators=150, random_state=1, min_samples_leaf=2)

clf.fit(train[columns], train["high_income"])

predictions = clf.predict(test[columns])
print(roc_auc_score(test["high_income"], predictions))

#--------------------------------------------------------------------------------------------------#

#%% 11. Reducing Overfitting
clf = DecisionTreeClassifier(random_state=1, min_samples_leaf=5)

clf.fit(train[columns], train["high_income"])

predictions = clf.predict(train[columns])
print(roc_auc_score(train["high_income"], predictions))

predictions = clf.predict(test[columns])
print(roc_auc_score(test["high_income"], predictions))

clf = RandomForestClassifier(n_estimators=150, random_state=1, min_samples_leaf=5)

clf.fit(train[columns], train["high_income"])

predictions = clf.predict(train[columns])
print(roc_auc_score(train["high_income"], predictions))

predictions = clf.predict(test[columns])
print(roc_auc_score(test["high_income"], predictions))

#--------------------------------------------------------------------------------------------------#

#%% 12. When to Use Random Forests
# No code
