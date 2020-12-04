#**************************************************************************************************#
#                                                                                                  #
# 02_Building_a_decision_tree                                                                      #
#                                                                                                  #
# Authors: S.G.M. Neves                                                                            #
#                                                                                                  #
#**************************************************************************************************#

#%% 1. Introduction to the Data
# No code
#--------------------------------------------------------------------------------------------------#

#%% 2. Overview of the ID3 Algorithm
# No code

#--------------------------------------------------------------------------------------------------#

#%% 3. Walking Through an Example of the ID3 Algorithm
# No code

#--------------------------------------------------------------------------------------------------#

#%% 4. Determining the Column to Split On
import math
import numpy as np
import pandas as pd

income = pd.read_csv("income.csv", index_col=False)

cols = income.select_dtypes('object').columns
income[cols] = income[cols].apply(lambda col: pd.Categorical(col).codes)

def entropy(column):
    """
    Calculate the entropy given a pandas series, list, or numpy array.
    """

    # Compute the counts of each unique value in the column
    counts = np.bincount(column)

    # Divide by the total column length to get a probability
    probabilities = counts / len(column)

    return -sum([p * math.log(p, 2) for p in probabilities if p > 0])

def information_gain(data, split_name, target_name):
    """
    Calculate information gain given a data set, column to split on, and target
    """

    # Split the data into two subsets, based on the median
    cond = data[split_name] <= data[split_name].median()
    left_split = data.loc[cond, target_name]
    right_split = data.loc[~cond, target_name]

    # Return information gain
    return (entropy(data[target_name])
            - 1/data.shape[0] * (left_split.shape[0] * entropy(left_split)
                                 + right_split.shape[0] * entropy(right_split)))

def find_best_column(data, target_name, columns):
    """
    Returns the name of the column that should de used to split the data set
    """

    # Calculate the information gain for each potential column to split on
    information_gains = [information_gain(data, col, target_name) for col in columns]

    # Return the name of the column with the highest information gain
    return columns[np.array(information_gains).argmax()]

columns = ["age", "workclass", "education_num", "marital_status", "occupation", "relationship", "race", "sex", "hours_per_week", "native_country"]

income_split = find_best_column(income, 'high_income', columns)

#--------------------------------------------------------------------------------------------------#

#%% 5. Creating a Simple Recursive Algorithm

# We'll use lists to store our labels for nodes (when we find them)
# Lists can be accessed inside our recursive function, whereas integers can't.
# Look at the python missions on scoping for more information on this topic
label_1s = []
label_0s = []

def id3(data, target, columns):

    unique_targets = pd.unique(data[target])

    if len(unique_targets) == 1:

        if unique_targets == 0:
            label_0s.append(0)
        else:
            label_1s.append(1)

        return

    # Find the best column to split on our data
    best_column = find_best_column(data, target, columns)

    # Split the data into two subsets, based on the median
    cond = data[best_column] <= data[best_column].median()
    left_split = data[cond]
    right_split = data[~cond]

    # Loop through the splits and call id3 recursively
    for split in [left_split, right_split]:
        # Call id3 recursively to process each branch
        id3(split, target, columns)

# Create the data set that we used in the example on the last screen
data = pd.DataFrame([
    [0,20,0],
    [0,60,2],
    [0,40,1],
    [1,25,1],
    [1,35,2],
    [1,55,1]
    ])

# Assign column names to the data
data.columns = ["high_income", "age", "marital_status"]

# Call the function on our data to set the counters properly
id3(data, "high_income", ["age", "marital_status"])

#--------------------------------------------------------------------------------------------------#

#%% 6. Storing the Tree
# No code

#--------------------------------------------------------------------------------------------------#

#%% 7. Storing the Tree

# Create a dictionary to hold the tree
# It has to be outside of the function so we can access it later
tree = {}

# This list will let us number the nodes
# It has to be a list so we can access it inside the function
nodes = []

def id3(data, target, columns, tree):

    unique_targets = pd.unique(data[target])

    # Assign the number key to the tree dictionary
    nodes.append(len(nodes) + 1)
    tree["number"] = nodes[-1]

    # Assign the label key to the tree dictionary
    if len(unique_targets) == 1:

        if unique_targets == 0:
            tree["label"] = 0
        else:
            tree["label"] = 1

        return

    # Find the best column to split on our data
    best_column = find_best_column(data, target, columns)
    tree["column"] = best_column

    # Split the data into two subsets, based on the median
    median = data[best_column].median()
    tree["median"] = median

    cond = data[best_column] <= median
    left_split = data[cond]
    right_split = data[~cond]

    # Loop through the splits and call id3 recursively
    split_dict = [["left", left_split], ["right", right_split]]

    for name, split in split_dict:
        tree[name] = {}
        id3(split, target, columns, tree[name])

# Call the function on our data to set the counters properly
id3(data, "high_income", ["age", "marital_status"], tree)

#--------------------------------------------------------------------------------------------------#

#%% 8. Printing Labels for a More Attractive Tree

def print_with_depth(string, depth):

    # Add space before a string
    prefix = "    " * depth

    # Print a string, and indent it appropriately
    print("{0}{1}".format(prefix, string))

def print_node(tree, depth):

    # Check for the presence of "label" in the tree
    if "label" in tree:
        # If found, then this is a leaf, so print it and return
        print_with_depth("Leaf: Label {0}".format(tree["label"]), depth)

        return

    # Print information about what the node is splitting on
    print_with_depth("{0} > {1}".format(tree["column"], tree["median"]), depth)

    # Loop through the branches and call print_node recursively
    for branch in [tree["left"], tree["right"]]:
        print_node(branch, depth + 1)

print_node(tree, 0)

#--------------------------------------------------------------------------------------------------#

#%% 9. Making Predictions With the Printed Tree
# No code

#--------------------------------------------------------------------------------------------------#

#%% 10. Making Predictions Automatically
def predict(tree, row):

    if "label" in tree:
        return tree["label"]

    column = tree["column"]
    median = tree["median"]

    # Insert code here to check whether row[column] is less than or equal to median
    if row[column] <= median:
        return predict(tree["left"], row)
    else:
        return predict(tree["right"], row)

# Print the prediction for the first row in our data
print(predict(tree, data.iloc[0]))

#--------------------------------------------------------------------------------------------------#

#%% 11. Making Multiple Predictions
new_data = pd.DataFrame([
    [40,0],
    [20,2],
    [80,1],
    [15,1],
    [27,2],
    [38,1]
    ])

# Assign column names to the data
new_data.columns = ["age", "marital_status"]

def batch_predict(tree, df):

    return df.apply(lambda row: predict(tree, row), axis = 1)

predictions = batch_predict(tree, new_data)
