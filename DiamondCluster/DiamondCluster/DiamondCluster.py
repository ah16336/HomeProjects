import seaborn as sns
import numpy as np
import pandas as pd
from matplotlib import pyplot as plt

df = sns.load_dataset("diamonds")


high_I = df[(df.cut == 'Premium') & (df.color == 'I')]
high = df[(df.cut == 'Premium')]
color = df[(df.color == 'I')]
print(high.head())

carat = high_I.carat
price = high_I.price

plt.scatter(carat, price)
plt.show()

sns.set(style="ticks")

sns.lmplot('carat', 'price', high_I, lowess=True)
plt.show()

x = high_I.x

plt.scatter(x, price)
plt.show()

sns.lmplot('x', 'price', high_I, order=2)
plt.show()