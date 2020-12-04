#**************************************************************************************************#
#                                                                                                  #
# 03_Making_predictions                                                                            #
#                                                                                                  #
# Authors: S.G.M. Neves                                                                            #
#                                                                                                  #
#**************************************************************************************************#

#%% 1. Recap
import pandas as pd

loans = pd.read_csv('clean_loans_2007.csv')

print(loans.info())

#--------------------------------------------------------------------------------------------------#

#%% 2. Picking an error metric
# No code

#--------------------------------------------------------------------------------------------------#

#%% 3. Picking an error metric
tn = ((predictions == 0) & (loans["loan_status"] == 0)).sum()
tp = ((predictions == 1) & (loans["loan_status"] == 1)).sum()
fn = ((predictions == 0) & (loans["loan_status"] == 1)).sum()
fp = ((predictions == 1) & (loans["loan_status"] == 0)).sum()

#--------------------------------------------------------------------------------------------------#

#%% 4. Class imbalance
# No code

#--------------------------------------------------------------------------------------------------#

#%% 5. Class imbalance
import numpy

# Predict that all loans will be paid off on time.
predictions = pd.Series(numpy.ones(loans.shape[0]))

tn = ((predictions == 0) & (loans["loan_status"] == 0)).sum()
tp = ((predictions == 1) & (loans["loan_status"] == 1)).sum()
fn = ((predictions == 0) & (loans["loan_status"] == 1)).sum()
fp = ((predictions == 1) & (loans["loan_status"] == 0)).sum()

# False positive rate
fpr = fp / (fp + tn)
print(fpr)

# True positive rate
tpr = tp / (tp + fn)
print(tpr)

#--------------------------------------------------------------------------------------------------#

#%% 6. Logistic Regression
from sklearn.linear_model import LogisticRegression

features = loans.drop('loan_status', axis=1)
target = loans['loan_status']

lr = LogisticRegression(max_iter=1000)

lr.fit(features, target)

predictions = lr.predict(features)

#--------------------------------------------------------------------------------------------------#

#%% 7. Cross Validation
from sklearn.model_selection import cross_val_predict

lr = LogisticRegression(max_iter=1000)

predictions = pd.Series(cross_val_predict(lr, features, target, cv=3))

tn = ((predictions == 0) & (loans["loan_status"] == 0)).sum()
tp = ((predictions == 1) & (loans["loan_status"] == 1)).sum()
fn = ((predictions == 0) & (loans["loan_status"] == 1)).sum()
fp = ((predictions == 1) & (loans["loan_status"] == 0)).sum()

# False positive rate
fpr = fp / (fp + tn)
print(fpr)

# True positive rate
tpr = tp / (tp + fn)
print(tpr)

#--------------------------------------------------------------------------------------------------#

#%% 8. Penalizing the classifier
# No code

#--------------------------------------------------------------------------------------------------#

#%% 9. Penalizing the classifier
lr = LogisticRegression(max_iter=1000, class_weight='balanced')

predictions = pd.Series(cross_val_predict(lr, features, target, cv=3))

tn = ((predictions == 0) & (loans["loan_status"] == 0)).sum()
tp = ((predictions == 1) & (loans["loan_status"] == 1)).sum()
fn = ((predictions == 0) & (loans["loan_status"] == 1)).sum()
fp = ((predictions == 1) & (loans["loan_status"] == 0)).sum()

# False positive rate
fpr = fp / (fp + tn)
print(fpr)

# True positive rate
tpr = tp / (tp + fn)
print(tpr)

#--------------------------------------------------------------------------------------------------#

#%% 10. Manual penalties
penalty = {0: 10,1: 1}

lr = LogisticRegression(max_iter=1000, class_weight=penalty)

predictions = pd.Series(cross_val_predict(lr, features, target, cv=3))

tn = ((predictions == 0) & (loans["loan_status"] == 0)).sum()
tp = ((predictions == 1) & (loans["loan_status"] == 1)).sum()
fn = ((predictions == 0) & (loans["loan_status"] == 1)).sum()
fp = ((predictions == 1) & (loans["loan_status"] == 0)).sum()

# False positive rate
fpr = fp / (fp + tn)
print(fpr)

# True positive rate
tpr = tp / (tp + fn)
print(tpr)

#--------------------------------------------------------------------------------------------------#

#%% 11. Random forests
from sklearn.ensemble import RandomForestClassifier

rf = RandomForestClassifier(class_weight='balanced', random_state=1)

predictions = pd.Series(cross_val_predict(rf, features, target, cv=3))

tn = ((predictions == 0) & (loans["loan_status"] == 0)).sum()
tp = ((predictions == 1) & (loans["loan_status"] == 1)).sum()
fn = ((predictions == 0) & (loans["loan_status"] == 1)).sum()
fp = ((predictions == 1) & (loans["loan_status"] == 0)).sum()

# False positive rate
fpr = fp / (fp + tn)
print(fpr)

# True positive rate
tpr = tp / (tp + fn)
print(tpr)
