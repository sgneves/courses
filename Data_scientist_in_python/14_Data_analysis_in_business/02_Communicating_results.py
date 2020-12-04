#**************************************************************************************************#
#                                                                                                  #
# 02_Communicating_results                                                                         #
#                                                                                                  #
# Authors: S.G.M. Neves                                                                            #
#                                                                                                  #
#**************************************************************************************************#

#%% 1. Business Context

#--------------------------------------------------------------------------------------------------#

#%% 2. The Scenario
import pandas as pd

playstore = pd.read_csv("googleplaystore.csv")

print(playstore.shape)

answer = "no"

playstore.drop(10472, inplace=True)

#--------------------------------------------------------------------------------------------------#

#%% 3. Cleaning the Data
import numpy as np

def clean_size(size):
    """Convert file size string to float and megabytes"""
    size = size.replace("M","")
    if size.endswith("k"):
        size = float(size[:-1])/1000
    elif size == "Varies with device":
        size = np.NaN
    else:
        size = float(size)
    return size

playstore["Price"] = playstore["Price"].str.replace("$", "").astype("float")

paid = playstore[playstore["Price"] != 0].copy()

paid.drop("Type", axis=1, inplace=True)

paid["Reviews"] = paid["Reviews"].astype("int")

paid["Size"] = paid["Size"].apply(clean_size)

paid.info()

#--------------------------------------------------------------------------------------------------#

#%% 4. Removing Duplicates
paid.drop_duplicates(inplace=True)

paid.drop([2151, 4301], inplace=True)

paid.sort_values("Reviews", ascending=False, inplace=True)

paid.drop_duplicates("App", inplace=True)

print(paid.duplicated("App").sum())

paid.reset_index(drop=True, inplace=True)

#--------------------------------------------------------------------------------------------------#

#%% 5. Exploring the Price
affordable_apps = paid[paid["Price"] < 50].copy()

cheap = affordable_apps["Price"] < 5

reasonable = affordable_apps["Price"] >= 5

affordable_apps[cheap].hist(column="Price", grid=False, figsize=(12,6))

affordable_apps[reasonable].hist(column="Price", grid=False, figsize=(12,6))

affordable_apps.loc[cheap, "affordability"] = "cheap"
affordable_apps.loc[reasonable, "affordability"] = "reasonable"

#--------------------------------------------------------------------------------------------------#

#%% 6. Price vs. Rating
cheap_mean = affordable_apps.loc[cheap, "Price"].mean()

affordable_apps.loc[cheap, "price_criterion"] = affordable_apps.loc[cheap, "Price"].apply(lambda x: 1 if x < cheap_mean else 0)

affordable_apps[reasonable].plot(kind="scatter", x="Price", y="Rating")

reasonable_mean = affordable_apps.loc[reasonable, "Price"].mean()

affordable_apps.loc[reasonable, "price_criterion"] = affordable_apps.loc[reasonable, "Price"].apply(lambda x: 1 if x < reasonable_mean else 0)

#--------------------------------------------------------------------------------------------------#

#%% 7. Price vs Category and Genres
affordable_apps["genre_count"] = affordable_apps["Genres"].str.count(";") + 1

genres_mean = affordable_apps.groupby(["affordability", "genre_count"])["Price"].mean()

def label_genres(row):
    """For each segment in `genres_mean`,
    labels the apps that cost less than its segment's mean with `1`
    and the others with `0`."""

    if row["Price"] < genres_mean.loc[(row["affordability"], row["genre_count"])]:
        return 1
    else:
        return 0

affordable_apps["genre_criterion"] = affordable_apps.apply(label_genres, axis="columns")

categories_mean = affordable_apps.groupby(["affordability", "Category"])["Price"].mean()

def label_categories(row):

    if row["Price"] < categories_mean.loc[(row["affordability"], row["Category"])]:
        return 1
    else:
        return 0

affordable_apps["category_criterion"] = affordable_apps.apply(label_categories, axis="columns")

#--------------------------------------------------------------------------------------------------#

#%% 8. Results and Impact
criteria = ["price_criterion", "genre_criterion", "category_criterion"]
affordable_apps["Result"] = affordable_apps[criteria].mode(axis=1)

affordable_apps.loc[cheap, "New Price"] = affordable_apps.loc[cheap, "Price"].apply(lambda x: max([x, cheap_mean]))
affordable_apps.loc[reasonable, "New Price"] = affordable_apps.loc[reasonable, "Price"].apply(lambda x: max([x, reasonable_mean]))

affordable_apps["New Price"] = affordable_apps["New Price"].round(2)


affordable_apps["Installs"] = (affordable_apps["Installs"]
                               .str.replace("+", "")
                               .str.replace(",", "")
                               .astype("int")
                               )

affordable_apps["Impact"] = (affordable_apps["New Price"] - affordable_apps["Price"]) * affordable_apps["Installs"]

total_impact = affordable_apps["Impact"].sum()
print(total_impact)

#--------------------------------------------------------------------------------------------------#

#%% 9. Next Steps
# No code

#--------------------------------------------------------------------------------------------------#

#%% 10. Communicating Your Work I
# No code

#--------------------------------------------------------------------------------------------------#

#%% 11. Communicating Your Work II

#--------------------------------------------------------------------------------------------------#

#%% 12. Business Workflow
