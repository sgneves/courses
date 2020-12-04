#**************************************************************************************************#
#                                                                                                  #
# 02_Variables_and_data_types                                                                      #
#                                                                                                  #
# Authors: S.G.M. Neves                                                                            #
#                                                                                                  #
#**************************************************************************************************#

result = (42 - 11) * 22
print(result)

#--------------------------------------------------------------------------------------------------#

a_value = 15
a_result = (25 - 7) * 17
print(a_value)
print(a_result + 12)
print(a_value + a_result)

#--------------------------------------------------------------------------------------------------#

# INITIAL CODE
old_income = 34000
new_income = 40000

#--------------------------------------------------------------------------------------------------#

income = 34000
income = income + 6000
print(income)

#--------------------------------------------------------------------------------------------------#

variable_1 = 20
variable_2 = 20
variable_2 += 10
variable_1 *= 4
print(variable_1)
print(variable_2)

#--------------------------------------------------------------------------------------------------#

variable_1 = 10
variable_2 = 2.5
variable_1 += 6.5
variable_2 *= 2
print(variable_1)
print(variable_2)

#--------------------------------------------------------------------------------------------------#

variable_a = 13.9
variable_b = 2.8
variable_a = round(variable_a)
variable_b = int(variable_b)
print(variable_a)
print(variable_b)

#--------------------------------------------------------------------------------------------------#

app_name = "Pandora - Music & Radio"
average_rating = "4.0"
total_ratings = "1724546"
price = "free"
print(app_name)

#--------------------------------------------------------------------------------------------------#

motto = "Facebook's new motto is \"move fast with stable infra.\""
print(motto)

#--------------------------------------------------------------------------------------------------#

facebook = "Facebook's rating is "
fb_rating = 3.5
fb_rating_str = str(fb_rating)
fb = facebook + fb_rating_str
print(fb)
