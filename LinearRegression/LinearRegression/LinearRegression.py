import matplotlib.pyplot as plt
import numpy as np
from scipy import stats
import seaborn as sns
import statsmodels.api as sm
from sklearn import linear_model
plt.style.use('seaborn-whitegrid')

iris = sns.load_dataset('iris')

# finding relationship between two variables
# Statistical regression is a way to predict unknown quantities from a batch of existing data.
# OLS finds a relationship s.t. the sum of differences squared between data points and trend line is as small as possible

x = iris[['petal_length']]
y = iris[['petal_width']]

model = sm.OLS(y, x) # OLS estimates the unknown parameters in a linear regression model
results = model.fit()

print(results.summary())

print("\n")

# finding line equation between two variables

x = iris['petal_length']
x = np.vander(x, 2) # generates a vandermonde matrix with 2 columns, x must be a 1D array (this type of matrix has rows of the form (1, a, a^2, ..., a^n-1))
y = iris['petal_width']

model = sm.OLS(y, x) 
results = model.fit()

print(results.summary()) # x1 and const give the line equation

# this summary tells us the relationship between petal_length and petal_width
# P must be lower than 0.005 to be statistically significant (has to be true if we want to find the line equation)
# it gives the coefficient for each variable that we have included
# petal_width = petal_length * 0.4158 - 0.3631

print('Parameters: ', results.params) # gives an easier way to see equation coefficients

#displaying results

#fig = plt.figure()
#ax = plt.axes()
plt.plot(x, x*0.4158 - 0.3631, linestyle='dashed', color='PaleVioletRed', label='OLS Prediction')
plt.scatter(iris['petal_length'], iris['petal_width'], color='MediumAquaMarine', label='Actual Data')
plt.xlabel("Petal Length")
plt.ylabel("Petal Width")
plt.title("Petal Dimension Chart")
plt.legend()
plt.show()

print("\n")

# Finding relationship between more than 2 variables (multiple linear regression)
# Rather than finding a line of best fit, it finds a plane

x = iris[['petal_length', 'sepal_length']]
x = sm.add_constant(x) # Add a column of ones to an array (x).
y = iris['petal_width']

model = sm.OLS(y, x)
results = model.fit()

print(results.summary()) 

# this summary tells us the relationship between petal_length and petal_width and sepal_length
# petal_width = -0.009 + petal_length * 0.449 - sepal_length * 0.0822
# but p value is too big so....