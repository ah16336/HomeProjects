## Initialisation

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.DataFrame({ # Dataset that we want to group
    'x': [12, 20, 28, 18, 29, 33, 24, 45, 45, 52, 51, 52, 55, 53, 55, 61, 64, 69, 72],
    'y': [39, 36, 30, 52, 54, 46, 55, 59, 63, 70, 66, 63, 58, 23, 14, 8, 19, 7, 24]
})


np.random.seed(200)
k = 3 # Number of Clusters
# centroids[i] = [x, y]
centroids = { # We are defining in a dictionary our 3 initial centre points
    i+1: [np.random.randint(0, 80), np.random.randint(0, 80)]
    for i in range(k)
}
    
fig = plt.figure(figsize=(5, 5))
plt.scatter(df['x'], df['y'], color='k') # plotting from our dataframe df our data points.
colmap = {1: 'r', 2: 'g', 3: 'b'} # The colours we want for each centre point
for i in centroids.keys(): # for each entry in the dictionary
    plt.scatter(*centroids[i], color=colmap[i]) # plot the centre points with the previously defined colours
plt.xlim(0, 80)
plt.ylim(0, 80)
plt.show()

## Assignment Stage

def assignment(df, centroids): # function with database and centre points as arguments; calculates distance between points and centre points and finds closest centre for each point
    for i in centroids.keys(): # loops through each centre
        # sqrt((x1 - x2)^2 - (y1 - y2)^2) -> this is what we're calculating
       df['distance_from_{}'.format(i)] = ( # makes new columns in dataframe; format inputs i (the centre point) into {}
            np.sqrt(
                (df['x'] - centroids[i][0]) ** 2 #x co-ord of dataset minus x co-ord of centre point squared
                + (df['y'] - centroids[i][1]) ** 2
            )
        )
    centroid_distance_cols = ['distance_from_{}'.format(i) for i in centroids.keys()]
    df['closest'] = df.loc[:, centroid_distance_cols].idxmin(axis=1)
    df['closest'] = df['closest'].map(lambda x: int(x.lstrip('distance_from_')))
    df['color'] = df['closest'].map(lambda x: colmap[x]) # sets colour for each point
    return df

df = assignment(df, centroids)
print(df.head())

fig = plt.figure(figsize=(5, 5))
plt.scatter(df['x'], df['y'], color=df['color'], alpha=0.5, edgecolor='k') # plotting the results of using our function
for i in centroids.keys():
    plt.scatter(*centroids[i], color=colmap[i])
plt.xlim(0, 80)
plt.ylim(0, 80)
plt.show()

## Updating Stage

import copy

old_centroids = copy.deepcopy(centroids)

def update(k): # function for updating centres, use this in iteration stage.
    for i in centroids.keys():
        centroids[i][0] = np.mean(df[df['closest'] == i]['x']) # updating the centres by finding the mean of x-cords in each cluster
        centroids[i][1] = np.mean(df[df['closest'] == i]['y']) # updating the centres by finding the mean of y-cords in each cluster
    return k

centroids = update(centroids)
    
fig = plt.figure(figsize=(5, 5)) # plotting new centres
ax = plt.axes()
plt.scatter(df['x'], df['y'], color=df['color'], alpha=0.5, edgecolor='k')
for i in centroids.keys():
    plt.scatter(*centroids[i], color=colmap[i])
plt.xlim(0, 80)
plt.ylim(0, 80)
for i in old_centroids.keys(): # arrows showing us the change in the centre points after iteration
    old_x = old_centroids[i][0]
    old_y = old_centroids[i][1]
    dx = (centroids[i][0] - old_centroids[i][0]) * 0.75 # change in x between old and new centre points
    dy = (centroids[i][1] - old_centroids[i][1]) * 0.75 # change in y between old and new centre points
    ax.arrow(old_x, old_y, dx, dy, head_width=2, head_length=3, fc=colmap[i], ec=colmap[i])
plt.show()

# Now we use the assignment function again to regroup the data points and recolour them. Then we use the update function to find new centre points.'
# Repeat this until the old and new centre points and have a small enough amount of change.

## Repeat Assigment Stage

df = assignment(df, centroids)

# Plot results
fig = plt.figure(figsize=(5, 5))
plt.scatter(df['x'], df['y'], color=df['color'], alpha=0.5, edgecolor='k')
for i in centroids.keys():
    plt.scatter(*centroids[i], color=colmap[i])
plt.xlim(0, 80)
plt.ylim(0, 80)
plt.show()

# Continue until all assigned categories don't change any more
while True:
    closest_centroids = df['closest'].copy(deep=True)
    centroids = update(centroids)
    df = assignment(df, centroids)
    if closest_centroids.equals(df['closest']):
        break

fig = plt.figure(figsize=(5, 5))
plt.scatter(df['x'], df['y'], color=df['color'], alpha=0.5, edgecolor='k')
for i in centroids.keys():
    plt.scatter(*centroids[i], color=colmap[i])
plt.xlim(0, 80)
plt.ylim(0, 80)
plt.show()