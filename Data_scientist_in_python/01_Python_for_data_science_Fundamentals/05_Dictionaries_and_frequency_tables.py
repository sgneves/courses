#**************************************************************************************************#
#                                                                                                  #
# 05_Dictionaries_and_frequency_tables                                                             #
#                                                                                                  #
# Authors: S.G.M. Neves                                                                            #
#                                                                                                  #
#**************************************************************************************************#

# 1.Storing Data
content_ratings = ['4+', '9+', '12+', '17+']
numbers = [4433, 987, 1155, 622]

content_rating_numbers = [content_ratings, numbers]

#--------------------------------------------------------------------------------------------------#

# 2.Dictionaries
content_ratings = {'4+': 4433, '9+': 987, '12+': 1155, '17+': 622}

print(content_ratings )

#--------------------------------------------------------------------------------------------------#

# 3.Indexing
content_ratings = {'4+': 4433, '9+': 987, '12+': 1155, '17+': 622}

over_9 = content_ratings['9+']
over_17 = content_ratings['17+']

#--------------------------------------------------------------------------------------------------#

# 4.Alternative Way of Creating a Dictionary
content_ratings = {}
content_ratings['4+'] = 4433
content_ratings['9+'] = 987
content_ratings['12+'] = 1155
content_ratings['17+'] = 622

over_12_n_apps = content_ratings['12+']

#--------------------------------------------------------------------------------------------------#

# 5.Key-Value Pairs
d_1 = {'key_1': 'first_value', 'key_2': 2, 'key_3': 3.14, 'key_4': True, 'key_5': [4,2,1],
       'key_6': {'inner_key' : 6}}

error = True

#--------------------------------------------------------------------------------------------------#

# 6.Checking for Membership
content_ratings = {'4+': 4433, '9+': 987, '12+': 1155, '17+': 622}

is_in_dictionary_1 = '9+' in content_ratings
is_in_dictionary_2 = 987 in content_ratings

if '17+' in content_ratings: result = 'It exists'

print(result)

#--------------------------------------------------------------------------------------------------#

# 7.Counting with Dictionaries
from csv import reader

opened_file = open('AppleStore.csv', encoding='utf-8')

read_file = reader(opened_file)

apps_data = list(read_file)

content_ratings = {'4+': 0, '9+': 0, '12+': 0, '17+': 0}

for app in apps_data[1:]:

    c_rating = app[10]

    if c_rating in content_ratings: content_ratings[c_rating] += 1

print(content_ratings)

#--------------------------------------------------------------------------------------------------#

# 8.Finding the Unique Values
from csv import reader

opened_file = open('AppleStore.csv', encoding='utf-8')

read_file = reader(opened_file)

apps_data = list(read_file)

content_ratings = {}

for app in apps_data[1:]:

    c_rating = app[10]

    if c_rating in content_ratings:

        content_ratings[c_rating] += 1
    else:
        content_ratings[c_rating] = 1

print(content_ratings)

#--------------------------------------------------------------------------------------------------#

# 9.Proportions and Percentages
from csv import reader

opened_file = open('AppleStore.csv', encoding='utf-8')

read_file = reader(opened_file)

apps_data = list(read_file)

genre_counting = {}

for app in apps_data[1:]:

    genre = app[11]

    if genre in genre_counting:

        genre_counting[genre] += 1
    else:
        genre_counting[genre] = 1

print(genre_counting)

#--------------------------------------------------------------------------------------------------#

# 10.Looping over Dictionaries
content_ratings = {'4+': 4433, '12+': 1155, '9+': 987, '17+': 622}
total_number_of_apps = 7197

for rating in content_ratings:

    content_ratings[rating] = content_ratings[rating] / total_number_of_apps * 100

percentage_17_plus = content_ratings['17+']

percentage_15_allowed = 100 - percentage_17_plus

#--------------------------------------------------------------------------------------------------#

# 11.Keeping the Dictionaries Separate
content_ratings = {'4+': 4433, '12+': 1155, '9+': 987, '17+': 622}
total_number_of_apps = 7197

c_ratings_proportions = {}
c_ratings_percentages = {}

for rating in content_ratings:

    c_ratings_proportions[rating] = content_ratings[rating] / total_number_of_apps
    c_ratings_percentages[rating] = content_ratings[rating] / total_number_of_apps * 100

#--------------------------------------------------------------------------------------------------#

# 12.Frequency Tables for Numerical Columns
from csv import reader

opened_file = open('AppleStore.csv', encoding='utf-8')

read_file = reader(opened_file)

apps_data = list(read_file)

data_sizes = []

for app in apps_data[1:]:

    size = float(app[2])

    data_sizes.append(size)

min_size = min(data_sizes)
max_size = max(data_sizes)

#--------------------------------------------------------------------------------------------------#

# 13.Filtering for the Intervals
from csv import reader

opened_file = open('AppleStore.csv', encoding='utf-8')

read_file = reader(opened_file)

apps_data = list(read_file)

apps_rating_count_tot = []

for app in apps_data[1:]:

    rating_count_tot = int(app[5])

    apps_rating_count_tot.append(rating_count_tot)

min_size = min(apps_rating_count_tot)
max_size = max(apps_rating_count_tot)

groups_rating_count_tot = {'0 - 100000': 0, '100000 - 200000': 0, '200000 - 500000': 0,
                           '500000 - 1000000': 0, '1000000+': 0}

for count_tot in apps_rating_count_tot:

    if count_tot <= 100000:

        groups_rating_count_tot['0 - 100000'] += 1

    elif count_tot > 100000 and count_tot <= 200000:

        groups_rating_count_tot['100000 - 200000'] += 1

    elif count_tot > 200000 and count_tot <= 500000:

        groups_rating_count_tot['200000 - 500000'] += 1

    elif count_tot > 500000 and count_tot <= 1000000:

        groups_rating_count_tot['500000 - 1000000'] += 1

    else:
        groups_rating_count_tot['1000000+'] += 1

print(groups_rating_count_tot)
