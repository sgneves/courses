#**************************************************************************************************#
#                                                                                                  #
# 01_Introduction_to_Spark                                                                         #
#                                                                                                  #
# Authors: S.G.M. Neves                                                                            #
#                                                                                                  #
#**************************************************************************************************#

#%% 1. A Brief History of Big Data
# No code

#--------------------------------------------------------------------------------------------------#

#%% 2. The Spark Revolution
# No code

#--------------------------------------------------------------------------------------------------#

#%% 3. Resilient Distributed Data Sets (RDDs)
raw_data = sc.textFile("daily_show.tsv")
raw_data.take(5)

#--------------------------------------------------------------------------------------------------#

#%% 4. SparkContext
# No code

#--------------------------------------------------------------------------------------------------#

#%% 5. Lazy Evaluation
# No code

#--------------------------------------------------------------------------------------------------#

#%% 6. Pipelines
daily_show = raw_data.map(lambda line: line.split('\t'))
daily_show.take(5)

#--------------------------------------------------------------------------------------------------#

#%% 7. Python and Scala, Friends Forever
# No code

#--------------------------------------------------------------------------------------------------#

#%% 8. ReduceByKey()
tally = daily_show.map(lambda x: (x[0], 1)).reduceByKey(lambda x,y: x+y)
print(tally)

#--------------------------------------------------------------------------------------------------#

#%% 9. Explanation
tally.take(tally.count())

#--------------------------------------------------------------------------------------------------#

#%% 10. Filter
def filter_year(line):

    if line[0] == 'YEAR':
        return False
    else:
        return True

filtered_daily_show = daily_show.filter(lambda line: filter_year(line))

#--------------------------------------------------------------------------------------------------#

#%% 11. Practice with Pipelines
filtered_daily_show.filter(lambda line: line[1] != '') \
                   .map(lambda line: (line[1].lower(), 1)) \
                   .reduceByKey(lambda x,y: x+y) \
                   .take(5)
