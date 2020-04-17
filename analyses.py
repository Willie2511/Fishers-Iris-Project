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
# The output of the '.describe()' function will be exported to a .txt file
# called 'Flowers_summary.txt'


print(dataset.describe(), file=open("Flowers_summary.txt", 'w'))

# Class Distribution
# The code below goups the dataset by class and size.
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










#######################################################################################
#          This section is an attempt at learning predicting and testing              #
#######################################################################################

# Experimental 
import pandas
import matplotlib.pyplot as plt
from sklearn import model_selection
from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix
from sklearn.metrics import accuracy_score
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
from sklearn.naive_bayes import GaussianNB
from sklearn.svm import SVC



array = dataset.values
X = array[: ,0:4]
Y = array[: ,4]
validation_size = 0.20
seed = 7
X_train, X_validation, Y_train, Y_validation= model_selection.train_test_split(X, Y, test_size=validation_size, random_state=seed)

seed = 7
scoring = 'accuracy'



models = []
models.append(('LR', LogisticRegression()))
models.append(('LDA', LinearDiscriminantAnalysis()))
models.append(('KNN', KNeighborsClassifier()))
models.append(('CART', DecisionTreeClassifier()))
models.append(('NB', GaussianNB()))
models.append(('SVM', SVC()))
# evaluate each model in turn
results = []
names = []
for name, model in models:
 kfold = model_selection.KFold(n_splits=10, random_state=seed)
 cv_results = model_selection.cross_val_score(model, X_train, Y_train, cv=kfold, scoring=scoring)
 results.append(cv_results)
 names.append(name)
 msg = "%s: %f (%f)" % (name, cv_results.mean(), cv_results.std())
 print(msg)


 # Make predictions on validation dataset
knn = KNeighborsClassifier()
knn.fit(X_train, Y_train)
predictions = knn.predict(X_validation)
print(accuracy_score(Y_validation, predictions))
print(confusion_matrix(Y_validation, predictions))
print(classification_report(Y_validation, predictions))




#####################################################################
#####################################################################
