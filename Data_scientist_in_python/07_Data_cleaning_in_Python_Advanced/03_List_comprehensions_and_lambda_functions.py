#**************************************************************************************************#
#                                                                                                  #
# 03_List_comprehensions_and_lambda_functions                                                      #
#                                                                                                  #
# Authors: S.G.M. Neves                                                                            #
#                                                                                                  #
#**************************************************************************************************#

#%% 1. The JSON Format
import json

world_cup_str = """
[
    {
        "team_1": "France",
        "team_2": "Croatia",
        "game_type": "Final",
        "score" : [4, 2]
    },
    {
        "team_1": "Belgium",
        "team_2": "England",
        "game_type": "3rd/4th Playoff",
        "score" : [2, 0]
    }
]
"""

world_cup_obj = json.loads(world_cup_str)

#--------------------------------------------------------------------------------------------------#

#%% 2. Reading a JSON file
file = open("hn_2014.json")

hn = json.load(file)

#--------------------------------------------------------------------------------------------------#

#%% 3. Deleting Dictionary Keys
def del_key(dict_, key):
    # create a copy so we don't
    # modify the original dict
    modified_dict = dict_.copy()
    del modified_dict[key]
    return modified_dict

hn_clean = []

for item in hn:
    hn_clean.append(del_key(item, 'createdAtI'))

#--------------------------------------------------------------------------------------------------#

#%% 4. Writing List Comprehensions
hn_clean = [del_key(item, 'createdAtI') for item in hn]

#--------------------------------------------------------------------------------------------------#

#%% 5. Using List Comprehensions to Transform and Create Lists
urls = [item['url'] for item in hn_clean]

#--------------------------------------------------------------------------------------------------#

#%% 6. Using List Comprehensions to Reduce a List
thousand_points = [item for item in hn_clean if item['points'] > 1000]

num_thousand_points = len(thousand_points)

#--------------------------------------------------------------------------------------------------#

#%% 7. Passing Functions as Arguments
def get_n_comments(json_dict):
    return json_dict['numComments']

most_comments = max(hn_clean, key=get_n_comments)

#--------------------------------------------------------------------------------------------------#

#%% 8. Lambda Functions
multiply = lambda a, b: a * b

#--------------------------------------------------------------------------------------------------#

#%% 9. Using Lambda Functions to Analyze JSON data
hn_sorted_points = sorted(hn_clean, key=lambda x: x['points'], reverse=True)

top_5_titles = [item['title'] for item in hn_sorted_points[:5]]

#--------------------------------------------------------------------------------------------------#

#%% 10. Reading JSON files into pandas
import pandas as pd

hn_df = pd.DataFrame(hn_clean)

#--------------------------------------------------------------------------------------------------#

#%% 11. Exploring Tags Using the Apply Function
tags = hn_df['tags']

four_tags = tags[tags.apply(len) == 4]

#--------------------------------------------------------------------------------------------------#

#%% 12. Extracting Tags Using Apply with a Lambda Function
cleaned_tags = tags.apply(lambda x: x[-1] if len(x) == 4 else None)

hn_df['tags'] = cleaned_tags
