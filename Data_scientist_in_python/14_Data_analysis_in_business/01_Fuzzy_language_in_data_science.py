#**************************************************************************************************#
#                                                                                                  #
# 01_Fuzzy_language_in_data_science                                                                #
#                                                                                                  #
# Authors: S.G.M. Neves                                                                            #
#                                                                                                  #
#**************************************************************************************************#

#%% 1. Fuzzy Language
# No code

#--------------------------------------------------------------------------------------------------#

#%% 2. Communication is a Two-way Street
ans = "C"

#--------------------------------------------------------------------------------------------------#

#%% 3. Dealing with Fuzzy Language
ans = "A"

#--------------------------------------------------------------------------------------------------#

#%% 4. Churned Customers
import pandas as pd
import datetime as dt

data = pd.read_csv("rfm_xmas19.txt", parse_dates=["trans_date"])

group_by_customer = data.groupby("customer_id")

last_transaction = group_by_customer["trans_date"].max()

best_churn = pd.DataFrame(last_transaction)

cutoff_day = dt.datetime(2019, 10, 16)

best_churn["churned"] = best_churn["trans_date"].apply(lambda x: 1 if x < cutoff_day else 0)

#--------------------------------------------------------------------------------------------------#

#%% 5. Aggregate Data by Customer
best_churn["nr_of_transactions"] = group_by_customer.size()

best_churn["amount_spent"] = group_by_customer["tran_amount"].sum()

best_churn.drop("trans_date", axis=1, inplace=True)

#--------------------------------------------------------------------------------------------------#

#%% 6. Ranking Customers
temp = best_churn["nr_of_transactions"]
best_churn["scaled_tran"] = (temp - temp.min()) / (temp.max() - temp.min())

temp = best_churn["amount_spent"]
best_churn["scaled_amount"] = (temp - temp.min()) / (temp.max() - temp.min())

best_churn["score"] = best_churn[["scaled_tran", "scaled_amount"]].sum(axis=1) / 2 * 100

best_churn.sort_values("score", ascending=False, inplace=True)

#--------------------------------------------------------------------------------------------------#

#%% 7. Determining a Threshold
coupon = 0.3 * data["tran_amount"].mean()

nr_of_customers = 1000 / coupon

#--------------------------------------------------------------------------------------------------#

#%% 8. Delivering the Results
top_50_churned = best_churn.loc[best_churn["churned"] == 1].iloc[:50]

top_50_churned.to_csv("best_customers.txt")
