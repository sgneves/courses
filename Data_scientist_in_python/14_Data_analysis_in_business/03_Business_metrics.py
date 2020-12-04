#**************************************************************************************************#
#                                                                                                  #
# 03_Business_metrics                                                                              #
#                                                                                                  #
# Authors: S.G.M. Neves                                                                            #
#                                                                                                  #
#**************************************************************************************************#

#%% 1. Business Metrics
# No code

#--------------------------------------------------------------------------------------------------#

#%% 2. What's a Good Metric?
ans1 = "no"
ans21 = "no"
ans22 = "yes"

#--------------------------------------------------------------------------------------------------#

#%% 3. Introduction to the Net Promoter Score
def categorize(score):

    if score < 0 or score > 10:
        return None

    elif score <=6:
        return "Detractor"

    elif score <=8:
        return "Passive"

    else:
        return "Promoter"

#--------------------------------------------------------------------------------------------------#

#%% 4. Net Promoter Score
import pandas as pd

df = pd.read_csv("nps.csv", parse_dates=["event_date"])

df["yearmonth"] = df["event_date"].dt.year * 100 + df["event_date"].dt.month

df["category"] = df["score"].apply(categorize)

nps = df.pivot_table(index="yearmonth", columns="category", aggfunc="size")

nps["total_responses"] = nps.sum(axis=1)

nps["nps"] = (nps["Promoter"] - nps["Detractor"]) / nps["total_responses"] * 100
nps["nps"] = nps["nps"].astype("int")

#--------------------------------------------------------------------------------------------------#

#%% 5. Analyzing NPS
# No code

#--------------------------------------------------------------------------------------------------#

#%% 6. Customer Churn
import pandas as pd

subs = pd.read_csv("muscle_labs.csv", parse_dates=["end_date", "start_date"])

subs["churn_month"] = subs["end_date"].dt.year * 100 + subs["end_date"].dt.month

monthly_churn = pd.DataFrame({"total_churned": subs.groupby("churn_month").size()})
monthly_churn["total_churned"]

#--------------------------------------------------------------------------------------------------#

#%% 7. Date Wrangling
years = list(range(2011, 2015))
months = list(range(1, 13))
yearmonths = [y * 100 + m for y in years for m in months][:-1]

churn = pd.DataFrame({"yearmonth": yearmonths})

churn = pd.merge(churn, monthly_churn, "left", left_on="yearmonth", right_index=True)

churn.head()

churn = churn.fillna(0).astype("int")

#--------------------------------------------------------------------------------------------------#

#%% 8. Churn Rate
import datetime as dt
from matplotlib.patches import Ellipse

def total_customers(yearmonth):

    date = dt.datetime.strptime(str(yearmonth), "%Y%m")

    return ((subs["start_date"] < date) & (subs["end_date"] >= date)).sum()

churn["total_customers"] = churn["yearmonth"].apply(total_customers)

churn["churn_rate"] = churn["total_churned"] / churn["total_customers"]

churn["yearmonth"] = churn["yearmonth"].astype("str")

ax = churn.plot(x="yearmonth", y="churn_rate", figsize=(12,6), rot=45, marker=".")

ax.set_xticks(range(1, 47, 3))
ax.set_xticklabels(yearmonths[1::3])
circle = Ellipse((35, churn.loc[churn.yearmonth == "201312", "churn_rate"].iloc[0]),
                  5, 0.065, color='sandybrown', fill=False
                    )
ax.add_artist(circle)
ax.xaxis.label.set_visible(False)
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.get_legend().remove()

#--------------------------------------------------------------------------------------------------#

#%% 9. Investigating Churn

#--------------------------------------------------------------------------------------------------#

#%% 10. Analyzing Churn
