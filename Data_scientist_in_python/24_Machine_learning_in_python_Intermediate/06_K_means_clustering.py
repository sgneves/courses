#**************************************************************************************************#
#                                                                                                  #
# 06_K_means_clustering                                                                            #
#                                                                                                  #
# Authors: S.G.M. Neves                                                                            #
#                                                                                                  #
#**************************************************************************************************#

#%% 1. Clustering NBA Players
import pandas as pd
import numpy as np

nba = pd.read_csv("nba_2013.csv")
nba.head(3)

#--------------------------------------------------------------------------------------------------#

#%% 2. Point Guards
point_guards = nba[nba['pos'] == 'PG'].copy()

#--------------------------------------------------------------------------------------------------#

#%% 3. Points Per Game
point_guards['ppg'] = point_guards['pts'] / point_guards['g']

#--------------------------------------------------------------------------------------------------#

#%% 4. Assist Turnover Ratio
point_guards = point_guards[point_guards['tov'] != 0]

point_guards['atr'] = point_guards['ast'] / point_guards['tov']

#--------------------------------------------------------------------------------------------------#

#%% 5. Visualizing the Point Guards
import matplotlib.pyplot as plt

plt.scatter(point_guards['ppg'], point_guards['atr'], c='y')
plt.title("Point Guards")
plt.xlabel('Points Per Game', fontsize=13)
plt.ylabel('Assist Turnover Ratio', fontsize=13)
plt.show()

#--------------------------------------------------------------------------------------------------#

#%% 6. Clustering players
# No code

#--------------------------------------------------------------------------------------------------#

#%% 7. The Algorithm
num_clusters = 5

# Use numpy's random function to generate a list, length: num_clusters, of indices
random_initial_points = np.random.choice(point_guards.index, size=num_clusters)

# Use the random indices to create the centroids
centroids = point_guards.loc[random_initial_points]

#--------------------------------------------------------------------------------------------------#

#%% 8. Visualize Centroids
plt.scatter(point_guards['ppg'], point_guards['atr'], c='yellow')
plt.scatter(centroids['ppg'], centroids['atr'], c='red')
plt.title("Centroids")
plt.xlabel('Points Per Game', fontsize=13)
plt.ylabel('Assist Turnover Ratio', fontsize=13)
plt.show()

#--------------------------------------------------------------------------------------------------#

#%% 9. Setup (continued)
centroids_dict = dict(zip(range(centroids.shape[0]), centroids[['ppg','atr']].values.tolist()))

#--------------------------------------------------------------------------------------------------#

#%% 10. Step 1 (Euclidean Distance)
import math

def calculate_distance(centroid, player_values):
    root_distance = 0

    for x in range(0, len(centroid)):
        difference = centroid[x] - player_values[x]
        squared_difference = difference**2
        root_distance += squared_difference

    euclid_distance = math.sqrt(root_distance)
    return euclid_distance

q = [5, 2]
p = [3,1]

# Sqrt(5) = ~2.24
print(calculate_distance(q, p))

#--------------------------------------------------------------------------------------------------#

#%% 11. Step 1 (Continued)
def assign_to_cluster(row):

    distances = [calculate_distance(centroid, row[['ppg','atr']]) for centroid in centroids_dict.values()]

    return np.array(distances).argmin()

point_guards['cluster'] = point_guards.apply(assign_to_cluster, axis=1)

#--------------------------------------------------------------------------------------------------#

#%% 12. Visualizing Clusters
# Visualizing clusters
def visualize_clusters(df, num_clusters):
    colors = ['b', 'g', 'r', 'c', 'm', 'y', 'k']

    for n in range(num_clusters):
        clustered_df = df[df['cluster'] == n]
        plt.scatter(clustered_df['ppg'], clustered_df['atr'], c=colors[n-1])
        plt.xlabel('Points Per Game', fontsize=13)
        plt.ylabel('Assist Turnover Ratio', fontsize=13)
    plt.show()

visualize_clusters(point_guards, 5)

#--------------------------------------------------------------------------------------------------#

#%% 13. Step 2
def recalculate_centroids(df):

    coord = df.groupby("cluster")[['ppg','atr']].mean().values.tolist()

    return dict(zip(range(centroids.shape[0]), coord))

centroids_dict = recalculate_centroids(point_guards)

#--------------------------------------------------------------------------------------------------#

#%% 14. Repeat Step 1
point_guards['cluster'] = point_guards.apply(lambda row: assign_to_cluster(row), axis=1)
visualize_clusters(point_guards, num_clusters)

#--------------------------------------------------------------------------------------------------#

#%% 15. Repeat Step 2 and Step 1
centroids_dict = recalculate_centroids(point_guards)
point_guards['cluster'] = point_guards.apply(lambda row: assign_to_cluster(row), axis=1)
visualize_clusters(point_guards, num_clusters)

#--------------------------------------------------------------------------------------------------#

#%% 16. Challenges of K-Means
from sklearn.cluster import KMeans

kmeans = KMeans(n_clusters=num_clusters)
kmeans.fit(point_guards[['ppg', 'atr']])
point_guards['cluster'] = kmeans.labels_

visualize_clusters(point_guards, num_clusters)

#--------------------------------------------------------------------------------------------------#

#%% 17. Conclusion
# No code
