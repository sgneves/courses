#**************************************************************************************************#
#                                                                                                  #
# 02_Introduction_to_evaluating_binary_classifiers                                                 #
#                                                                                                  #
# Authors: S.G.M. Neves                                                                            #
#                                                                                                  #
#**************************************************************************************************#

#%% 1. Introduction to the Data
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LogisticRegression

admissions = pd.read_csv("admissions.csv")

model = LogisticRegression()

model.fit(admissions[["gpa"]], admissions["admit"])

labels = model.predict(admissions[["gpa"]])

admissions['predicted_label'] = labels

print(admissions['predicted_label'].value_counts())

print(admissions.head())

#--------------------------------------------------------------------------------------------------#

#%% 2. Accuracy
admissions.rename(columns={'admit': 'actual_label'}, inplace=True)

matches = admissions['predicted_label'] == admissions['actual_label']

correct_predictions = admissions[matches]

print(correct_predictions.head())

accuracy = correct_predictions.shape[0] / admissions.shape[0]

#--------------------------------------------------------------------------------------------------#

#%% 3. Binary classification outcomes
# No code

#--------------------------------------------------------------------------------------------------#

#%% 4. Binary classification outcomes
true_positives = ((admissions['predicted_label'] == 1) & (admissions['actual_label'] == 1)).sum()
print(true_positives)

true_negatives = ((admissions['predicted_label'] == 0) & (admissions['actual_label'] == 0)).sum()
print(true_negatives)

#--------------------------------------------------------------------------------------------------#

#%% 5. Sensitivity
false_negatives = ((admissions['predicted_label'] == 0) & (admissions['actual_label'] == 1)).sum()

sensitivity = true_positives / (true_positives + false_negatives)

#--------------------------------------------------------------------------------------------------#

#%% 6. Specificity
false_positives = ((admissions['predicted_label'] == 1) & (admissions['actual_label'] == 0)).sum()

specificity = true_negatives / (false_positives + true_negatives)
