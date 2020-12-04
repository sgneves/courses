#**************************************************************************************************#
#                                                                                                  #
# 02_Context_managers                                                                              #
#                                                                                                  #
# Authors: S.G.M. Neves                                                                            #
#                                                                                                  #
#**************************************************************************************************#

#%% 1. Introduction
# No code

#--------------------------------------------------------------------------------------------------#

#%% 2. Using Context Managers
with open('my_file.txt') as my_file:

    text = my_file.read()

print(text)

#--------------------------------------------------------------------------------------------------#

#%% 3. Using Context Managers Continued
n = 0

with open('alice.txt') as file:

    text = file.read()

for word in text.split():
    if word.lower() in ['cat', 'cats']:
        n += 1

print('Lewis Caroll uses the word "cat" {} times'.format(n))

#--------------------------------------------------------------------------------------------------#

#%% 4. Writing Context Managers
import contextlib
import time

@contextlib.contextmanager
def timer():
    """Time the execution of a context block.

    Yields:
      None
    """
    start = time.time()

    yield

    end = time.time()

    print('Elapsed: {:.2f}s'.format(end - start))

with timer():

    print('This should take approximately 0.25 seconds')
    time.sleep(0.25)

#--------------------------------------------------------------------------------------------------#

#%% 5. Writing Context Managers Continued
@contextlib.contextmanager
def open_read_only(filename):
    'Open filename for reading and return a corresponding file object.'

    read_only_file = open(filename)

    yield read_only_file

    read_only_file.close()

with open_read_only('my_file.txt') as my_file :

    text = my_file.read()

print(text)

#--------------------------------------------------------------------------------------------------#

#%% 6. Nested Contexts
with stock('NVDA') as nvda:

    with open('NVDA.txt', 'w') as f_out:

      for _ in range(10):

          value = nvda.price()
          print('Logging ${:.2f} for NVDA'.format(value))
          f_out.write('{:.2f}\n'.format(value))

#--------------------------------------------------------------------------------------------------#

#%% 7. Handling Errors
# No code

#--------------------------------------------------------------------------------------------------#

#%% 8. When to Create Context Managers
answer = 2
