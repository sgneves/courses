#**************************************************************************************************#
#                                                                                                  #
# get_titles                                                                                       #
# Gets the titles of programming exercises from the specified text file.                           #
#                                                                                                  #
# Authors: S.G.M. Neves                                                                            #
#                                                                                                  #
#**************************************************************************************************#

import re
import sys

def main():

    # Get the filename
    if len(sys.argv) != 2:

        print('usage: get_titles file')
        sys.exit(1)

    filename = sys.argv[1]

    # Read the file with the titles
    with open(filename) as file:

        string = file.read()

    lines = string.splitlines()

    # Extract the titles
    lines = [line for line in lines if ('Lab:' in line) or ('Programming Assignment:' in line)]

    lines = [re.sub(r'^.*?:', '', line) for line in lines]

    lines = [line.strip().replace(' ', '_').capitalize() for line in lines]

    # Write the titles to file
    with open(filename, 'w') as file:

       file.write("\n".join(lines))

if __name__ == '__main__':
    main()
