#**************************************************************************************************#
#                                                                                                  #
# 05_Comparing_frequency_distributions                                                             #
#                                                                                                  #
# Authors: S.G.M. Neves                                                                            #
#                                                                                                  #
#**************************************************************************************************#

#%% 1. Comparing Frequency Distributions
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

rookies = wnba[wnba['Exp_ordinal'] == 'Rookie']
little_xp = wnba[wnba['Exp_ordinal'] == 'Little experience']
experienced = wnba[wnba['Exp_ordinal'] == 'Experienced']
very_xp = wnba[wnba['Exp_ordinal'] == 'Very experienced']
veterans =  wnba[wnba['Exp_ordinal'] == 'Veteran']

rookie_distro = rookies["Pos"].value_counts()
little_xp_distro = little_xp["Pos"]
experienced_distro = experienced["Pos"]
very_xp_distro = very_xp["Pos"]
veteran_distro = veterans["Pos"]

print(rookie_distro)
print(little_xp_distro)
print(experienced_distro)
print(very_xp_distro)
print(veteran_distro)

#--------------------------------------------------------------------------------------------------#

#%% 2. Grouped Bar Plots
import seaborn as sns

sns.countplot(x="Exp_ordinal", hue="Pos", data=wnba,
              order=["Rookie", "Little experience", "Experienced", "Very experienced", "Veteran"],
              hue_order=["C", "F", "F/C", "G", "G/F"])

#--------------------------------------------------------------------------------------------------#

#%% 3. Challenge: Do Older Players Play Less?
wnba['age_mean_relative'] = wnba['Age'].apply(lambda x: 'old' if x >= 27 else 'young')
wnba['min_mean_relative'] = wnba['MIN'].apply(lambda x: 'average or above' if x >= 497 else 'below average')

sns.countplot(x="age_mean_relative", hue="min_mean_relative", data=wnba)

result = "rejection"

#--------------------------------------------------------------------------------------------------#

#%% 4. Comparing Histograms
import matplotlib.pyplot as plt

wnba[wnba.Age >= 27]['MIN'].plot.hist(histtype = 'step', label = 'Old', legend = True)
wnba[wnba.Age < 27]['MIN'].plot.hist(histtype = 'step', label = 'Young', legend = True)

plt.axvline(497, label="Average")
plt.legend()
plt.show()

#--------------------------------------------------------------------------------------------------#

#%% 5. Kernel Density Estimate Plots
wnba[wnba.Age >= 27]['MIN'].plot.kde(label = 'Old', legend = True)
wnba[wnba.Age < 27]['MIN'].plot.kde(label = 'Young', legend = True)

plt.axvline(497, label="Average")
plt.legend()
plt.show()

#--------------------------------------------------------------------------------------------------#

#%% 6. Drawbacks of Kernel Density Plots
# No code

#--------------------------------------------------------------------------------------------------#

#%% 7. Strip Plots
sns.stripplot(x='Pos', y='Weight', data=wnba, jitter = True)
plt.show()

#--------------------------------------------------------------------------------------------------#

#%% 8. Box plots
sns.boxplot(x='Pos', y='Weight', data=wnba)
plt.show()

#--------------------------------------------------------------------------------------------------#

#%% 9. Outliers
iqr = 29 - 22
lower_bound = 22 - 1.5 * iqr
upper_bound = 29 + 1.5 * iqr

outliers_low = sum(wnba['Games Played'] < lower_bound)
outliers_high = sum(wnba['Games Played'] > upper_bound)

sns.boxplot(x=wnba['Games Played'])
plt.show()
