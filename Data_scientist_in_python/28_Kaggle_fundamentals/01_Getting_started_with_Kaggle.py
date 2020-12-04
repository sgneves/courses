#**************************************************************************************************#
#                                                                                                  #
# 01_Getting_started_with_Kaggle                                                                   #
#                                                                                                  #
# Authors: S.G.M. Neves                                                                            #
#                                                                                                  #
#**************************************************************************************************#

#%% 1. Introduction to Kaggle
import pandas as pd

train = pd.read_csv("train.csv")
train_shape = train.shape

test = pd.read_csv("test.csv")
test_shape = test.shape

#--------------------------------------------------------------------------------------------------#

#%% 2. Exploring the Data
import matplotlib.pyplot as plt

sex_pivot = train.pivot_table(index="Sex",values="Survived")
sex_pivot.plot.bar()
plt.show()

class_pivot = train.pivot_table(index="Pclass",values="Survived")
class_pivot.plot.bar()
plt.show()

#--------------------------------------------------------------------------------------------------#

#%% 3. Exploring and Converting the Age Column
def process_age(df, cut_points, label_names):

    df["Age"] = df["Age"].fillna(-0.5)
    df["Age_categories"] = pd.cut(df["Age"],cut_points,labels=label_names)
    return df

cut_points = [-1,0,5,12,18,35,60,100]
label_names = ['Missing','Infant','Child','Teenager','Young Adult','Adult','Senior']

train = process_age(train,cut_points,label_names)
test = process_age(test,cut_points,label_names)

age_pivot = train.pivot_table(index="Age_categories",values="Survived")
age_pivot.plot.bar()
plt.show()

#--------------------------------------------------------------------------------------------------#

#%% 4. Preparing our Data for Machine Learning
def create_dummies(df, cols):

    for col in cols:

        dummies = pd.get_dummies(df[col], prefix=col)

        df = pd.concat([df,dummies], axis=1)

    return df

train = create_dummies(train, ["Pclass","Sex","Age_categories"])
test = create_dummies(test, ["Pclass","Sex","Age_categories"])

#--------------------------------------------------------------------------------------------------#

#%% 5. Creating Our First Machine Learning Model
from sklearn.linear_model import LogisticRegression

columns = ['Pclass_1', 'Pclass_2', 'Pclass_3', 'Sex_female', 'Sex_male',
       'Age_categories_Missing','Age_categories_Infant',
       'Age_categories_Child', 'Age_categories_Teenager',
       'Age_categories_Young Adult', 'Age_categories_Adult',
       'Age_categories_Senior']

lr = LogisticRegression()

lr.fit(train[columns], train['Survived'])

#--------------------------------------------------------------------------------------------------#

#%% 6. Splitting Our Training Data
from sklearn.model_selection import train_test_split

holdout = test # from now on we will refer to this
               # dataframe as the holdout data

train_X, test_X, train_y, test_y = train_test_split(train[columns], train['Survived'],
                                                    test_size=0.2,random_state=0)

#--------------------------------------------------------------------------------------------------#

#%% 7. Making Predictions and Measuring their Accuracy
from sklearn.metrics import accuracy_score

lr = LogisticRegression()

lr.fit(train_X, train_y)

predictions = lr.predict(test_X)

accuracy = accuracy_score(test_y, predictions)

#--------------------------------------------------------------------------------------------------#

#%% 8. Using Cross Validation for More Accurate Error Measurement
from sklearn.model_selection import cross_val_score

lr = LogisticRegression()

scores = cross_val_score(lr, train[columns], train['Survived'], cv=10)

accuracy = scores.mean()

#--------------------------------------------------------------------------------------------------#

#%% 9. Making Predictions on Unseen Data
lr = LogisticRegression()

lr.fit(train[columns], train['Survived'])

holdout_predictions = lr.predict(holdout[columns])

#--------------------------------------------------------------------------------------------------#

#%% 10. Creating a Submission File
submission = pd.DataFrame({"PassengerId": holdout["PassengerId"],"Survived": holdout_predictions})

submission.to_csv('submission.csv', index=False)

#--------------------------------------------------------------------------------------------------#

#%% 11. Making Our First Submission to Kaggle
# No code
