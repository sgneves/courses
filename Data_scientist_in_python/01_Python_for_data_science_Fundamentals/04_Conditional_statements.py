#**************************************************************************************************#
#                                                                                                  #
# 04_Conditional_statements                                                                        #
#                                                                                                  #
# Authors: S.G.M. Neves                                                                            #
#                                                                                                  #
#**************************************************************************************************#

# 1.If Statements
from csv import reader

opened_file = open('AppleStore.csv', encoding='utf-8')

read_file = reader(opened_file)

apps_data = list(read_file)

free_apps_ratings = []

for row in apps_data[1:]:
    rating = float(row[7])
    price = float(row[4])

    if price == 0:

        free_apps_ratings.append(rating)

avg_rating_free = sum(free_apps_ratings) / len(free_apps_ratings)

#--------------------------------------------------------------------------------------------------#

# 2.Booleans
a_price = 0

if a_price == 0: print("This is free")
if a_price == 1: print("This is not free")

#--------------------------------------------------------------------------------------------------#

# 3.The Average Rating of Non-free Apps
from csv import reader

opened_file = open('AppleStore.csv', encoding='utf-8')

read_file = reader(opened_file)

apps_data = list(read_file)

non_free_apps_ratings = []

for row in apps_data[1:]:

    price = float(row[4])
    rating = float(row[7])

    if price != 0.0:

        non_free_apps_ratings.append(rating)

avg_rating_non_free = sum(non_free_apps_ratings) / len(non_free_apps_ratings)

#--------------------------------------------------------------------------------------------------#

# 4.The Average Rating of Gaming Apps
from csv import reader

opened_file = open('AppleStore.csv', encoding='utf-8')

read_file = reader(opened_file)

apps_data = list(read_file)

non_games_ratings = []

for row in apps_data[1:]:

    rating = float(row[7])
    genre  = row[11]

    if genre != 'Games':

        non_games_ratings.append(rating)

avg_rating_non_games = sum(non_games_ratings) / len(non_games_ratings)

#--------------------------------------------------------------------------------------------------#

# 5.Multiple Conditions
from csv import reader

opened_file = open('AppleStore.csv', encoding='utf-8')

read_file = reader(opened_file)

apps_data = list(read_file)

free_games_ratings = []

for row in apps_data[1:]:

    price = float(row[4])
    rating = float(row[7])
    genre = row[11]

    if price == 0 and genre == 'Games':

        free_games_ratings.append(rating)

avg_rating_free_games = sum(free_games_ratings) / len(free_games_ratings)

#--------------------------------------------------------------------------------------------------#

# 6.The or Operator
from csv import reader

opened_file = open('AppleStore.csv', encoding='utf-8')

read_file = reader(opened_file)

apps_data = list(read_file)

games_social_ratings = []

for row in apps_data[1:]:

    rating = float(row[7])
    genre  = row[11]

    if genre == 'Games' or genre == 'Social Networking':

        games_social_ratings.append(rating)

avg_games_social = sum(games_social_ratings) / len(games_social_ratings)

#--------------------------------------------------------------------------------------------------#

# 7.Combining Logical Operators
from csv import reader

opened_file = open('AppleStore.csv', encoding='utf-8')

read_file = reader(opened_file)

apps_data = list(read_file)

non_free_apps_ratings = []

for row in apps_data[1:]:

    price = float(row[4])
    rating = float(row[7])
    genre  = row[11]

    if price != 0 and (genre == 'Games' or genre == 'Social Networking'):

        non_free_apps_ratings.append(rating)

avg_non_free = sum(non_free_apps_ratings) / len(non_free_apps_ratings)

#--------------------------------------------------------------------------------------------------#

# 8.Comparison Operators
from csv import reader

opened_file = open('AppleStore.csv', encoding='utf-8')

read_file = reader(opened_file)

apps_data = list(read_file)

apps_ratings = []

for row in apps_data[1:]:

    price = float(row[4])
    rating = float(row[7])

    if price > 9:

        apps_ratings.append(rating)

n_apps_more_9 = len(apps_ratings)
n_apps_less_9 = len(apps_data) - 1 - n_apps_more_9

avg_rating = sum(apps_ratings) / n_apps_more_9

#--------------------------------------------------------------------------------------------------#

# 9.The else Clause
from csv import reader

opened_file = open('AppleStore.csv', encoding='utf-8')

read_file = reader(opened_file)

apps_data = list(read_file)
apps_data[0].append('free_or_not')

for app in apps_data[1:]:

    price = float(app[4])

    if price == 0:

        app.append('free')
    else:
        app.append('non-free')

#--------------------------------------------------------------------------------------------------#

# 10.The elif Clause
from csv import reader

opened_file = open('AppleStore.csv', encoding='utf-8')

read_file = reader(opened_file)

apps_data = list(read_file)
apps_data[0].append('price_label')

for app in apps_data[1:]:

    price = float(app[4])

    if price == 0:

        app.append('free')

    elif price > 0 and price < 20:

        app.append('affordable')

    elif price >= 20 and price < 50:

        app.append('expensive')

    elif price >= 50:

        app.append('very expensive')
