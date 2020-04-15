# Willie Byrne

import sys
import scipy
import numpy as np 
import matplotlib 
import pandas
import sklearn
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from pandas import read_csv
from matplotlib import pyplot


# load libraries
from pandas import read_csv
from pandas.plotting import scatter_matrix
from pandas.api.types import is_numeric_dtype 
from matplotlib import pyplot
from sklearn.model_selection import train_test_split
from sklearn.model_selection import cross_val_score
from sklearn.model_selection import StratifiedKFold
from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix
from sklearn.metrics import accuracy_score
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
from sklearn.naive_bayes import GaussianNB
from sklearn.svm import SVC 

# Load dataset
url = "https://raw.githubusercontent.com/jbrownlee/Datasets/master/iris.csv"
names = ['sepal-length', 'sepal-width', 'petal-length', 'petal-width', 'class']
dataset = read_csv(url, names=names)


# Shape
print (dataset.shape)

#Calculating average, standard deviation, minimum and maximum values
#for col in names:
 #   if is_numeric_dtype(dataset[col]):
  #      print('%s:' % (col), file=open("Flowers_summary.txt", 'w'))
   #     print('\t Mean = %.2f' % dataset[col].mean(), file=open("Flowers_summary.txt", 'w'))
    #    print('\t Standard deviation = %.2f' % dataset[col].mean(), file=open("Flowers_summary.txt", 'w'))
     #   print('\t Minimum = %.2f' % dataset[col].min(), file=open("Flowers_summary.txt", 'w'))
      #  print('\t Maximum = %.2f' % dataset[col].max(), file=open("Flowers_summary.txt", 'w'))


# Head
print (dataset.head(20))

# Descriptions
print(dataset.describe(), file=open("Flowers_summary.txt", 'w'))

# Class Distribution
print (dataset.groupby('class').size())

print (dataset.describe(include='all'), file=open("Flowers_summary.txt", 'w'))


# Visualisation
#Histograms

dataset.hist()
pyplot.savefig('Histogram.png')

# Scatter Plot Matrix
scatter_matrix(dataset)
pyplot.savefig('ScatterPlot.png')
#Note the diagonal grouping of some pairs of attributes. 
#This suggests a high correlation and a predictable relationship.










