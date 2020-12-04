#**************************************************************************************************#
#                                                                                                  #
# 06_Functions_fundamentals                                                                        #
#                                                                                                  #
# Authors: S.G.M. Neves                                                                            #
#                                                                                                  #
#**************************************************************************************************#

# 1.Functions
a_list = [4444, 8897, 6340, 9896, 4835, 4324, 10, 6445,
          661, 1246, 1000, 7429, 1376, 8121, 647, 1280,
          3993, 4881, 9500, 6701, 1199, 6251, 4432, 37]

sum_manual = 0

for item in a_list:

    sum_manual += item

#--------------------------------------------------------------------------------------------------#

# 2.Built-in Functions
ratings = ['4+', '4+', '4+', '9+', '12+', '12+', '17+', '17+']

content_ratings = {}

for rating in ratings:

    if rating in content_ratings:

        content_ratings[rating] += 1

    else:
        content_ratings[rating] = 1

print(content_ratings)

#--------------------------------------------------------------------------------------------------#

# 3.Creating Our Own Functions
def square(number):

    return number * number

squared_10 = square(10)
squared_16 = square(16)

#--------------------------------------------------------------------------------------------------#

# 4.The Structure of a Function
def add_10(number):

    return number + 10

add_30 = add_10(30)
add_90 = add_10(90)

#--------------------------------------------------------------------------------------------------#

# 5.Parameters and Arguments
def square(number):

    return number * number

squared_6 = square(6)
squared_11 = square(11)

#--------------------------------------------------------------------------------------------------#

# 6.Extract Values From Any Column
from csv import reader

def extract(apps, idx):

    col = []

    for app in apps:

        col.append(app[idx])

    return col

opened_file = open('AppleStore.csv', encoding='utf-8')

read_file = reader(opened_file)

apps_data = list(read_file)

genres = extract(apps_data[1:], 11)

#--------------------------------------------------------------------------------------------------#

# 7.Creating Frequency Tables
from csv import reader

def extract(apps, idx):

    col = []

    for app in apps:

        col.append(app[idx])

    return col

def freq_table(lst):

    table = {}

    for item in lst:

        if item in table:

            table[item] += 1

        else:
            table[item] = 1

    return table

opened_file = open('AppleStore.csv', encoding='utf-8')

read_file = reader(opened_file)

apps_data = list(read_file)

genres = extract(apps_data[1:], 11)

genres_ft = freq_table(genres)

#--------------------------------------------------------------------------------------------------#

# 8.Writing a Single Function
from csv import reader

def freq_table(idx):

    table = {}

    for app in apps_data[1:]:

        item = app[idx]

        if item in table:

            table[item] += 1

        else:
            table[item] = 1

    return table

opened_file = open('AppleStore.csv', encoding='utf-8')

read_file = reader(opened_file)

apps_data = list(read_file)

ratings_ft = freq_table(7)

#--------------------------------------------------------------------------------------------------#

# 9.Reusability and Multiple Parameters
from csv import reader

def freq_table(apps, idx):

    table = {}

    for app in apps:

        item = app[idx]

        if item in table:

            table[item] += 1

        else:
            table[item] = 1

    return table

opened_file = open('AppleStore.csv', encoding='utf-8')

read_file = reader(opened_file)

apps_data = list(read_file)

ratings_ft = freq_table(apps_data[1:], 7)

#--------------------------------------------------------------------------------------------------#

# 10.Keyword and Positional Arguments
from csv import reader

def freq_table(apps, idx):

    table = {}

    for app in apps:

        item = app[idx]

        if item in table:

            table[item] += 1

        else:
            table[item] = 1

    return table

opened_file = open('AppleStore.csv', encoding='utf-8')

read_file = reader(opened_file)

apps_data = list(read_file)

content_ratings_ft = freq_table(apps_data[1:], 10)

ratings_ft = freq_table(apps=apps_data[1:], idx=7)

genres_ft = freq_table(idx=11, apps=apps_data[1:])

#--------------------------------------------------------------------------------------------------#

# 11.Combining Functions
from csv import reader

def extract(data_set, index):

    column = []
    for row in data_set[1:]:
        value = row[index]
        column.append(value)
    return column

def find_sum(a_list):

    a_sum = 0
    for element in a_list:
        a_sum += float(element)
    return a_sum

def find_length(a_list):

    length = 0
    for element in a_list:
        length += 1
    return length

def mean(data_set, index):

    a_list = extract(data_set, index)

    return find_sum(a_list) / find_length(a_list)


opened_file = open('AppleStore.csv', encoding='utf-8')

read_file = reader(opened_file)

apps_data = list(read_file)

avg_price = mean(apps_data, 4)

#--------------------------------------------------------------------------------------------------#

# 12.Debugging Functions
def extract(data_set, index):
    column = []

    for row in data_set[1:]:
        value = row[index]
        column.append(value)

    return column

def find_sum(a_list):
    a_sum = 0
    for element in a_list:
        a_sum += float(element)
    return a_sum

def find_length(a_list):
    length = 0
    for element in a_list:
        length += 1
    return length

def mean(data_set, index):
    column = extract(data_set, index)
    return find_sum(column) / find_length(column)

avg_price = mean(apps_data, 4)
avg_rating = mean(apps_data, 7)
