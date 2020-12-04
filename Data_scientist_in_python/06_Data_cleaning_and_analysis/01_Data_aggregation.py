#**************************************************************************************************#
#                                                                                                  #
# 01_Data_aggregation                                                                              #
#                                                                                                  #
# Authors: S.G.M. Neves                                                                            #
#                                                                                                  #
#**************************************************************************************************#

# 1. Introduction
# No code

#--------------------------------------------------------------------------------------------------#

# 2. Introduction to the Data
import pandas as pd

happiness2015 = pd.read_csv("World_Happiness_2015.csv")

first_5 = happiness2015[:5]

happiness2015.info()

#--------------------------------------------------------------------------------------------------#

# 3. Using Loops to Aggregate Data
regions = happiness2015["Region"].unique()

mean_happiness = {}

for region in regions:

    mean_happiness[region] = happiness2015.loc[happiness2015["Region"]==region,"Happiness Score"].mean()

#--------------------------------------------------------------------------------------------------#

# 4. The GroupBy Operation
# No code

#--------------------------------------------------------------------------------------------------#

# 5. Creating GroupBy Objects
grouped = happiness2015.groupby("Region")

aus_nz = grouped.get_group("Australia and New Zealand")

#--------------------------------------------------------------------------------------------------#

# 6. Exploring GroupBy Objects
north_america = happiness2015.loc[[4,14]]

na_group = grouped.get_group("North America")

equal = north_america == na_group

#--------------------------------------------------------------------------------------------------#

# 7. Common Aggregation Methods with Groupby
means = grouped.mean()

#--------------------------------------------------------------------------------------------------#

# 8. Aggregating Specific Columns with Groupby
happy_grouped = grouped["Happiness Score"]

happy_mean = happy_grouped.mean()

#--------------------------------------------------------------------------------------------------#

# 9. Introduction to the Agg() Method
import numpy as np

def dif(group):
    return (group.max() - group.mean())

happy_mean_max = happy_grouped.agg([np.mean, np.max])

mean_max_dif = happy_grouped.agg(dif)

#--------------------------------------------------------------------------------------------------#

# 10. Computing Multiple and Custom Aggregations with the Agg() Method
happiness_means = happiness2015.groupby('Region')['Happiness Score'].mean()

#--------------------------------------------------------------------------------------------------#

# 11. Aggregation with Pivot Tables
pv_happiness = happiness2015.pivot_table(values='Happiness Score', index='Region', aggfunc=np.mean,
                                         margins=True)

pv_happiness.plot.barh(title='Mean Happiness Scores by Region', xlim=(0,10), legend=False)

world_mean_happiness = happiness2015['Happiness Score'].mean()

#--------------------------------------------------------------------------------------------------#

# 12. Aggregating Multiple Columns and Functions with Pivot Tables
grouped = happiness2015.groupby("Region")['Happiness Score','Family']

happy_family_stats = grouped.agg([np.min,np.max,np.mean])

pv_happy_family_stats = happiness2015.pivot_table(['Happiness Score','Family'], 'Region',
                                                  aggfunc=[np.min,np.max,np.mean], margins=True)
