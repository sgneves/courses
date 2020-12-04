#**************************************************************************************************#
#                                                                                                  #
# 01_Data_cleaning_walkthrough                                                                     #
#                                                                                                  #
# Authors: S.G.M. Neves                                                                            #
#                                                                                                  #
#**************************************************************************************************#

#%% 1.Introduction
# No code

#--------------------------------------------------------------------------------------------------#

#%% 2.Finding All of the Relevant Data Sets
# No code

#--------------------------------------------------------------------------------------------------#

#%% 3.Finding Background Information
# No code

#--------------------------------------------------------------------------------------------------#

#%% 4.Reading in the Data
import pandas as pd

data_files = [
    "ap_2010.csv",
    "class_size.csv",
    "demographics.csv",
    "graduation.csv",
    "hs_directory.csv",
    "sat_results.csv"
]

data = {}

for file in data_files:

    data[file[:-4]] = pd.read_csv('schools/' + file)

#--------------------------------------------------------------------------------------------------#

#%% 5.Exploring the SAT Data
print(data['sat_results'].head(5))

#--------------------------------------------------------------------------------------------------#

#%% 6.Exploring the Remaining Data
for k in data:

    print(data[k].head(5))

#--------------------------------------------------------------------------------------------------#

#%% 7.Reading in the Survey Data
# No code

#--------------------------------------------------------------------------------------------------#

#%% 8.Reading in the Survey Data
all_survey = pd.read_csv('schools/survey_all.txt', delimiter="\t", encoding="windows-1252")
d75_survey = pd.read_csv('schools/survey_d75.txt', delimiter="\t", encoding="windows-1252")

survey = pd.concat([all_survey, d75_survey])

survey.head()

#--------------------------------------------------------------------------------------------------#

#%% 9.Cleaning Up the Surveys
survey['DBN'] = survey['dbn']

cols = ["DBN", "rr_s", "rr_t", "rr_p", "N_s", "N_t", "N_p", "saf_p_11", "com_p_11", "eng_p_11",
        "aca_p_11", "saf_t_11", "com_t_11", "eng_t_11", "aca_t_11", "saf_s_11", "com_s_11",
        "eng_s_11", "aca_s_11", "saf_tot_11", "com_tot_11", "eng_tot_11", "aca_tot_11"]

survey = survey[cols]

data['survey'] = survey[cols]

#--------------------------------------------------------------------------------------------------#

#%% 10.Inserting DBN Fields
# No code

#--------------------------------------------------------------------------------------------------#

#%% 11.Inserting DBN Fields
data['hs_directory']['DBN'] = data['hs_directory']['dbn']

data['class_size']['padded_csd'] = data['class_size']['CSD'].astype(str).str.zfill(2)

data['class_size']['DBN'] = data['class_size']['padded_csd'] + data['class_size']['SCHOOL CODE']

print(data['class_size'].head())

#--------------------------------------------------------------------------------------------------#

#%% 12.Combining the SAT Scores
cols = ['SAT Math Avg. Score','SAT Critical Reading Avg. Score','SAT Writing Avg. Score']

for col in cols:

    data['sat_results'][col] = pd.to_numeric(data['sat_results'][col], errors="coerce")

data['sat_results']['sat_score'] = data['sat_results'].loc[:,cols].sum(axis=1)

print(data['sat_results']['sat_score'])

#--------------------------------------------------------------------------------------------------#

#%% 13.Parsing Geographic Coordinates for Schools
data['hs_directory']['lat'] = data['hs_directory']['Location 1'].str.extract(r"\(([+\-\d.]+),\s*[+\-\d.]+\)")

#--------------------------------------------------------------------------------------------------#

#%% 14.Extracting the Longitude
data['hs_directory']['lon'] = data['hs_directory']['Location 1'].str.extract(r"\([+\-\d.]+,\s*([+\-\d.]+)\)")

data['hs_directory']['lat'] = pd.to_numeric(data['hs_directory']['lat'], errors="coerce")
data['hs_directory']['lon'] = pd.to_numeric(data['hs_directory']['lon'], errors="coerce")
