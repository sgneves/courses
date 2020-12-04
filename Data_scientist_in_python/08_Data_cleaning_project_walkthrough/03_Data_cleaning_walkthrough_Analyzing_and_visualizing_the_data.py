#**************************************************************************************************#
#                                                                                                  #
# 03_Data_cleaning_walkthrough_Analyzing_and_visualizing_the_data                                  #
#                                                                                                  #
# Authors: S.G.M. Neves                                                                            #
#                                                                                                  #
#**************************************************************************************************#

#%% 1.Introduction
cols = ['SAT Math Avg. Score','SAT Critical Reading Avg. Score','SAT Writing Avg. Score']

combined['sat_score'] = combined.loc[:,cols].sum(axis=1)

#--------------------------------------------------------------------------------------------------#

#%% 2.Finding Correlations With the r Value
# No code

#--------------------------------------------------------------------------------------------------#

#%% 3.Finding Correlations With the r Value
correlations = combined.corr()['sat_score']

print(correlations)

#--------------------------------------------------------------------------------------------------#

#%% 4.Plotting Enrollment With the Plot() Accessor
# No code

#--------------------------------------------------------------------------------------------------#

#%% 5.Plotting Enrollment With the Plot() Accessor
combined.plot.scatter(x='total_enrollment', y='sat_score')

#--------------------------------------------------------------------------------------------------#

#%% 6.Exploring Schools With Low SAT Scores and Enrollment
low_enrollment = combined.loc[(combined['total_enrollment'] < 1000)
                              & (combined['sat_score'] < 1000)]

print(low_enrollment['School Name'])

#--------------------------------------------------------------------------------------------------#

#%% 7.Plotting Language Learning Percentage
combined.plot.scatter(x='ell_percent', y='sat_score')

#--------------------------------------------------------------------------------------------------#

#%% 8.Calculating District-Level Statistics
districts = combined.groupby('school_dist').mean()

districts.reset_index(inplace=True)

print(districts.head()