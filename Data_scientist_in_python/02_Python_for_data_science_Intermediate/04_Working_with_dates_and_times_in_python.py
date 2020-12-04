#**************************************************************************************************#
#                                                                                                  #
# 04_Working_with_dates_and_times_in_python                                                        #
#                                                                                                  #
# Authors: S.G.M. Neves                                                                            #
#                                                                                                  #
#**************************************************************************************************#

# 1. Introduction
from csv import reader

# Open the file and parse the data
opened_file = open('potus_visitors_2015.csv', encoding='utf-8')
read_file = reader(opened_file)

# Convert the read file into a list of lists and remove the first row of the data, which contains
# the column names
potus = list(read_file)
potus = potus[1:]

#--------------------------------------------------------------------------------------------------#

# 2. Importing Modules
# No code

#--------------------------------------------------------------------------------------------------#

# 3. The Datetime Module
import datetime as dt

#--------------------------------------------------------------------------------------------------#

# 4. The Datetime Class
import datetime as dt

ibm_founded = dt.datetime(1911, 6, 16)
man_on_moon = dt.datetime(1969, 7, 20, 20, 17)

#--------------------------------------------------------------------------------------------------#

# 5. Using Strptime to Parse Strings as Dates
date_format = "%m/%d/%y %H:%M"

for row in potus:

    row[2] = dt.datetime.strptime(row[2], date_format)

#--------------------------------------------------------------------------------------------------#

# 6. Using Strftime to format dates
visitors_per_month = {}

for row in potus:

    date = row[2].strftime("%B, %Y")

    if date in visitors_per_month:

        visitors_per_month[date] += 1
    else:
        visitors_per_month[date] = 1

#--------------------------------------------------------------------------------------------------#

# 7. The Time Class
appt_times = [row[2].time() for row in potus]

#--------------------------------------------------------------------------------------------------#

# 8. Comparing time objects
min_time = min(appt_times)
max_time = max(appt_times)

#--------------------------------------------------------------------------------------------------#

# 9. Calculations with Dates and Times
dt_1 = dt.datetime(1981, 1, 31)
dt_2 = dt.datetime(1984, 6, 28)
dt_3 = dt.datetime(2016, 5, 24)
dt_4 = dt.datetime(2001, 1, 1, 8, 24, 13)

answer_1 = dt_2 - dt_1
answer_2 = dt_3 + dt.timedelta(56)
answer_3 = dt_4 - dt.timedelta(0, 3600)

#--------------------------------------------------------------------------------------------------#

# 10. Summarizing Appointment Lengths
appt_lengths = {}

for row in potus:

    row[3] = dt.datetime.strptime(row[3], date_format)

    length = row[3] - row[2]

    if length in appt_lengths:

        appt_lengths[length] += 1
    else:
        appt_lengths[length] = 1

min_length = min(appt_lengths.keys())
max_length = max(appt_lengths.keys())
