#**************************************************************************************************#
#                                                                                                  #
# 02_Data_cleaning_walkthrough_Combining_the_data                                                  #
#                                                                                                  #
# Authors: S.G.M. Neves                                                                            #
#                                                                                                  #
#**************************************************************************************************#

#%% 1.Introduction
# No code

#--------------------------------------------------------------------------------------------------#

#%% 2.Condensing the Class Size Data Set
# No code

#--------------------------------------------------------------------------------------------------#

#%% 3.Condensing the Class Size Data Set
class_size = data['class_size']

class_size = class_size.loc[class_size['GRADE '] == '09-12']
class_size = class_size.loc[class_size['PROGRAM TYPE'] == 'GEN ED']

print(class_size.head())

#--------------------------------------------------------------------------------------------------#

#%% 4.Computing Average Class Sizes
# No code

#--------------------------------------------------------------------------------------------------#

#%% 5.Computing Average Class Sizes
class_size = class_size.groupby('DBN').mean()

class_size.reset_index(inplace=True)

data['class_size'] = class_size

print(data['class_size'].head())

#--------------------------------------------------------------------------------------------------#

#%% 6.Condensing the Demographics Data Set
# No code

#--------------------------------------------------------------------------------------------------#

#%% 7.Condensing the Demographics Data Set
data['demographics'] = data['demographics'].loc[data['demographics']['schoolyear'] == 20112012]

print(data['demographics'].head())

#--------------------------------------------------------------------------------------------------#

#%% 8.Condensing the Graduation Data Set
# No code

#--------------------------------------------------------------------------------------------------#

#%% 9.Condensing the Graduation Data Set
data['graduation'] = data['graduation'].loc[(data['graduation']['Cohort'] == '2006')
                                            & (data['graduation']['Demographic'] == 'Total Cohort')]

print(data['graduation'].head())

#--------------------------------------------------------------------------------------------------#

#%% 10.Converting AP Test Scores
cols = ['AP Test Takers ','Total Exams Taken','Number of Exams with scores 3 4 or 5']

for col in cols:

    data['ap_2010'][col] = pd.to_numeric(data['ap_2010'][col], errors='coerce')

print(data['ap_2010'][cols].dtypes)

#--------------------------------------------------------------------------------------------------#

#%% 11.Left, Right, Inner, and Outer Joins
# No code

#--------------------------------------------------------------------------------------------------#

#%% 12.Performing the Left Joins
combined = data['sat_results']

combined = combined.merge(data['ap_2010'], how='left', on='DBN')

combined = combined.merge(data['graduation'], how='left', on='DBN')

print(combined.head())

print(combined.shape)

#--------------------------------------------------------------------------------------------------#

#%% 13.Performing the Inner Joins
combined = combined.merge(data['class_size'], on='DBN')

combined = combined.merge(data['demographics'], on='DBN')

combined = combined.merge(data['survey'], on='DBN')

combined = combined.merge(data['hs_directory'], on='DBN')

print(combined.head())

print(combined.shape)

#--------------------------------------------------------------------------------------------------#

#%% 14.Filling in Missing Values
# No code

#--------------------------------------------------------------------------------------------------#

#%% 15.Filling in Missing Values
combined.fillna(combined.mean(), inplace=True)

combined.fillna(0, inplace=True)

print(combined.head())

#--------------------------------------------------------------------------------------------------#

#%% 16.Adding a School District Column for Mapping
combined['school_dist'] = combined['DBN'].str[:2]
