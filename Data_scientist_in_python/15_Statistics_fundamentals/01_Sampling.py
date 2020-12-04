#**************************************************************************************************#
#                                                                                                  #
# 01_Sampling                                                                                      #
#                                                                                                  #
# Authors: S.G.M. Neves                                                                            #
#                                                                                                  #
#**************************************************************************************************#

#%% 1. Introduction
# No code

#--------------------------------------------------------------------------------------------------#

#%% 2. Solving Problems with Statistics
# No code

#--------------------------------------------------------------------------------------------------#

#%% 3. Populations and Samples
question1 = 'population'
question2 = 'population'
question3 = 'sample'
question4 = 'population'
question5 = 'sample'

#--------------------------------------------------------------------------------------------------#

#%% 4. Sampling Error
import pandas as pd

wnba = pd.read_csv("wnba.csv")

print(wnba.head())
print(wnba.tail())
print(wnba.shape)

parameter = wnba["Games Played"].max()

sample = wnba["Games Played"].sample(30, random_state=1)

statistic = sample.max()

sampling_error = parameter - statistic

#--------------------------------------------------------------------------------------------------#

#%% 5. Simple Random Sampling
import matplotlib.pyplot as plt

samples_means = []

for i in range(100):

    sample = wnba["PTS"].sample(10, random_state=i)

    samples_means.append(sample.mean())

plt.scatter(range(1, 101), samples_means)
plt.axhline(wnba["PTS"].mean())

#--------------------------------------------------------------------------------------------------#

#%% 6. The Importance of Sample Size
# No code

#--------------------------------------------------------------------------------------------------#

#%% 7. Stratified Sampling
wnba["pts_per_game"] = wnba["PTS"] / wnba["Games Played"]

mean_points_per_game = {}

for pos in wnba["Pos"].unique():

    mean_points_per_game[pos] = wnba.loc[wnba["Pos"] == pos, "pts_per_game"].sample(10, random_state=0).mean()

position_most_points = max(mean_points_per_game, key=mean_points_per_game.get)

#--------------------------------------------------------------------------------------------------#

#%% 8. Proportional Stratified Sampling
PTS_1 = wnba.loc[wnba["Games Played"] <= 12, "PTS"].copy()
PTS_2 = wnba.loc[(wnba["Games Played"] > 12) & (wnba["Games Played"] <= 22), "PTS"]
PTS_3 = wnba.loc[wnba["Games Played"] > 22, "PTS"]

samples_means = []

for i in range(100):

    sample_1 = PTS_1.sample(1, random_state=i)
    sample_2 = PTS_2.sample(2, random_state=i)
    sample_3 = PTS_3.sample(7, random_state=i)

    samples_means.append(pd.concat([sample_1, sample_2, sample_3]).mean())

plt.scatter(range(1, 101), samples_means)
plt.axhline(wnba["PTS"].mean())

#--------------------------------------------------------------------------------------------------#

#%% 9. Choosing the Right Strata
print(wnba['MIN'].value_counts(bins = 3, normalize = True))

PTS_1 = wnba.loc[wnba["MIN"] <= 347, "PTS"]
PTS_2 = wnba.loc[(wnba["MIN"] > 347) & (wnba["MIN"] <= 683), "PTS"]
PTS_3 = wnba.loc[wnba["MIN"] > 683, "PTS"]

samples_means = []

for i in range(100):

    sample_1 = PTS_1.sample(4, random_state=i)
    sample_2 = PTS_2.sample(4, random_state=i)
    sample_3 = PTS_3.sample(4, random_state=i)

    samples_means.append(pd.concat([sample_1, sample_2, sample_3]).mean())

plt.scatter(range(1, 101), samples_means)
plt.axhline(wnba["PTS"].mean())

#--------------------------------------------------------------------------------------------------#

#%% 10. Cluster Sampling
teams = pd.Series(wnba['Team'].unique()).sample(4, random_state = 0)

wnba_sample = pd.DataFrame()

for team in teams:

    wnba_sample = pd.concat([wnba_sample, wnba.loc[wnba["Team"] == team]])

sampling_error_height = wnba["Height"].mean() - wnba_sample["Height"].mean()
sampling_error_age = wnba["Age"].mean() - wnba_sample["Age"].mean()
sampling_error_BMI = wnba["BMI"].mean() - wnba_sample["BMI"].mean()
sampling_error_points = wnba["PTS"].mean() - wnba_sample["PTS"].mean()

#--------------------------------------------------------------------------------------------------#

#%% 11. Sampling in Data Science Practice
# No code

#--------------------------------------------------------------------------------------------------#

#%% 12. Descriptive and Inferential Statistics
# No code
