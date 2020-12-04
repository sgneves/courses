#**************************************************************************************************#
#                                                                                                  #
# 01_Representing_neural_networks                                                                  #
#                                                                                                  #
# Authors: S.G.M. Neves                                                                            #
#                                                                                                  #
#**************************************************************************************************#

#%% 1. Nonlinear Models
# No code

#--------------------------------------------------------------------------------------------------#

#%% 2. Introduction to Graphs
# No code

#--------------------------------------------------------------------------------------------------#

#%% 3. Computational Graphs
# No code

#--------------------------------------------------------------------------------------------------#

#%% 4. A Neural Network That Performs Linear Regression
# No code

#--------------------------------------------------------------------------------------------------#

#%% 5. Generating Regression Data
import pandas as pd
from sklearn.datasets import make_regression

data = make_regression(n_samples=100, n_features=3, random_state=1)

features = pd.DataFrame(data[0])

labels = pd.Series(data[1])

#--------------------------------------------------------------------------------------------------#

#%% 6. Fitting A Linear Regression Neural Network
import numpy as np
from sklearn.linear_model import SGDRegressor

def train(features, labels):

    lr = SGDRegressor()

    lr.fit(features, labels)

    return lr.coef_

def feedforward(features, weights):

    return np.dot(features, weights)

features['bias'] = 1

train_weights = train(features, labels)

linear_predictions = feedforward(features, train_weights)

#--------------------------------------------------------------------------------------------------#

#%% 7. Generating Classification Data
from sklearn.datasets import make_classification

data = make_classification(n_samples=100, n_features=4, random_state=1)

class_features = pd.DataFrame(data[0])

class_labels = pd.Series(data[1])

#--------------------------------------------------------------------------------------------------#

#%% 8. Implementing A Neural Network That Performs Classification
from sklearn.linear_model import SGDClassifier

def log_train(class_features, class_labels):

    lc = SGDClassifier()

    lc.fit(class_features, class_labels)

    return lc.coef_

def sigmoid(linear_combination):

    return 1 / (1 + np.exp(-linear_combination))

def log_feedforward(class_features, log_train_weights):

    linear_combination = np.dot(class_features, log_train_weights.transpose())

    log_predictions = sigmoid(linear_combination)

    cond = log_predictions >= 0.5
    log_predictions[cond] = 1
    log_predictions[~cond] = 0

    return log_predictions

class_features['bias'] = 1

log_train_weights = log_train(class_features, class_labels)

log_predictions = log_feedforward(class_features, log_train_weights)
