                                      FISHERS IRIS DATASET

             Introduction and Background

This project will investigate and analyse the well-known Fishers Iris Data Set. This is a multivariate data set introduced by the British statistician and biologist Ronald Fisher in his paper 'The Use of Multiple Measurements in Taxonomic Problems'. The data was collected by Edgar Anderson to quantify the morphologic variation of iris flowers of three related species. The data set consists of 50 samples from three species of iris (setosa, virginica and versicolor). The length and width, in centimeters, of the sepals and petals for each sample were recorded. This project will import and analyse the data set using python, summarize the variables, and produce graphs and plots to add visual representation of results.

             Literature Review

After studying many different articles, books and videos on Fishers data set analyses which presented numerous different approaches to analysing the data set, I concluded that a simplified exploratory data analysis would work best. While a study by Kozak and Lotocka (2013) raised the question: Do Iris flowers have sepals?, which makes the data less interesting for botanists, statisticians have successfully used the data set for years. Exploratory Data Analysis is the process of analysing data by using simple concepts from statistics and probability and presenting the results in easy-to-understand pictorial format (Nabria, 2019). The data would be analysed using Python, Pandas, Matplotlib, Pyplot and Seaborn libraries. Histograms and scatterplots would also be produced to help visualise data and aid comparative analysis. 

             Plan

   The next step of the project was to lay out a plan of how the assesment criteria and objectives could most accuratly, and efficiently, be met. To complete this step an approach was taken which was attained from the Algorithm section of the Computer Architecture and Technology Convergence module of the course. This approach broke the development of an algorithm down into four parts. 1. Identify the inputs - what data is needed and where to get it. 2. Identify the processes - How to manipulate the data to produce meaningful results. 3. Identify the outputs - What outputs need to be returned and in what format. 4. Develop a HIPO (Hierarchy of inputs, processes and outputs) Chart - Break the project down into smaller parts, and what processes need to happen in each section.

   This project was broken down into four subsections which made it easier, and less intimidating, to tackle the iris dataset. The first part of the project entailed researching the methods which would be implemented, and importing the necessary libraries into the python file which would be used to achieve the desired results. The iris dataset was downloaded online as a .csv file. Once all necessary libraries were imported, the next section focused on writing up the first piece of code which would produce desired results when run on the terminal, and would meet the assesment criteria. Dissecting the dataset, acquiring descriptions, calculating averages and standard deviations, and to group the data into classes were all carried out in this section of the project using concise code. All code will be discussed in greater detail in the section below. 

  The third section of this project was to produce a histogram and scatter plot of each pair of variables, and to export the histogram as .png files. As part of this section of the project, research was conducted into how to export a decription of each variable into a .txt file when the program was run. This took some time to achieve in the most accurate, and concise, code possible. Both steps in section three of the project required relatively simple code, but produced accurate desired results. 

   The Final step of the project was to investigate some interesting approaches and results from other studies on the dataset, which would require learning how to use new libraries and developing new code. Although this section was not necessitated, it was encouraged as it would broaden Python knowledge. The majority of research conducted on this dataset used different types of visual representation in the conclusion section of the respective studies. This opened up the potential to explore new graphs and libraries which may be beneficial in effectively displaying results in future research. A violin plot was selected for this project as it would most accurately portray a real petal or sepal, from the dataset. A violin plot was produced for the sepal width and length, and petal width and length, of all three species. A pairplot was also produced with a KDE (Kernel Density Estimate) plot which depicts the probability density at different values in a continuous variable. We can also plot a single graph for multiple samples which helps in more efficient data visualization (Prateek,2019).     

          Code

The code starts by importing all essential libraries which would be used throughout the project. Numpy imported as np, matplotlib.pyplot as plt, sys imported, pandas imported and from pandas both read_csv and scatter_matrix are both imported. NumPy is the fundamental package for scientific computing with Python. It is a general-purpose array-processing package. Matplotlib.pyplot is a state-based interface to matplotlib. Pyplot is mainly intended for interactive plots and simple cases of programmatic plot generation (Hunter et al, 2020). Pandas is a fast, powerful, flexible and easy to use open source data analysis and manipulation tool, built on top of the Python programming language (McKinney, 2020). train_test_split is a method for splitting the dataset while KNeighborsClassifier is used for classifying using the K-Nearest Neighbor approach (Trindade, 2019). 

The first lines of code written after all neccessary libraries were imported involved importing the dataset dataset as a .csv file, which are a common file format for transferring and storing data. The basic process of loading/importing data from a csv file into a pandas data frame is with the use of the "read_csv" function in pandas (Lynn,2020), which can be seen in the first few lines of code. The dataset and names are given the variable name 'dataset' to be used throughout the project. The program then moves onto printing out some basic information by analysing the dataset. The shape is printed using the 'print(dataset.shape)' function, '(dataset.head(20))' is used to print out information on the first 20 variables, and descriptions of the data are printed using the '(dataset.describe())' function. In order to meet the project brief this program needed to export a description of the variables into a .txt file when it was run. In order to do this, I included the code 'file=open("Flowers_summary.txt", 'w')' after the initial describe function. This takes the output of the function and redirects it to a text file called 'Flowers_summary.txt' which is opened. This code is included after a select number of instructions. 

Once the data analyses was complete, using concise and accurate code, it was time to visually represent the data on graphs. First up was the task of simply creating a histogram. The histogram was created using the 'dataset.hist()' command, before using pyplot to save the resulting graph as a .png file. This was completed using the 'pyplot.savefig' command. The next task was to produce a scatter plot for each pair of variables. This scatterplot required the use of a previously unfamiliar library, scatter_matrix which was imported form pandas.plotting. The code was relatively simple, after some research, and the scatter plot was created and saved with two lines of code. The first line was simply 'scatter_matrix(dataset)', while the second line used 'pyplot.savefig("ScatterPlot.png")' to save the resulting plot as a .png file. 

This concluded all the necessary code which was needed to accurately produce and meet the assessment criteria set out in the project brief, however through further research I decided to dig a little deeper into the data and learn new Python libraries for data analyses.

















                                               References

Anderson, Edgar. “The Species Problem in Iris.” Annals of the Missouri Botanical Garden, vol. 23, no. 3, 1936, pp. 457–509. JSTOR, www.jstor.org/stable/2394164. Accessed on: 27-03-2020.

Hunter, J., Dale, D., Firing, E., Droettboom, M. (2020) 'Matplotlib.pyplot' Matplotlib.org. Available at: https://matplotlib.org/3.1.1/api/_as_gen/matplotlib.pyplot.html Accessed on: 30-03-2020.

Kozak, M., Lotocka, B. (2013) 'What should we know about the famous Iris data?' CURRENT SCIENCE, VOL. 104, NO. 5. Available at: https://www.researchgate.net/profile/Marcin_Kozak/publication/237010807_What_should_we_know_about_the_famous_Iris_data/links/02e7e51be9229f3495000000.pdf Accessed on: 30-03-2020.

Lynn, S. (2020) "Python Pandas read_csv – Load Data from CSV Files" Panda Tutorials. Available at: https://www.shanelynn.ie/python-pandas-read_csv-load-data-from-csv-files/ Accessed on: 30-03-2020.

McKinney, W. (2020) 'pandas: powerful Python data analysis toolkit' Pandas.pydata.org Available at: https://pandas.pydata.org/docs/pandas.pdf Accessed on: 30-03-2020.

Nabriya, P. (2019) "Exploratory Data Analysis: Uni-variate analysis of Iris Data set" Medium. Available at: https://medium.com/analytics-vidhya/exploratory-data-analysis-uni-variate-analysis-of-iris-data-set-690c87a5cd40 Accessed on: 27-03-2020.

Prateek, S. (2019) "KDE Plot Visualization with Pandas and Seaborn" Geeks For Geeks. Available at: https://www.geeksforgeeks.org/kde-plot-visualization-with-pandas-and-seaborn/ Accessed on: 22-04-2020.

Trindade, F. (2019) "Start to learn Machine Learning with the Iris flower classification challenge" Medium. Available at: https://medium.com/gft-engineering/start-to-learn-machine-learning-with-the-iris-flower-classification-challenge-4859a920e5e3 Accessed on: 14/04/2020.
