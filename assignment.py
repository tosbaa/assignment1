import pandas as pd
import numpy as np
import random
from scipy.stats import norm
import matplotlib.pyplot as plt
from scipy.stats.kde import gaussian_kde

data = pd.read_csv("./bank.csv", sep=r';', header=0)

##2 Calculate mean, standart deviation, mode and skewness

# data_numerical = data.select_dtypes(include=np.number)
# for header in list(data_numerical.columns):
#     column = data_numerical[header]
#     print("name" + " = " + str(header))
#     print("mean" + " = " + str(column.mean()))
#     print("std" + " = " + str(column.std()))
#     print("mode" + " = " + str(column.mode()))
#     print("skew" + " = " + str(column.skew()))
#     print("---------------")

## End of 2

##3 Find the mod of the categorical values

# data_categorical = data.select_dtypes(exclude=np.number)
# for header in list(data_categorical):
#     print("name = " + header)
#     print("mode = " + data_categorical[header].mode())


## End of 3

## 4 Plot the Probability density function for variables and histogram for categorical

## PDF For Numerical

# data_numerical = data.select_dtypes(include=np.number)
# data_age = data_numerical["previous"]
# dist = norm(data_age.mean(), data_age.std())
# data_age = list(data_age.sort_values())

# sample = np.arange(min(data_age), max(data_age), 0.5)
# print(sample)

# probabilities = [dist.pdf(value) for value in sample]

# plt.plot(sample, probabilities)
# plt.show()

## Histogram for Categorical

# data_categorical = data.select_dtypes(exclude=np.number)

# plt.xticks(rotation=90)

# plt.hist(data_categorical["y"])
# plt.show()

## End of 4


## 5 
