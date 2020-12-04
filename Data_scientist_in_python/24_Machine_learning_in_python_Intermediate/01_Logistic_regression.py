#**************************************************************************************************#
#                                                                                                  #
# 01_Logistic_regression                                                                           #
#                                                                                                  #
# Authors: S.G.M. Neves                                                                            #
#                                                                                                  #
#**************************************************************************************************#

#%% 1. Classification
# No code

#--------------------------------------------------------------------------------------------------#

#%% 2. Introduction to the data
import pandas as pd
import matplotlib.pyplot as plt

admissions = pd.read_csv('admissions.csv')

plt.scatter(admissions['gpa'], admissions['admit'])
plt.show()

#--------------------------------------------------------------------------------------------------#

#%% 3. Logistic regression
# No code

#--------------------------------------------------------------------------------------------------#

#%% 4. Logistic function
import numpy as np

# Logistic Function
def logistic(x):

    return np.exp(x)  / (1 + np.exp(x))

# Generate 50 real values, evenly spaced, between -6 and 6.
x = np.linspace(-6, 6, 50, dtype=float)

# Transform each number in t using the logistic function.
y = logistic(x)

# Plot the resulting data.
plt.plot(x, y)
plt.ylabel("Probability")
plt.show()

#--------------------------------------------------------------------------------------------------#

#%% 5. Training a logistic regression model
from sklearn.linear_model import LogisticRegression

logistic_model = LogisticRegression()

logistic_model.fit(admissions[["gpa"]], admissions["admit"])

#--------------------------------------------------------------------------------------------------#

#%% 6. Plotting probabilities

# Get the predicted probabilities
pred_probs = logistic_model.predict_proba(admissions[["gpa"]])

# Plot the predicted probabilities
plt.scatter(admissions['gpa'], pred_probs[:,1])
plt.show()

#--------------------------------------------------------------------------------------------------#

#%% 7. Predict labels
fitted_labels = logistic_model.predict(admissions[["gpa"]])

plt.scatter(admissions['gpa'], fitted_labels)
plt.show()
