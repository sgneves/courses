#**************************************************************************************************#
#                                                                                                  #
# 04_Transforming_Hamlet_into_a_data_set                                                           #
#                                                                                                  #
# Authors: S.G.M. Neves                                                                            #
#                                                                                                  #
#**************************************************************************************************#

#%% 1. Introduction
# No code

#--------------------------------------------------------------------------------------------------#

#%% 2. Extract Line Numbers
import findspark
findspark.init()

import pyspark

sc = pyspark.SparkContext()

raw_hamlet = sc.textFile("hamlet.txt")

split_hamlet = raw_hamlet.map(lambda line: line.split('\t'))

split_hamlet.take(10)

def clean_ids(line):

    line[0] = line[0].replace('hamlet@', '')

    return line

hamlet_with_ids = split_hamlet.map(clean_ids)

hamlet_with_ids.take(10)

#--------------------------------------------------------------------------------------------------#

#%% 3. Remove Blank Values
hamlet_with_ids.take(10)

hamlet_text_only = (hamlet_with_ids
                    .map(lambda line: [i for i in line if i != ''])
                    .filter(lambda line: len(line) > 1))

hamlet_text_only.take(10)

#--------------------------------------------------------------------------------------------------#

#%% 4. Remove Pipe Characters
hamlet_text_only.take(10)

clean_hamlet = (hamlet_text_only
                .map(lambda line: [i for i in line if i != '|'])
                .map(lambda line: [i.replace('|', '') for i in line]))

clean_hamlet.take(10)
