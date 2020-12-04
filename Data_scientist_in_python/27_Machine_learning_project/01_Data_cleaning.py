#**************************************************************************************************#
#                                                                                                  #
# 01_Data_cleaning                                                                                 #
#                                                                                                  #
# Authors: S.G.M. Neves                                                                            #
#                                                                                                  #
#**************************************************************************************************#

#%% 1. Introduction
# No code

#--------------------------------------------------------------------------------------------------#

#%% 2. Introduction to the data
# No code

#--------------------------------------------------------------------------------------------------#

#%% 3. Reading in to Pandas
import pandas as pd

loans_2007 = pd.read_csv('loans_2007.csv', low_memory=False)
print(loans_2007.iloc[0])

print(loans_2007.shape)

#--------------------------------------------------------------------------------------------------#

#%% 4. First group of columns
# No code

#--------------------------------------------------------------------------------------------------#

#%% 5. First group of columns
cols = ['id','member_id','funded_amnt','funded_amnt_inv','grade','sub_grade','emp_title','issue_d']

loans_2007.drop(cols, axis=1, inplace=True)

#--------------------------------------------------------------------------------------------------#

#%% 6. Second group of features
# No code

#--------------------------------------------------------------------------------------------------#

#%% 7. Second group of features
cols = ['zip_code','out_prncp','out_prncp_inv','total_pymnt','total_pymnt_inv','total_rec_prncp']

loans_2007.drop(cols, axis=1, inplace=True)

#--------------------------------------------------------------------------------------------------#

#%% 8. Third group of features
# No code

#--------------------------------------------------------------------------------------------------#

#%% 9. Third group of features
cols = ['total_rec_int','total_rec_late_fee','recoveries','collection_recovery_fee','last_pymnt_d',
        'last_pymnt_amnt']

loans_2007.drop(cols, axis=1, inplace=True)

#--------------------------------------------------------------------------------------------------#

#%% 10. Target column
print(loans_2007['loan_status'].value_counts())

#--------------------------------------------------------------------------------------------------#

#%% 11. Binary classification
# No code

#--------------------------------------------------------------------------------------------------#

#%% 12. Binary classification
loans_2007 = loans_2007[(loans_2007['loan_status'] == 'Fully Paid')
                        | (loans_2007['loan_status'] == 'Charged Off')].copy()

loans_2007['loan_status'] = loans_2007['loan_status'].str.replace('Fully Paid', '1')
loans_2007['loan_status'] = loans_2007['loan_status'].str.replace('Charged Off', '0')
loans_2007['loan_status'] = loans_2007['loan_status'].astype('int')

#--------------------------------------------------------------------------------------------------#

#%% 13. Removing single value columns
def count_unique_values(row):

    non_null = row.dropna()
    unique_non_null = non_null.unique()

    return len(unique_non_null)

unique_values = loans_2007.apply(count_unique_values)

loans_2007.drop(unique_values[unique_values == 1].index, axis=1, inplace=True)
