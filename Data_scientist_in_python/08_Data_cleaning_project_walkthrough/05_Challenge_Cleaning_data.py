#**************************************************************************************************#
#                                                                                                  #
# 05_Challenge_Cleaning_data                                                                       #
#                                                                                                  #
# Authors: S.G.M. Neves                                                                            #
#                                                                                                  #
#**************************************************************************************************#

#%% 1.Introduction
# No code

#--------------------------------------------------------------------------------------------------#

#%% 2.Life and Death of the Avengers
# No code

#--------------------------------------------------------------------------------------------------#

#%% 3.Exploring the Data
import pandas as pd

avengers = pd.read_csv("avengers.csv", encoding="Windows-1251")
avengers.head(5)

#--------------------------------------------------------------------------------------------------#

#%% 4.Filtering Out Bad Data
true_avengers = avengers.loc[avengers["Year"] > 1960].copy()

#--------------------------------------------------------------------------------------------------#

#%% 5.Consolidating Deaths
cols = ["Death" + str(i) for i in range(1,6)]

true_avengers["Deaths"] = (avengers[cols] == "YES").sum(axis=1)

#--------------------------------------------------------------------------------------------------#

#%% 6.Verifying Years Since Joining
joined_accuracy_count = (true_avengers["Years since joining"] == 2015 - true_avengers["Year"]).sum()
