#**************************************************************************************************#
#                                                                                                  #
# 01_Introduction_to_decision_trees                                                                #
#                                                                                                  #
# Authors: S.G.M. Neves                                                                            #
#                                                                                                  #
#**************************************************************************************************#

#%% 1. Introduction
# No code

#--------------------------------------------------------------------------------------------------#

#%% 2. Overview of the Data Set
import pandas as pd

# Set index_col to False to avoid pandas thinking that the first column is row indexes (it's age)
income = pd.read_csv("income.csv", index_col=False)
print(income.head(5))

#--------------------------------------------------------------------------------------------------#

#%% 3. Converting Categorical Variables
cols = income.select_dtypes('object').columns

income[cols] = income[cols].apply(lambda col: pd.Categorical(col).codes)

print(income["workclass"].head(5))

#--------------------------------------------------------------------------------------------------#

#%% 4. Splitting Data
# No code

#--------------------------------------------------------------------------------------------------#

#%% 5. Creating Splits
cond = income['workclass'] == 4
private_incomes = income[cond]
public_incomes = income[~cond]

#--------------------------------------------------------------------------------------------------#

#%% 6. Decision Trees as Flows of Data
# No code

#--------------------------------------------------------------------------------------------------#

#%% 7. Splitting Data to Make Predictions
# No code

#--------------------------------------------------------------------------------------------------#

#%% 8. Overview of Data Set Entropy
# No code

#--------------------------------------------------------------------------------------------------#

#%% 9. Overview of Data Set Entropy
import math

n = income.shape[0]
n_one = income['high_income'].sum()

income_entropy = -((n - n_one) / n * math.log((n - n_one) / n, 2) + n_one / n * math.log(n_one / n, 2))

print(income_entropy)

# entropy = -(2/5 * math.log(2/5, 2) + 3/5 * math.log(3/5, 2))

#--------------------------------------------------------------------------------------------------#

#%% 10. Information Gain
# No code

#--------------------------------------------------------------------------------------------------#

#%% 11. Information Gain
import numpy as np

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

# Verify that our function matches our answer from earlier
entropy = calc_entropy([1,1,0,0,1])
print(entropy)

information_gain = entropy - ((.8 * calc_entropy([1,1,0,0])) + (.2 * calc_entropy([1])))
print(information_gain)

print()

split_age = income['age'] > income['age'].median()

hi_entropy = calc_entropy(income['high_income'])
print(hi_entropy)

n = income.shape[0]
left_split = income.loc[~split_age, 'high_income']
right_split = income.loc[split_age, 'high_income']

age_information_gain = hi_entropy - (left_split.shape[0] / n * calc_entropy(left_split)
                                      + right_split.shape[0] / n * calc_entropy(right_split))
print(age_information_gain)

#--------------------------------------------------------------------------------------------------#

#%% 12. Finding the Best Split
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

# Verify that our answer is the same as on the last screen
print(calc_information_gain(income, "age", "high_income"))

columns = ["age", "workclass", "education_num", "marital_status", "occupation", "relationship", "race", "sex", "hours_per_week", "native_country"]

information_gains = [calc_information_gain(income, col, "high_income") for col in columns]

highest_gain = columns[np.array(information_gains).argmax()]

#--------------------------------------------------------------------------------------------------#

#%% 13. Build the Whole Tree
# No code
