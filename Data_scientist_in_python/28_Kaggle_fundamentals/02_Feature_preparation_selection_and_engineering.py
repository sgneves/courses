#**************************************************************************************************#
#                                                                                                  #
# 02_Feature_preparation_selection_and_engineering                                                 #
#                                                                                                  #
# Authors: S.G.M. Neves                                                                            #
#                                                                                                  #
#**************************************************************************************************#

#%% 1. Introduction
import pandas as pd

train = pd.read_csv('train.csv')
holdout = pd.read_csv('test.csv')

def process_age(df):

    df["Age"] = df["Age"].fillna(-0.5)
    cut_points = [-1,0,5,12,18,35,60,100]
    label_names = ["Missing","Infant","Child","Teenager","Young Adult","Adult","Senior"]
    df["Age_categories"] = pd.cut(df["Age"],cut_points,labels=label_names)
    return df

def create_dummies(df, cols):

    for col in cols:

        dummies = pd.get_dummies(df[col], prefix=col)

        df = pd.concat([df,dummies], axis=1)

    return df

train = process_age(train)
holdout = process_age(holdout)

train = create_dummies(train, ["Age_categories","Pclass","Sex"])
holdout = create_dummies(holdout, ["Age_categories","Pclass","Sex"])

print(train.columns)

#--------------------------------------------------------------------------------------------------#

#%% 2. Preparing More Features
from sklearn.preprocessing import minmax_scale

# The holdout set has a missing value in the Fare column which
# we'll fill with the mean.
holdout["Fare"] = holdout["Fare"].fillna(train["Fare"].mean())

train["Embarked"] = train["Embarked"].fillna("S")
holdout["Embarked"] = holdout["Embarked"].fillna("S")

train = create_dummies(train, ["Embarked"])
holdout = create_dummies(holdout, ["Embarked"])

for col in ["SibSp","Parch","Fare"]:

    train[col + "_scaled"] = minmax_scale(train[col])
    holdout[col + "_scaled"] = minmax_scale(holdout[col])

#--------------------------------------------------------------------------------------------------#

#%% 3. Determining the Most Relevant Features
from sklearn.linear_model import LogisticRegression

columns = ['Age_categories_Missing', 'Age_categories_Infant',
       'Age_categories_Child', 'Age_categories_Teenager',
       'Age_categories_Young Adult', 'Age_categories_Adult',
       'Age_categories_Senior', 'Pclass_1', 'Pclass_2', 'Pclass_3',
       'Sex_female', 'Sex_male', 'Embarked_C', 'Embarked_Q', 'Embarked_S',
       'SibSp_scaled', 'Parch_scaled', 'Fare_scaled']

lr = LogisticRegression()

lr.fit(train[columns], train['Survived'])

coefficients = lr.coef_

feature_importance = pd.Series(coefficients[0], index=columns)

feature_importance.plot.barh()

#--------------------------------------------------------------------------------------------------#

#%% 4. Training a model using relevant features
from sklearn.model_selection import cross_val_score

columns = ['Age_categories_Infant', 'SibSp_scaled', 'Sex_female', 'Sex_male',
       'Pclass_1', 'Pclass_3', 'Age_categories_Senior', 'Parch_scaled']

lr = LogisticRegression()

scores = cross_val_score(lr, train[columns], train['Survived'], cv=10)

accuracy = scores.mean()
print(accuracy)

#--------------------------------------------------------------------------------------------------#

#%% 5. Submitting our Improved Model to Kaggle
columns = ['Age_categories_Infant', 'SibSp_scaled', 'Sex_female', 'Sex_male',
       'Pclass_1', 'Pclass_3', 'Age_categories_Senior', 'Parch_scaled']

lr = LogisticRegression()

lr.fit(train[columns], train['Survived'])

holdout_predictions = lr.predict(holdout[columns])

submission = pd.DataFrame({"PassengerId": holdout["PassengerId"],"Survived": holdout_predictions})

submission.to_csv('submission_1.csv', index=False)

#--------------------------------------------------------------------------------------------------#

#%% 6. Engineering a New Feature Using Binning
def process_fare(df):

    label_names = ["0-12","12-50","50-100","100+"]

    df["Fare_categories"] = pd.cut(df["Fare"], [0,12,50,100,200], labels=label_names)

    return df

train = process_fare(train)
holdout = process_fare(holdout)

train = create_dummies(train, ["Fare_categories"])
holdout = create_dummies(holdout, ["Fare_categories"])

#--------------------------------------------------------------------------------------------------#

#%% 7. Engineering Features From Text Columns
titles = {
    "Mr" :         "Mr",
    "Mme":         "Mrs",
    "Ms":          "Mrs",
    "Mrs" :        "Mrs",
    "Master" :     "Master",
    "Mlle":        "Miss",
    "Miss" :       "Miss",
    "Capt":        "Officer",
    "Col":         "Officer",
    "Major":       "Officer",
    "Dr":          "Officer",
    "Rev":         "Officer",
    "Jonkheer":    "Royalty",
    "Don":         "Royalty",
    "Sir" :        "Royalty",
    "Countess":    "Royalty",
    "Dona":        "Royalty",
    "Lady" :       "Royalty"
}

extracted_titles = train["Name"].str.extract(' ([A-Za-z]+)\.',expand=False)
train["Title"] = extracted_titles.map(titles)
extracted_titles = holdout["Name"].str.extract(' ([A-Za-z]+)\.',expand=False)
holdout["Title"] = extracted_titles.map(titles)

train["Cabin_type"] = train["Cabin"].str[0].fillna("Unknown")
holdout["Cabin_type"] = holdout["Cabin"].str[0].fillna("Unknown")

train = create_dummies(train, ["Title","Cabin_type"])
holdout = create_dummies(holdout, ["Title","Cabin_type"])

#--------------------------------------------------------------------------------------------------#

#%% 8. Finding Correlated Features
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

def plot_correlation_heatmap(df):
    corr = df.corr()

    sns.set(style="white")
    mask = np.zeros_like(corr, dtype=np.bool)
    mask[np.triu_indices_from(mask)] = True

    f, ax = plt.subplots(figsize=(11, 9))
    cmap = sns.diverging_palette(220, 10, as_cmap=True)


    sns.heatmap(corr, mask=mask, cmap=cmap, vmax=.3, center=0,
            square=True, linewidths=.5, cbar_kws={"shrink": .5})
    plt.show()

columns = ['Age_categories_Missing', 'Age_categories_Infant',
       'Age_categories_Child', 'Age_categories_Teenager',
       'Age_categories_Young Adult', 'Age_categories_Adult',
       'Age_categories_Senior', 'Pclass_1', 'Pclass_2', 'Pclass_3',
       'Sex_female', 'Sex_male', 'Embarked_C', 'Embarked_Q', 'Embarked_S',
       'SibSp_scaled', 'Parch_scaled', 'Fare_categories_0-12',
       'Fare_categories_12-50','Fare_categories_50-100', 'Fare_categories_100+',
       'Title_Master', 'Title_Miss', 'Title_Mr','Title_Mrs', 'Title_Officer',
       'Title_Royalty', 'Cabin_type_A','Cabin_type_B', 'Cabin_type_C', 'Cabin_type_D',
       'Cabin_type_E','Cabin_type_F', 'Cabin_type_G', 'Cabin_type_T', 'Cabin_type_Unknown']

plot_correlation_heatmap(train[columns])

#--------------------------------------------------------------------------------------------------#

#%% 9. Final Feature Selection using RFECV
from sklearn.feature_selection import RFECV

columns = ['Age_categories_Missing', 'Age_categories_Infant',
       'Age_categories_Child', 'Age_categories_Young Adult',
       'Age_categories_Adult', 'Age_categories_Senior', 'Pclass_1', 'Pclass_3',
       'Embarked_C', 'Embarked_Q', 'Embarked_S', 'SibSp_scaled',
       'Parch_scaled', 'Fare_categories_0-12', 'Fare_categories_50-100',
       'Fare_categories_100+', 'Title_Miss', 'Title_Mr', 'Title_Mrs',
       'Title_Officer', 'Title_Royalty', 'Cabin_type_B', 'Cabin_type_C',
       'Cabin_type_D', 'Cabin_type_E', 'Cabin_type_F', 'Cabin_type_G',
       'Cabin_type_T', 'Cabin_type_Unknown']

all_X = train[columns]
all_y = train["Survived"]

lr = LogisticRegression()

selector = RFECV(lr, cv=10)

selector.fit(all_X, all_y)

optimized_columns = all_X.columns[selector.support_]

#--------------------------------------------------------------------------------------------------#

#%% 10. Training A Model Using our Optimized Columns
columns = ['SibSp_scaled','Title_Mr','Title_Officer','Cabin_type_Unknown']

lr = LogisticRegression()

scores = cross_val_score(lr, train[columns], train['Survived'], cv=10)

accuracy = scores.mean()
print(accuracy)

#--------------------------------------------------------------------------------------------------#

#%% 11. Submitting our Model to Kaggle
lr = LogisticRegression()

lr.fit(train[columns], train['Survived'])

holdout_predictions = lr.predict(holdout[columns])

submission = pd.DataFrame({"PassengerId": holdout["PassengerId"],"Survived": holdout_predictions})

submission.to_csv('submission_2.csv', index=False)
