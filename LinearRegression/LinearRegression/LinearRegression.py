import matplotlib.pyplot as plt
import numpy as np
from scipy import stats
import seaborn as sns
import statsmodels.api as sm
from sklearn import linear_model

iris = sns.load_dataset('iris')

# finding relationship between two variables

x = iris[['petal_length']]
y = iris[['petal_width']]

model = sm.OLS(y, x) # OLS estimates the unknown parameters in a linear regression model
results = model.fit()

print(results.summary())

print("\n")

# finding line equation between two variables

x = iris['petal_length']
x = np.vander(x, 2) # update x with this as we want to find the line equation, 2 is the number of variables
y = iris['petal_width']

model = sm.OLS(y, x) 
results = model.fit()

print(results.summary()) # x1 and const give the line equation

# this summary tells us the relationship between petal_length and petal_width
# P must be lower than 0.005 to be statistically significant (has to be true if we want to find the line equation)
# it gives the coefficient for each variable that we have included
# petal_width = petal_length * 0.4158 - 0.3631

print("\n")

#  Finding relationship between more than 2 variables (multiple linear regression)

x = iris[['petal_length', 'sepal_length']]
x = sm.add_constant(x) # Add a column of ones to an array (x).
y = iris['petal_width']

model = sm.OLS(y, x)
results = model.fit()

print(results.summary()) 

# this summary tells us the relationship between petal_length and petal_width and sepal_length
# petal_width = -0.009 + petal_length * 0.449 - sepal_length * 0.0822
# but p value is too big so....