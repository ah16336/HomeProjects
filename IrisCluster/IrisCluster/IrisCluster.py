import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
import seaborn as sns

df = sns.load_dataset('iris')

sns.lmplot('petal_length', 'petal_width', df, hue='species')
plt.title("Petal width and petal length of plants, grouped by species")
plt.show()

# CLUSTERING PETALS TO PREDICT SPECIES #

np.random.seed(7)
k = 3 # Number of Clusters
# centroids[i] = [x, y]
centroids = { # We are defining in a dictionary our 3 initial centre points
    i+1: [np.random.randint(0, 8), np.random.randint(0, 3)]
    for i in range(k)
}

colmap = {1: 'r', 2: 'g', 3: 'b'} # The colours we want for each centre point defined as a dictionary

def assignment(df, centroids): # function with database and centre points as arguments; calculates distance between points and centre points and finds closest centre for each point
    for i in centroids.keys(): # loops through each centre
        # sqrt((x1 - x2)^2 - (y1 - y2)^2) -> this is what we're calculating
       df['distance_from_{}'.format(i)] = ( # makes new columns in dataframe; format inputs i (the centre point) into {}
            np.sqrt(
                (df['petal_length'] - centroids[i][0]) ** 2 #x co-ord of dataset minus x co-ord of centre point squared
                + (df['petal_width'] - centroids[i][1]) ** 2
            )
        )
    centroid_distance_cols = ['distance_from_{}'.format(i) for i in centroids.keys()]
    df['closest'] = df.loc[:, centroid_distance_cols].idxmin(axis=1)
    df['closest'] = df['closest'].map(lambda x: int(x.lstrip('distance_from_')))
    df['color'] = df['closest'].map(lambda x: colmap[x]) # sets colour for each point
    return df

df = assignment(df, centroids)

import copy

old_centroids = copy.deepcopy(centroids)

def update(k): # function for updating centres, use this in iteration stage.
    for i in centroids.keys():
        centroids[i][0] = np.mean(df[df['closest'] == i]['petal_length']) # updating the centres by finding the mean of x-cords in each cluster
        centroids[i][1] = np.mean(df[df['closest'] == i]['petal_width']) # updating the centres by finding the mean of y-cords in each cluster
    return k

centroids = update(centroids)

# Now we use the assignment function again to regroup the data points and recolour them. Then we use the update function to find new centre points.
# Repeat this until the old and new centre points and have a small enough amount of change.

## Repeat Assigment Stage

df = assignment(df, centroids)

# Continue until all assigned categories don't change any more
while True:
    closest_centroids = df['closest'].copy(deep=True)
    centroids = update(centroids)
    df = assignment(df, centroids)
    if closest_centroids.equals(df['closest']):
        break

#Final clusters: 

fig = plt.figure(figsize=(5, 5))
plt.scatter(df['petal_length'], df['petal_width'], color=df['color'], alpha=0.5, edgecolor='k')
for i in centroids.keys():
    plt.scatter(*centroids[i], color=colmap[i])
plt.xlim(0, 8)
plt.ylim(0, 3)
plt.title("Flowers clustered using K Means")
plt.xlabel("Petal Length")
plt.ylabel("Petal Width")
plt.show()

