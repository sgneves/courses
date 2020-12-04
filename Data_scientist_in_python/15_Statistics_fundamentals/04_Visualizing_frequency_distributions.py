#**************************************************************************************************#
#                                                                                                  #
# 04_Visualizing_frequency_distributions                                                           #
#                                                                                                  #
# Authors: S.G.M. Neves                                                                            #
#                                                                                                  #
#**************************************************************************************************#

#%% 1. Visualizing Distributions
# No code

#--------------------------------------------------------------------------------------------------#

#%% 2. Bar Plots
import pandas as pd

wnba = pd.read_csv("wnba.csv")

def set_exp_cat(exp):

    if exp == "R":
        return "Rookie"

    exp = int(exp)

    if exp <= 3:
        return "Little experience"

    elif exp <= 5:
        return "Experienced"

    elif exp <= 10:
        return "Very experienced"

    else:
        return "Veteran"

wnba["Exp_ordinal"] = wnba["Experience"].apply(set_exp_cat)

freq_table = wnba["Exp_ordinal"].value_counts().iloc[[3,0,2,1,4]]

freq_table.plot.bar()

#--------------------------------------------------------------------------------------------------#

#%% 3. Horizontal Bar Plots
freq_table.plot.barh(title="Number of players in WNBA by level of experience")

#--------------------------------------------------------------------------------------------------#

#%% 4. Pie Charts
freq_table = wnba["Exp_ordinal"].value_counts()

freq_table.plot.pie()

#--------------------------------------------------------------------------------------------------#

#%% 5. Customizing a Pie Chart
import matplotlib.pyplot as plt

freq_table.plot.pie(figsize=(6,6), autopct="%.2f%%",
                    title="Percentage of players in WNBA by level of experience")
plt.ylabel("")

#--------------------------------------------------------------------------------------------------#

#%% 6. Histograms
wnba["PTS"].plot.hist()

#--------------------------------------------------------------------------------------------------#

#%% 7. The Statistics Behind Histograms
print(wnba["Games Played"].describe())

wnba["Games Played"].plot.hist()

#--------------------------------------------------------------------------------------------------#

#%% 8. Histograms as Modified Bar Plots
# No code

#--------------------------------------------------------------------------------------------------#

#%% 9. Binning for Histograms
wnba["Games Played"].plot.hist(range=(1,32), bins=8,
                               title="The distribution of players by games played")
plt.xlabel("Games played")

#--------------------------------------------------------------------------------------------------#

#%% 10. Skewed Distributions
plt.figure()
wnba["AST"].plot.hist()

plt.figure()
wnba["FT%"].plot.hist()

assists_distro = 'right skewed'
ft_percent_distro = 'left skewed'

#--------------------------------------------------------------------------------------------------#

#%% 11. Symmetrical Distributions
plt.subplot(1, 3, 1)
wnba["Age"].plot.hist()
plt.subplot(1, 3, 2)
wnba["Height"].plot.hist()
plt.subplot(1, 3, 3)
wnba["MIN"].plot.hist()

normal_distribution = "Height"
