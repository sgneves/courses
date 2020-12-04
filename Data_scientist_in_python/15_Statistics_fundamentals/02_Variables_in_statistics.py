#**************************************************************************************************#
#                                                                                                  #
# 02_Variables_in_statistics                                                                       #
#                                                                                                  #
# Authors: S.G.M. Neves                                                                            #
#                                                                                                  #
#**************************************************************************************************#

#%% 1. Variables in Statistics
# No code

#--------------------------------------------------------------------------------------------------#

#%% 2. Quantitative and Qualitative Variables
import pandas as pd
wnba = pd.read_csv('wnba.csv')

variables = {'Name': 'qualitative', 'Team': 'qualitative', 'Pos': 'qualitative', 'Height': 'quantitative', 'BMI': 'quantitative',
             'Birth_Place': 'qualitative', 'Birthdate': 'quantitative', 'Age': 'quantitative', 'College': 'qualitative', 'Experience': 'quantitative',
             'Games Played': 'quantitative', 'MIN': 'quantitative', 'FGM': 'quantitative', 'FGA': 'quantitative',
             '3PA': 'quantitative', 'FTM': 'quantitative', 'FTA': 'quantitative', 'FT%': 'quantitative', 'OREB': 'quantitative', 'DREB': 'quantitative',
             'REB': 'quantitative', 'AST': 'quantitative', 'PTS': 'quantitative'}

#--------------------------------------------------------------------------------------------------#

#%% 3. Scales of Measurement
# No code

#--------------------------------------------------------------------------------------------------#

#%% 4. The Nominal Scale
nominal_scale = ["Birth_Place", "College", "Name", "Pos", "Team"]

#--------------------------------------------------------------------------------------------------#

#%% 5. The Ordinal Scale
question1 = True
question2 = False
question3 = False
question4 = True
question5 = False
question6 = False

#--------------------------------------------------------------------------------------------------#

#%% 6. The Interval and Ratio Scales
# No code

#--------------------------------------------------------------------------------------------------#

#%% 7. The Difference Between Ratio and Interval Scales
interval = ["Birthdate", "Weight_deviation"]

ratio = ["15:00", "3P%", "3PA", "Age", "AST", "BLK", "BMI", "DD2", "DREB", "Experience", "FG%",
         "FGA", "FGM", "FT%", "FTA", "FTM", "Games Played", "Height", "MIN", "OREB", "PTS", "REB",
         "STL", "TD3", "TO", "Weight"]
ratio = sorted(ratio)


#--------------------------------------------------------------------------------------------------#

#%% 8. Common Examples of Interval Scales
# No code

#--------------------------------------------------------------------------------------------------#

#%% 9. Discrete and Continuous Variables
ratio_interval_only = {'Height': 'continuous', 'Weight': 'continuous', 'BMI': 'continuous',
                       'Age': 'continuous', 'Games Played': 'discrete', 'MIN': 'continuous',
                       'FGM': 'discrete', 'FGA': 'discrete', 'FG%': 'continuous',
                       '3PA': 'discrete', '3P%': 'continuous', 'FTM': 'discrete',
                       'FTA': 'discrete', 'FT%': 'continuous', 'OREB': 'discrete',
                       'DREB': 'discrete', 'REB': 'discrete', 'AST': 'discrete',
                       'STL': 'discrete', 'BLK': 'discrete', 'TO': 'discrete', 'PTS': 'discrete',
                       'DD2': 'discrete', 'TD3': 'discrete', 'Weight_deviation': 'continuous'}

#--------------------------------------------------------------------------------------------------#

#%% 10. Real Limits
bmi = {21.201: [],
       21.329: [],
       23.875: [],
       24.543: [],
       25.469: []}
