#**************************************************************************************************#
#                                                                                                  #
# 01_Best_practices_for_writing_functions                                                          #
#                                                                                                  #
# Authors: S.G.M. Neves                                                                            #
#                                                                                                  #
#**************************************************************************************************#

#%% 1. Introducing Docstrings
import numpy as np
import pandas as pd

def split_and_stack(df, new_names):
    """Splits a DataFrame's columns into two halves and then stack
    them vertically, returning a new DataFrame with `new_names` as the
    column names.

    Args:
      df (DataFrame): The DataFrame to split.
      new_names (iterable of str): The column names for the new DataFrame.

    Returns:
      DataFrame
    """

    half = int(len(df.columns) / 2)
    left = df.iloc[:, :half]
    right = df.iloc[:, half:]

    return pd.DataFrame(data=np.vstack([left.values, right.values]), columns=new_names)

#--------------------------------------------------------------------------------------------------#

#%% 2. Retrieving Docstrings
import inspect

raw_docstring = split_and_stack.__doc__

formatted_docstring = inspect.getdoc(split_and_stack)

#--------------------------------------------------------------------------------------------------#

#%% 3. Google Style Docstrings
def count_letter(content, letter):
    """Counts the number of times `letter` appears in `content`.

    Args:
      content (str): The string to search.
      letter (str): The letter to search for.

    Returns:
      int: Number of times `letter` appears in `content`
    """

    if (not isinstance(letter, str)) or len(letter) != 1:
        raise ValueError('`letter` must be a single character string.')

    return len([char for char in content if char == letter])

formatted_docstring = inspect.getdoc(count_letter)

#--------------------------------------------------------------------------------------------------#

#%% 4. Google Style Docstrings Continued
def count_letter(content, letter):
    """Counts the number of times `letter` appears in `content`.

    Args:
      content (str): The string to search.
      letter (str): The letter to search for.

    Returns:
      int: Number of times `letter` appears in `content`

    Raises:
      ValueError: If `letter` is not a one-character string.
    """

    if (not isinstance(letter, str)) or len(letter) != 1:
        raise ValueError('`letter` must be a single character string.')

    return len([char for char in content if char == letter])

formatted_docstring = inspect.getdoc(count_letter)
print(formatted_docstring)

#--------------------------------------------------------------------------------------------------#

#%% 5. Don't Repeat Yourself
def standardize(df, col):
    """Returns the z-scores of a column.

    Args:
      df (DataFrame): DataFrame with the data.
      col (str): Name of the column to calculate the z-scores.

    Returns:
      float: z-scores of the column.
    """

    return (df[col] - df[col].mean()) / df[col].std()


df['y1_z'] = standardize(df, 'y1_gpa')
df['y2_z'] = standardize(df, 'y2_gpa')
df['y3_z'] = standardize(df, 'y3_gpa')
df['y4_z'] = standardize(df, 'y4_gpa')

#--------------------------------------------------------------------------------------------------#

#%% 6. Do One Thing
def mean(values):
    """Gets the mean of a list of `values`

    Args:
      values (iterable of float): A list of numbers

    Returns:
      float: The mean
    """
    mean = sum(values) / len(values)

    return mean

def median(values):
    """Gets the median of a list of `values`

    Args:
      values (iterable of float): A list of numbers

    Returns:
      float: The median
    """

    midpoint = int(len(values) / 2)

    if len(values) % 2 == 0:
        median = (values[midpoint - 1] + values[midpoint]) / 2
    else:
        median = values[midpoint]

    return median

list_mean = mean([1,2,3])

list_median = median([1,2,3,4])

#--------------------------------------------------------------------------------------------------#

#%% 7. Pass by Assignment
a = [1, 2, 3]
b = a

a.append(4)
print(b)

b.append(5)
print(a)

a = 42
print(a)
print(b)

#--------------------------------------------------------------------------------------------------#

#%% 8. Pass by Assignment Continued
# No code

#--------------------------------------------------------------------------------------------------#

#%% 9. Mutable and Immutable Variables
def foo(var=[]):
    var.append(1)
    return var

print(foo())
print(foo())

#--------------------------------------------------------------------------------------------------#

#%% 10. Mutable and Immutable Variables Continued
import pandas

def add_column(values, df=None):
    """Adds a column of `values` to a DataFrame `df`.
    The column will be named "col_<n>" where "n" is
    the numerical index of the column.

    Args:
        values (iterable): The values of the new column
        df (DataFrame, optional): The DataFrame to update.
          If no DataFrame is passed, one is created by default.

    Returns:
        DataFrame
    """

    if df is None:
        df=pandas.DataFrame()

    df['col_{}'.format(len(df.columns))] = values
    return df

df_1 = add_column(range(10))

df_2 = add_column(range(10))
