#**************************************************************************************************#
#                                                                                                  #
# 03_Hidden_layers                                                                                 #
#                                                                                                  #
# Authors: S.G.M. Neves                                                                            #
#                                                                                                  #
#**************************************************************************************************#

#%% 1. Hidden Layers
# No code

#--------------------------------------------------------------------------------------------------#

#%% 2. Generating Data That Contains Nonlinearity
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.datasets import make_moons

data = make_moons(100, random_state=3, noise=0.04)

features = pd.DataFrame(data[0])
labels = pd.Series(data[1])

fig = plt.figure(figsize=(8,8))

ax = fig.add_subplot(111, projection='3d')

ax.scatter3D(features.iloc[:,0], features.iloc[:,1], labels)
ax.set_xlabel('x1')
ax.set_ylabel('x2')
ax.set_zlabel('y')

#--------------------------------------------------------------------------------------------------#

#%% 3. Hidden Layer With A Single Neuron
# No code

#--------------------------------------------------------------------------------------------------#

#%% 4. Training A Neural Network Using Scikit-learn
import numpy as np
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
from sklearn.neural_network import MLPClassifier

np.random.seed(8)

features["bias"] = 1

shuffled_index = np.random.permutation(features.index)
shuffled_data = features.loc[shuffled_index]
shuffled_labels = labels.loc[shuffled_index]

mid_length = int(len(shuffled_data)/2)
train_features = shuffled_data.iloc[0:mid_length]
test_features = shuffled_data.iloc[mid_length:len(shuffled_data)]
train_labels = shuffled_labels.iloc[0:mid_length]
test_labels = shuffled_labels.iloc[mid_length: len(labels)]

mlp = MLPClassifier(hidden_layer_sizes=(1,), activation='logistic')
mlp.fit(train_features, train_labels)
nn_predictions = mlp.predict(test_features)

lr = LogisticRegression()
lr.fit(train_features, train_labels)
log_predictions = lr.predict(test_features)

nn_accuracy = accuracy_score(test_labels, nn_predictions)
print(nn_accuracy)
log_accuracy = accuracy_score(test_labels, log_predictions)
print(log_accuracy)

#--------------------------------------------------------------------------------------------------#

#%% 5. Hidden Layer With Multiple Neurons
np.random.seed(8)
shuffled_index = np.random.permutation(features.index)
shuffled_data = features.loc[shuffled_index]
shuffled_labels = labels.loc[shuffled_index]
mid_length = int(len(shuffled_data)/2)
train_features = shuffled_data.iloc[0:mid_length]
test_features = shuffled_data.iloc[mid_length:len(shuffled_data)]
train_labels = shuffled_labels.iloc[0:mid_length]
test_labels = shuffled_labels.iloc[mid_length: len(labels)]

neurons = [1, 5, 10, 15, 20, 25]
accuracies = []

for neuron in neurons:

    mlp = MLPClassifier(hidden_layer_sizes=(neuron,), activation='logistic')

    mlp.fit(train_features, train_labels)

    accuracies.append(accuracy_score(test_labels, mlp.predict(test_features)))

print(accuracies)

#--------------------------------------------------------------------------------------------------#

#%% 6. Multiple Hidden Layers
neurons = [1, 5, 10, 15, 20, 25]
nn_accuracies = []

for neuron in neurons:

    mlp = MLPClassifier(hidden_layer_sizes=(neuron,neuron), activation='relu', max_iter=1000)

    mlp.fit(train_features, train_labels)

    nn_accuracies.append(accuracy_score(test_labels, mlp.predict(test_features)))

print(nn_accuracies)
