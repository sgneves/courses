#**************************************************************************************************#
#                                                                                                  #
# 04_Working_with_strings_in_Pandas                                                                #
#                                                                                                  #
# Authors: S.G.M. Neves                                                                            #
#                                                                                                  #
#**************************************************************************************************#

# 1. Introduction
import pandas as pd

happiness2015 = pd.read_csv("World_Happiness_2015.csv")
world_dev = pd.read_csv("World_dev.csv")

col_renaming = {'SourceOfMostRecentIncomeAndExpenditureData': 'IESurvey'}

merged = pd.merge(left=happiness2015, right=world_dev, how='left', left_on='Country',
                  right_on='ShortName')

merged.rename(col_renaming, axis=1, inplace=True)

#--------------------------------------------------------------------------------------------------#

# 2. Using Apply to Transform Strings
def extract_last_word(element):

    return str(element).split()[-1]

merged['Currency Apply'] = merged['CurrencyUnit'].apply(extract_last_word)

#--------------------------------------------------------------------------------------------------#

# 3. Vectorized String Methods Overview
merged['Currency Vectorized'] = merged['CurrencyUnit'].str.split().str.get(-1)

merged['Currency Vectorized'].head()

#--------------------------------------------------------------------------------------------------#

# 4. Exploring Missing Values with Vectorized String Methods
lengths = merged['CurrencyUnit'].str.len()

value_counts = lengths.value_counts(dropna=False)

#--------------------------------------------------------------------------------------------------#

# 5. Finding Specific Words in Strings
pattern = r"[Nn]ational accounts"

national_accounts = merged['SpecialNotes'].str.contains(pattern)

national_accounts.head()

#--------------------------------------------------------------------------------------------------#

# 6. Finding Specific Words in Strings Continued
national_accounts = merged['SpecialNotes'].str.contains(pattern, na=False)

merged_national_accounts = merged[national_accounts]

merged_national_accounts.head()

#--------------------------------------------------------------------------------------------------#

# 7. Extracting Substrings from a Series
pattern = r"([1-2][0-9]{3})"

years = merged['SpecialNotes'].str.extract(pattern)

#--------------------------------------------------------------------------------------------------#

# 8. Extracting Substrings from a Series Continued
years = merged['SpecialNotes'].str.extract(pattern, expand=True)

#--------------------------------------------------------------------------------------------------#

# 9. Extracting All Matches of a Pattern from a Series
merged = merged.set_index('Country')

pattern = r"(?P<Years>[1-2][0-9]{3})"

years = merged['IESurvey'].str.extractall(pattern)

value_counts = years['Years'].value_counts()

#--------------------------------------------------------------------------------------------------#

# 10. Extracting More Than One Group of Patterns from a Series
pattern = r"(?P<First_Year>[1-2][0-9]{3})/?(?P<Second_Year>[0-9]{2})?"

years = merged['IESurvey'].str.extractall(pattern)

first_two_year = years['First_Year'].str[:2]

years['Second_Year'] = first_two_year + years['Second_Year']

#--------------------------------------------------------------------------------------------------#

# 11. Challenge: Clean a String Column, Aggregate the Data, and Plot the Results
merged['IncomeGroup'] = (merged['IncomeGroup']
                         .str.upper()
                         .str.replace('INCOME', '')
                         .str.replace(':', '')
                         .str.replace(r'[ ]+', ' ')
                         .str.strip()
                         )

pv_incomes = merged.pivot_table('Happiness Score', 'IncomeGroup')

pv_incomes.plot.bar(ylim=(0,10), rot=30)
