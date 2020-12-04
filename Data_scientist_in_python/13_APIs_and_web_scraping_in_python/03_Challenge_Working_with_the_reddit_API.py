#**************************************************************************************************#
#                                                                                                  #
# 03_Challenge_Working_with_the_reddit_API                                                         #
#                                                                                                  #
# Authors: S.G.M. Neves                                                                            #
#                                                                                                  #
#**************************************************************************************************#

#%% 1. Reddit
# No code

#--------------------------------------------------------------------------------------------------#

#%% 2. Authenticating with the API
headers = {"Authorization": "bearer 13426216-4U1ckno9J5AiK72VRbpEeBaMSKk",
           "User-Agent": "Dataquest/1.0"}

response = requests.get("https://oauth.reddit.com/r/python/top", headers=headers,
                        params={"t":"day"})

python_top = response.json()

#--------------------------------------------------------------------------------------------------#

#%% 3. Getting the Most Upvoted Post
import numpy as np

python_top_articles = python_top['data']['children']

idx = np.argmax([i['data']['ups'] for i in python_top_articles])

most_upvoted = python_top_articles[idx]['data']['id']

#--------------------------------------------------------------------------------------------------#

#%% 4. Getting Post Comments
response = requests.get("https://oauth.reddit.com/r/python/comments/" + most_upvoted,
                        headers=headers)

comments = response.json()

#--------------------------------------------------------------------------------------------------#

#%% 5. Getting the Most Upvoted Comment
comments_list = comments[1]['data']['children']

idx = np.argmax([i['data']['ups'] for i in comments_list])

most_upvoted_comment = comments_list[idx]['data']['id']

#--------------------------------------------------------------------------------------------------#

#%% 6. Upvoting a Comment
payload = {"dir": 1, 'id': most_upvoted_comment}

response = requests.post("https://oauth.reddit.com/api/vote", json=payload, headers=headers)

status = response.status_code
