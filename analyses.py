# Willie Byrne
# Analyses of Fisher's Iris Data set
# First section will import, analyse and produce graphs
# to visually represent the data.
# Second section will interpret the data from resulting graphs 
# and tables, in order to draw some definitive conclusions


# Import all libraries which will be needed to analyses the dataset

import sys
import scipy
import numpy as np 
import matplotlib 
import pandas
import sklearn
from pandas import read_csv
from matplotlib import pyplot
from pandas.plotting import scatter_matrix


# First we Load dataset and use the 'read_csv' function from pandas library to 
# enable us to use a .csv file. 
# Names are given for each variable which is included in the dataset, which will
# be used to differentiate the different flowers.

url = "https://raw.githubusercontent.com/jbrownlee/Datasets/master/iris.csv"
names = ['sepal-length', 'sepal-width', 'petal-length', 'petal-width', 'class']
dataset = read_csv(url, names=names)


# Print the shape of the data by using the 'dataset.shape' function.
# Returns tuple of shape of dataset.

print (dataset.shape)

# Head
# Head function is used to return the top specified number of rows of 
# a dataset. In this case, 'dataset.head(20)' will print the top 20 rows
# in the iris dataset

print (dataset.head(20))



# Descriptions
# The '.describe ()' function generates descriptive statistics,
# which include a summary of the central tendency, dispersion and the 
# shape dataset's distribution.
# Class Distribution
# The code below also goups the dataset by class and size. 
# The output of the '.describe()' and '.groupby' functions will be exported to a .txt file
# called 'Flowers_summary.txt'
# This is done using the 'with open as f:' command to ensure the code is as short and 
# concise as possible. Both outputs are exported to the file 'Flowers_summary.txt' when the 
# program is run.

with open ('Flowers_summary.txt', 'w') as f:
    print(dataset.describe(), file=f)
    print (dataset.groupby('class').size(), file=f)
f.close()

print('********************************************')


# The ('.describe(include='all')) function is similar to the .describe function but includes
# a couple of extra pieces of information.
# This info will be printed to the command line/terminal
# while the .describe info will be exported to the .txt file. 

print (dataset.describe(include='all'))



# Visualisation
#Histograms

dataset.hist()
pyplot.savefig('Histogram.png')

# Scatter Plot Matrix
scatter_matrix(dataset)
pyplot.savefig('ScatterPlot.png')
#Note the diagonal grouping of some pairs of attributes. 
#This suggests a high correlation and a predictable relationship.









