#**************************************************************************************************#
#                                                                                                  #
# 05_Working_with_missing_and_duplicate_data                                                       #
#                                                                                                  #
# Authors: S.G.M. Neves                                                                            #
#                                                                                                  #
#**************************************************************************************************#

# 1. Introduction
import pandas as pd

happiness2015 = pd.read_csv("wh_2015.csv")
happiness2016 = pd.read_csv("wh_2016.csv")
happiness2017 = pd.read_csv("wh_2017.csv")

shape_2015 = happiness2015.shape
shape_2016 = happiness2016.shape
shape_2017 = happiness2017.shape

#--------------------------------------------------------------------------------------------------#

# 2. Identifying Missing Values
missing_2015 = happiness2015.isnull().sum()
missing_2016 = happiness2016.isnull().sum()
missing_2017 = happiness2017.isnull().sum()

#--------------------------------------------------------------------------------------------------#

# 3. Correcting Data Cleaning Errors that Result in Missing Values
def rename_col(col):

    col = (col
           .str.replace('.', ' ')
           .str.replace('[()]', '')
           .str.replace('\s+', ' ')
           .str.strip()
           .str.upper()
           )

    return col

happiness2015.columns = rename_col(happiness2015.columns)
happiness2016.columns = rename_col(happiness2016.columns)
happiness2017.columns = rename_col(happiness2017.columns)

combined = pd.concat([happiness2015, happiness2016, happiness2017], ignore_index=True)

missing = combined.isnull().sum()

#--------------------------------------------------------------------------------------------------#

# 4. Visualizing Missing Data
regions_2017 = combined.loc[combined['YEAR'] == 2017,"REGION"]

missing = regions_2017.isnull().sum()

#--------------------------------------------------------------------------------------------------#

# 5. Using Data From Additional Sources to Fill in Missing Values
regions = combined[['COUNTRY','REGION']].dropna().drop_duplicates()

combined = combined.merge(regions, 'left', 'COUNTRY')

combined.drop('REGION_x', axis=1, inplace=True)

missing = combined.isnull().sum()

#--------------------------------------------------------------------------------------------------#

# 6. Identifying Duplicates Values
combined.rename({'REGION_y': 'REGION'}, axis=1, inplace=True)

combined['COUNTRY'] = combined['COUNTRY'].str.upper()

dups = combined.duplicated(['COUNTRY', 'YEAR'])

combined[dups]

#--------------------------------------------------------------------------------------------------#

# 7. Correcting Duplicates Values
combined.drop_duplicates(['COUNTRY', 'YEAR'], inplace=True)

#--------------------------------------------------------------------------------------------------#

# 8. Handle Missing Values by Dropping Columns
columns_to_drop = ['LOWER CONFIDENCE INTERVAL', 'STANDARD ERROR', 'UPPER CONFIDENCE INTERVAL',
                   'WHISKER HIGH', 'WHISKER LOW']

combined.drop(columns_to_drop, axis=1, inplace=True)

missing = combined.isnull().sum()

#--------------------------------------------------------------------------------------------------#

# 9. Handle Missing Values by Dropping Columns Continued
combined.dropna(axis=1, thresh=159, inplace=True)

missing = combined.isnull().sum()

#--------------------------------------------------------------------------------------------------#

# 10. Analyzing Missing Data
# No code

#--------------------------------------------------------------------------------------------------#

# 11. Handling Missing Values with Imputation
happiness_mean = combined['HAPPINESS SCORE'].mean()

print(happiness_mean)

combined['HAPPINESS SCORE UPDATED'] =  combined['HAPPINESS SCORE'].fillna(happiness_mean)

print(combined['HAPPINESS SCORE UPDATED'].mean())

#--------------------------------------------------------------------------------------------------#

# 12. Dropping Rows
combined.dropna(inplace=True)

missing = combined.isnull().sum()
