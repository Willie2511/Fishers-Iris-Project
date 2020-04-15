                                      FISHERS IRIS DATASET

Introduction and Background

This project will investigate and analyse the well-known Fishers Iris Data Set. This is a multivariate data set introduced by the British statistician and biologist Ronald Fisher in his paper 'The Use of Multiple Measurements in Taxonomic Problems'. The data was collected by Edgar Anderson to quantify the morphologic variation of iris flowers of three related species. The data set consists of 50 samples from three species of iris (setosa, virginica and versicolor). The length and width, in centimeters, of the sepals and petals for each sample were recorded. This project will import and analyse the data set using python, summarize the variables, and produce graphs and plots to add visual representation of results.

Literature Review

After studying many different articles, books and videos on Fishers data set analyses which presented numerous different approaches to analysing the data set, I concluded that a simplified exploratory data analysis would work best. While a study by Kozak and Lotocka (2013) raised the question: Do Iris flowers have sepals?, which makes the data less interesting for botanists, statisticians have successfully used the data set for years. Exploratory Data Analysis is the process of analysing data by using simple concepts from statistics and probability and presenting the results in easy-to-understand pictorial format (Nabria, 2019). The data would be analysed using Python, Pandas, Matplotlib, Pyplot and Seaborn libraries. Histograms and scatterplots would also be produced to help visualise data and aid comparative analysis. 

Plan

   The next step of the project was to lay out a plan of how the assesment criteria and objectives could most accuratly, and efficiently, be met. To complete this step an approach was taken which was attained from the Algorithm section of the Computer Architecture and Technology Convergence module of the course. This approach broke the development of an algorithm down into four parts. 1. Identify the inputs - what data is needed and where to get it. 2. Identify the processes - How to manipulate the data to produce meaningful results. 3. Identify the outputs - What outputs need to be returned and in what format. 4. Develop a HIPO (Hierarchy of inputs, processes and outputs) Chart - Break the project down into smaller parts, and what processes need to happen in each section.

   This project was broken down into four subsections which made it easier, and less intimidating, to tackle the iris dataset. The first part of the project entailed researching the methods which would be implemented, and importing the necessary libraries into the python file which would be used to achieve the desired results. The iris dataset was downloaded online as a .csv file. Once all necessary libraries were imported, the next step was to write up the first piece of code which would produce desired results when run on the terminal, and would meet the assesment criteria. Dissecting the dataset, acquiring descriptions, calculating averages and standard deviations, and to group the data into classes were all carried out in this section of the project using concise code. All code will be discussed in greater detail in the section below. 

    The third section of this project was to produce a histogram and scatter plot of each pair of variables, and to export these graphs as .png files. As part of this section of the project, research was conducted into how to export a decription of each variable into a .txt file when the program was run. This took some time to achieve in the most accurate, and concise, code possible. Both steps in section three of the project required relatively simple code, but produced accurate desired results. 

   The Final step of the project was to investigate some interesting approaches and results from other studies on the dataset, which would require learning how to use new libraries and developing new code. Although this section was not necessitated, it was encouraged as it would broaden Python knowledge. This project would use testing analyses to check if flower type could be predicted based on sepal and petal lenght and width data. A lot of research was conducted on this area as it was a new area of study. Many previous studies on the data set are used as an introduction to machine learning, therefore new libraries and code needed to be investigated. 

Code

The code starts by importing all essential libraries which would be used throughout the project. Numpy imported as np, matplotlib.pyplot as plt, sys imported, pandas imported and from pandas both read_csv and scatter_matrix are both imported. NumPy is the fundamental package for scientific computing with Python. It is a general-purpose array-processing package. Matplotlib.pyplot is a state-based interface to matplotlib. pyplot is mainly intended for interactive plots and simple cases of programmatic plot generation (Hunter et al, 2020). Pandas is a fast, powerful, flexible and easy to use open source data analysis and manipulation tool, built on top of the Python programming language (McKinney, 2020). The dataset was imported as a .csv file, which are a common file format for transferring and storing data. The basic process of loading/importing data from a csv file into a pandas data frame is with the use of the "read_csv" function in pandas (Lynn,2020), which can be seen in the first few lines of code.















                                               References

Anderson, Edgar. “The Species Problem in Iris.” Annals of the Missouri Botanical Garden, vol. 23, no. 3, 1936, pp. 457–509. JSTOR, www.jstor.org/stable/2394164. Accessed on: 27-03-2020.

Hunter, J., Dale, D., Firing, E., Droettboom, M. (2020) 'Matplotlib.pyplot' Matplotlib.org. Available at: https://matplotlib.org/3.1.1/api/_as_gen/matplotlib.pyplot.html Accessed on: 30-03-2020.

Kozak, M., Lotocka, B. (2013) 'What should we know about the famous Iris data?' CURRENT SCIENCE, VOL. 104, NO. 5. Available at: https://www.researchgate.net/profile/Marcin_Kozak/publication/237010807_What_should_we_know_about_the_famous_Iris_data/links/02e7e51be9229f3495000000.pdf Accessed on: 30-03-2020.

Lynn, S. (2020) "Python Pandas read_csv – Load Data from CSV Files" Panda Tutorials. Available at: https://www.shanelynn.ie/python-pandas-read_csv-load-data-from-csv-files/ Accessed on: 30-03-2020.

McKinney, W. (2020) 'pandas: powerful Python data analysis toolkit' Pandas.pydata.org Available at: https://pandas.pydata.org/docs/pandas.pdf Accessed on: 30-03-2020.

Nabriya, P. (2019) "Exploratory Data Analysis: Uni-variate analysis of Iris Data set" Medium. Available at: https://medium.com/analytics-vidhya/exploratory-data-analysis-uni-variate-analysis-of-iris-data-set-690c87a5cd40 Accessed on: 27-03-2020.
