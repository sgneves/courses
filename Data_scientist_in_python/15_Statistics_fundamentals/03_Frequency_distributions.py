#**************************************************************************************************#
#                                                                                                  #
# 03_Frequency_distributions                                                                       #
#                                                                                                  #
# Authors: S.G.M. Neves                                                                            #
#                                                                                                  #
#**************************************************************************************************#

#%% 1. Simplifying Data
import pandas as pd

pd.options.display.max_rows = 200
pd.options.display.max_columns = 50

wnba = pd.read_csv("wnba.csv")

print(wnba)

#--------------------------------------------------------------------------------------------------#

#%% 2. Frequency Distribution Tables
freq_distro_pos = wnba['Pos'].value_counts()

freq_distro_height = wnba['Height'].value_counts()

#--------------------------------------------------------------------------------------------------#

#%% 3. Sorting Frequency Distribution Tables
age_ascending = wnba['Age'].value_counts().sort_index()

age_descending = wnba['Age'].value_counts().sort_index(ascending=False)

#--------------------------------------------------------------------------------------------------#

#%% 4. Sorting Tables for Ordinal Variables
def make_pts_ordinal(row):
    if row['PTS'] <= 20:
        return 'very few points'
    if (20 < row['PTS'] <=  80):
        return 'few points'
    if (80 < row['PTS'] <=  150):
        return 'many, but below average'
    if (150 < row['PTS'] <= 300):
        return 'average number of points'
    if (300 < row['PTS'] <=  450):
        return 'more than average'
    else:
        return 'much more than average'

wnba['PTS_ordinal_scale'] = wnba.apply(make_pts_ordinal, axis = 1)

pts_ordinal_desc = wnba['PTS_ordinal_scale'].value_counts().iloc[[4,3,0,2,1,5]]

#--------------------------------------------------------------------------------------------------#

#%% 5. Proportions and Percentages
freq_distro_age = wnba['Age'].value_counts(normalize=True).sort_index() * 100

proportion_25 = freq_distro_age[25] / 100
percentage_30 = freq_distro_age[30]
percentage_over_30 = freq_distro_age.loc[30:].sum()
percentage_below_23 = freq_distro_age.loc[:23].sum()

#--------------------------------------------------------------------------------------------------#

#%% 6. Percentiles and Percentile Ranks
from scipy.stats import percentileofscore

percentile_rank_half_less = percentileofscore(wnba["Games Played"], 17, "weak")

percentage_half_more = 100 - percentile_rank_half_less

#--------------------------------------------------------------------------------------------------#

#%% 7. Finding Percentiles with pandas
stats = wnba["Age"].describe(percentiles = [0.5,0.75,0.95])

age_upper_quartile = stats["75%"]
age_middle_quartile = stats["50%"]
age_95th_percentile = stats["95%"]

question1 = True
question2 = False
question3 = True

#--------------------------------------------------------------------------------------------------#

#%% 8. Grouped Frequency Distribution Tables
grouped_freq_table = wnba["PTS"].value_counts(bins=10, normalize=True).sort_index(ascending=False) * 100

#--------------------------------------------------------------------------------------------------#

#%% 9. Information Loss
stats = wnba["MIN"].value_counts(bins=5).sort_index()

#--------------------------------------------------------------------------------------------------#

#%% 10. Readability for Grouped Frequency Tables
intervals = pd.interval_range(start = 0, end = 600, freq = 60)

gr_freq_table_10 = pd.Series([0] * len(intervals), index=intervals)

for val in wnba["PTS"]:

    for interval in intervals:

        if val in interval:

            gr_freq_table_10.loc[interval] += 1
            break

#--------------------------------------------------------------------------------------------------#

#%% 11. Frequency Tables and Continuous Variables
#No code
