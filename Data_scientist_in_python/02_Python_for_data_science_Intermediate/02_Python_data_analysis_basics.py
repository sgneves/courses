#**************************************************************************************************#
#                                                                                                  #
# 02_Python_data_analysis_basics                                                                   #
#                                                                                                  #
# Authors: S.G.M. Neves                                                                            #
#                                                                                                  #
#**************************************************************************************************#

# 1. Reading our MoMA Data Set
from csv import reader

# Read the 'artworks_clean.csv' file
opened_file = open('artworks_clean.csv', encoding='utf-8')
read_file = reader(opened_file)
moma = list(read_file)
moma = moma[1:]

def convert_date(date):

    if date != "": date = int(date)

    return date

# Convert the birthdate values
for row in moma:

    row[3] = convert_date(row[3])
    row[4] = convert_date(row[4])
    row[6] = convert_date(row[6])

#--------------------------------------------------------------------------------------------------#

# 2. Calculating Artist Ages
ages = []

for row in moma:

    birth = row[3]
    date = row[6]

    if type(birth) == int:

        age = date - birth
    else:
        age = 0

    ages.append(age)

final_ages = [age if age > 20 else 'Unknown' for age in ages]

#--------------------------------------------------------------------------------------------------#

# 3. Converting Ages to Decades
decades = []

for age in final_ages:

    if age != 'Unknown':

        age = str(age)[:-1] + '0s'

    decades.append(age)

#--------------------------------------------------------------------------------------------------#

# 4. Summarizing the Decade Data
decade_frequency = {}

for decade in decades:

    if decade in decade_frequency:

        decade_frequency[decade] += 1
    else:
        decade_frequency[decade] = 1

#--------------------------------------------------------------------------------------------------#

# 5. Inserting Variables Into Strings
artist = "Pablo Picasso"
birth_year = 1881

template = '{}\'s birth year is {}'

output = template.format(artist, birth_year)

print(output)

#--------------------------------------------------------------------------------------------------#

# 6. Creating an Artist Frequency Table
artist_freq = {}

for artwork in moma:

    artist = artwork[1]

    if artist in artist_freq:

        artist_freq[artist] += 1
    else:
        artist_freq[artist] = 1

#--------------------------------------------------------------------------------------------------#

# 7. Creating an Artist Summary Function
def artist_summary(artist):

    print('There are {} artworks by {} in the data set'.format(artist_freq[artist], artist))

artist_summary('Henri Matisse')

#--------------------------------------------------------------------------------------------------#

# 8. Formatting Numbers Inside Strings
pop_millions = [
    ["China", 1379.302771],
    ["India", 1281.935991],
    ["USA",  326.625791],
    ["Indonesia",  260.580739],
    ["Brazil",  207.353391],
]

for pop in pop_millions:

    print('The population of {} is {:,.2f} million'.format(pop[0], pop[1]))

#--------------------------------------------------------------------------------------------------#

# 9. Challenge: Summarizing Artwork Gender Data
gender_freq = {}

for artwork in moma:

    gender = artwork[5]

    if gender in gender_freq:

        gender_freq[gender] += 1
    else:
        gender_freq[gender] = 1

for k, v in gender_freq.items():

    print('There are {:,} artworks by {} artists'.format(v, k))
