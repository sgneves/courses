#**************************************************************************************************#
#                                                                                                  #
# 01_Cleaning_and_preparing_data_in_python                                                         #
#                                                                                                  #
# Authors: S.G.M. Neves                                                                            #
#                                                                                                  #
#**************************************************************************************************#

# 1. Introducing Data Cleaning
num_rows = len(moma)

#--------------------------------------------------------------------------------------------------#

# 2. Reading our MoMA Data Set
from csv import reader

# Open the file and parse the data
opened_file = open('artworks.csv', encoding='utf-8')
read_file = reader(opened_file)

# Convert the read file into a list of lists and remove the first row of the data, which contains
# the column names
moma = list(read_file)
moma = moma[1:]

#--------------------------------------------------------------------------------------------------#

# 3. Replacing Substrings with the replace Method
age1 = "I am thirty-one years old"

age2 = age1.replace('one', 'two')

#--------------------------------------------------------------------------------------------------#

# 4. Cleaning the Nationality and Gender Columns
for item in moma:

    item[2] = item[2].replace('(', '').replace(')', '')
    item[5] = item[5].replace('(', '').replace(')', '')

#--------------------------------------------------------------------------------------------------#

# 5. String Capitalization
for item in moma:

    nationality  = item[2].title()
    if not nationality: nationality = 'Nationality Unknown'
    item[2] = nationality

    genre = item[5].title()
    if not genre: genre = 'Gender Unknown/Other'
    item[5] = genre

#--------------------------------------------------------------------------------------------------#

# 6. Errors During Data Cleaning
def clean_and_convert(date):

    if date != "": date = int(date.replace("(", "").replace(")", ""))

    return date

for item in moma:

    item[3] = clean_and_convert(item[3])
    item[4] = clean_and_convert(item[4])

#--------------------------------------------------------------------------------------------------#

# 7. Parsing Numbers from Complex Strings, Part One
test_data = ["1912", "1929", "1913-1923",
             "(1951)", "1994", "1934",
             "c. 1915", "1995", "c. 1912",
             "(1988)", "2002", "1957-1959",
             "c. 1955.", "c. 1970's",
             "C. 1990-1999"]

bad_chars = ["(",")","c","C",".","s","'", " "]

def strip_characters(string):

    for char in bad_chars:

        string = string.replace(char, '')

    return string

stripped_test_data = []

for string in test_data:

    stripped_test_data.append(strip_characters(string))

#--------------------------------------------------------------------------------------------------#

# 8. Parsing Numbers from Complex Strings, Part Two
def process_date(string):

    if '-' in string:

        dates = [int(date) for date in string.split('-')]

        return round(sum(dates) / 2)
    else:
        return int(string)

processed_test_data = []

for string in stripped_test_data:

    processed_test_data.append(process_date(string))

for item in moma:

    item[6] = process_date(strip_characters(item[6]))
