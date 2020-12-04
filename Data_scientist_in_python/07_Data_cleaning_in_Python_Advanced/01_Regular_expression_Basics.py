#**************************************************************************************************#
#                                                                                                  #
# 01_Regular_expression_Basics                                                                     #
#                                                                                                  #
# Authors: S.G.M. Neves                                                                            #
#                                                                                                  #
#**************************************************************************************************#

# 1. Introduction
import pandas as pd

hn = pd.read_csv('hacker_news.csv')

#--------------------------------------------------------------------------------------------------#

# 2. The Regular Expression Module
import re

pattern = "[Pp]ython"
python_mentions = 0

for title in hn["title"].tolist():

    if re.search(pattern, title):
        python_mentions += 1

#--------------------------------------------------------------------------------------------------#

# 3. Counting Matches with pandas Methods
titles = hn["title"]

python_mentions = titles.str.contains(pattern).sum()

#--------------------------------------------------------------------------------------------------#

# 4. Using Regular Expressions to Select Data
ruby_titles = titles[titles.str.contains("[Rr]uby")]

#--------------------------------------------------------------------------------------------------#

# 5. Quantifiers
email_bool  = titles.str.contains("e-?mail")

email_count = email_bool.sum()

email_titles = titles[email_bool]

#--------------------------------------------------------------------------------------------------#

# 6. Character Classes
tag_titles = titles[titles.str.contains("\[[\w]+\]")]

tag_count = tag_titles.shape[0]

#--------------------------------------------------------------------------------------------------#

# 7. Accessing the Matching Text with Capture Groups
tag_freq = titles.str.extract(r"\[([\w]+)\]").value_counts()

#--------------------------------------------------------------------------------------------------#

# 8. Negative Character Classes
def first_10_matches(pattern):
    """
    Return the first 10 story titles that match
    the provided regular expression
    """
    all_matches = titles[titles.str.contains(pattern)]
    first_10 = all_matches.head(10)
    return first_10

java_titles = titles[titles.str.contains(r"[Jj]ava[^Ss]")]

#--------------------------------------------------------------------------------------------------#

# 9. Word Boundaries
java_titles = titles[titles.str.contains(r"\b[Jj]ava\b")]

#--------------------------------------------------------------------------------------------------#

# 10. Matching at the Start and End of Strings
beginning_count = titles.str.contains(r"^\[[\w]+\]").sum()

ending_count = titles.str.contains(r"\[[\w]+\]$").sum()

#--------------------------------------------------------------------------------------------------#

# 11. Challenge: Using Flags to Modify Regex Patterns
email_mentions = titles.str.contains(r"\be[\-\s]?mails?\b", flags=re.I).sum()
