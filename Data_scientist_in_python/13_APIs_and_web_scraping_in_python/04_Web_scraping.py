#**************************************************************************************************#
#                                                                                                  #
# 04_Web_scraping                                                                                  #
#                                                                                                  #
# Authors: S.G.M. Neves                                                                            #
#                                                                                                  #
#**************************************************************************************************#

#%% 1. Introduction
# No code

#--------------------------------------------------------------------------------------------------#

#%% 2. Web Page Structure
import requests

response = requests.get("http://dataquestio.github.io/web-scraping-pages/simple.html")

content = response.content

#--------------------------------------------------------------------------------------------------#

#%% 3. Retrieving Elements from a Page
from bs4 import BeautifulSoup

# Initialize the parser, and pass in the content we grabbed earlier.
parser = BeautifulSoup(content, 'html.parser')

# Get the body tag from the document. Since we passed in the top level of the document to the
# parser, we need to pick a branch off of the root. we can access branches by using tag types as
# attributes.
body = parser.body

# Get the p tag from the body.
p = body.p

# Print the text inside the p tag. Text is a property that gets the inside text of a tag.
print(p.text)

# Get the text inside the title tag
title_text = parser.head.title.text


#--------------------------------------------------------------------------------------------------#

#%% 4. Using Find All

# Get a list of all occurrences of the body tag in the element.
body = parser.find_all("body")

# Get the text inside the paragraph tag
p = body[0].find_all("p")
print(p[0].text)

# Get the text inside the title tag
title_text = parser.find_all("title")[0].text

#--------------------------------------------------------------------------------------------------#

#%% 5. Element IDs

# Get the page content and set up a new parser.
response = requests.get("http://dataquestio.github.io/web-scraping-pages/simple_ids.html")

parser = BeautifulSoup(response.content, 'html.parser')

# Get the text of the first paragraph
first_paragraph_text = parser.find_all("p", id="first")[0].text
print(first_paragraph_text)

# Get the text of the second paragraph
second_paragraph_text = parser.find_all("p", id="second")[0].text
print(second_paragraph_text)

#--------------------------------------------------------------------------------------------------#

#%% 6. Element Classes

# Get the page content and set up a new parser.
response = requests.get("http://dataquestio.github.io/web-scraping-pages/simple_classes.html")

parser = BeautifulSoup(response.content, 'html.parser')

# Get the first inner paragraph.
first_inner_paragraph_text = parser.find_all("p", class_="inner-text")[0].text
print(first_inner_paragraph_text)

# Get the second inner paragraph.
second_inner_paragraph_text = parser.find_all("p", class_="inner-text")[1].text
print(second_inner_paragraph_text)

# Get the first outer paragraph.
first_outer_paragraph_text = parser.find_all("p", class_="outer-text")[0].text
print(first_outer_paragraph_text)

#--------------------------------------------------------------------------------------------------#

#%% 7. CSS Selectors
# No code

#--------------------------------------------------------------------------------------------------#

#%% 8. Using CSS Selectors

# Get the page content and set up a new parser
response = requests.get("http://dataquestio.github.io/web-scraping-pages/ids_and_classes.html")

parser = BeautifulSoup(response.content, 'html.parser')

# Select all of the elements that have the first-item class
first_items = parser.select(".first-item")

# Print the text of the first paragraph (the first element with the first-item class)
print(first_items[0].text)

# Get the text of the first outer paragraph
outer_items = parser.select(".outer-text")

first_outer_text = outer_items[0].text

second_text = parser.find_all(id="second")[0].text

#--------------------------------------------------------------------------------------------------#

#%% 9. Nesting CSS Selectors
# No code

#--------------------------------------------------------------------------------------------------#

#%% 10. Using Nested CSS Selectors

# Get the page content and set up a new parser
response = requests.get("http://dataquestio.github.io/web-scraping-pages/2014_super_bowl.html")

parser = BeautifulSoup(response.content, 'html.parser')

# Find the number of turnovers the Seahawks committed
seahawks_turnovers_count = parser.select("#turnovers")[0].select("td")[1].text
print(seahawks_turnovers_count)

# Find the total plays for the New England Patriots
patriots_total_plays_count = parser.select("#total-plays")[0].select("td")[2].text
print(patriots_total_plays_count)

# Find the total yards for the Seahawks
seahawks_total_yards_count = parser.select("#total-yards")[0].select("td")[1].text
print(seahawks_total_yards_count)

#--------------------------------------------------------------------------------------------------#

#%% 11. Beyond the Basics
# No code
