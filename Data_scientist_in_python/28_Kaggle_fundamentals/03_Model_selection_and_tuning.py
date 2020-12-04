#**************************************************************************************************#
#                                                                                                  #
# 03_Model_selection_and_tuning                                                                    #
#                                                                                                  #
# Authors: S.G.M. Neves                                                                            #
#                                                                                                  #
#**************************************************************************************************#

#%% 1. Introducing Model Selection
import pandas as pd

train = pd.read_csv('train_modified.csv')
holdout = pd.read_csv('holdout_modified.csv')

#--------------------------------------------------------------------------------------------------#

#%% 2. Training a Baseline Model
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import cross_val_score

all_X = train.drop(['Survived','PassengerId'],axis=1)
all_y = train['Survived']

lr = LogisticRegression()

scores = cross_val_score(lr, all_X, all_y, cv=10)

accuracy_lr = scores.mean()
print(accuracy_lr)

#--------------------------------------------------------------------------------------------------#

#%% 3. Training a Model using K-Nearest Neighbors
from sklearn.neighbors import KNeighborsClassifier

knn = KNeighborsClassifier(n_neighbors=1)

scores = cross_val_score(knn, all_X, all_y, cv=10)

accuracy_knn = scores.mean()
print(accuracy_knn)

#--------------------------------------------------------------------------------------------------#

#%% 4. Exploring Different K Values
import matplotlib.pyplot as plt

def plot_dict(dictionary):
    pd.Series(dictionary).plot.bar(figsize=(9,6),
                                   ylim=(0.78,0.83),rot=0)
    plt.show()

knn_scores = dict()

for k in range(1,50,2):

    knn = KNeighborsClassifier(n_neighbors=k)

    knn_scores[k] = cross_val_score(knn, all_X, all_y, cv=10).mean()

plot_dict(knn_scores)

#--------------------------------------------------------------------------------------------------#

#%% 5. Automating Hyperparameter Optimization with Grid Search
from sklearn.model_selection import GridSearchCV

knn = KNeighborsClassifier()

hyperparameters = {
    "n_neighbors": range(1,20,2),
    "weights": ["distance", "uniform"],
    "algorithm": ['brute'],
    "p": [1,2]
}

grid = GridSearchCV(knn, param_grid=hyperparameters, cv=10)
grid.fit(all_X, all_y)

best_params = grid.best_params_
print(best_params)

best_score = grid.best_score_
print(best_score)

#--------------------------------------------------------------------------------------------------#

#%% 6. Submitting K-Nearest Neighbors Predictions to Kaggle
holdout_no_id = holdout.drop(['PassengerId'],axis=1)

best_knn = grid.best_estimator_

holdout_predictions = best_knn.predict(holdout_no_id)

submission = pd.DataFrame({"PassengerId": holdout["PassengerId"],"Survived": holdout_predictions})

submission.to_csv('submission_3.csv', index=False)

#--------------------------------------------------------------------------------------------------#

#%% 7. Introducing Random Forests
from sklearn.ensemble import RandomForestClassifier

clf = RandomForestClassifier(random_state=1)

scores = cross_val_score(clf, all_X, all_y, cv=10)

accuracy_rf = scores.mean()
print(accuracy_rf)

#--------------------------------------------------------------------------------------------------#

#%% 8. Tuning our Random Forests Model with GridSearch
clf = RandomForestClassifier(random_state=1)

hyperparameters = {
    "criterion": ["entropy","gini"],
    "max_depth": [5,10],
    "max_features": ["log2","sqrt"],
    "min_samples_leaf": [1,5],
    "min_samples_split": [3,5],
    "n_estimators": [6,9]
}

grid = GridSearchCV(clf, param_grid=hyperparameters, cv=10)
grid.fit(all_X, all_y)

best_params = grid.best_params_
print(best_params)

best_score = grid.best_score_
print(best_score)

#--------------------------------------------------------------------------------------------------#

#%% 9. Submitting Random Forest Predictions to Kaggle
best_rf = grid.best_estimator_

holdout_predictions = best_rf.predict(holdout_no_id)

submission = pd.DataFrame({"PassengerId": holdout["PassengerId"],"Survived": holdout_predictions})

submission.to_csv('submission_4.csv', index=False)
