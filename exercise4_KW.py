###-------Exercise 4, KW-------###
# import numpy:
import numpy as np
from prettytable import PrettyTable

# define the function to read the precipitation file and return just the precip_data:
def datareader(data):
    column = np.loadtxt(data, usecols=[2], skiprows=1)   # usecols =[2] -> read a single column in file at
    return column                                        # position 2 (=precip)/skip the first row with skiprows=1


# ask the user for the path and file name. then define the full path to a variable, here: 'investfile'
askpath = input("Please type in the exact path to your file: ")
askname = input("What is the exact name of your file, ending with '.txt'? ")
investfile = askpath + '\\' + askname


# now the defined function from the beginning takes over:
precipitation = datareader(investfile)

maxprec = precipitation.max()
minprec = precipitation.min()
meanprec = round(precipitation.mean(), 1)

# print the results as a table
t = PrettyTable(['max precipitation', 'min precipitation', 'mean precipitation'])
t.add_row([maxprec, minprec, meanprec])
print(t)
