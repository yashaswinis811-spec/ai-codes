import numpy as np
import matplotlib.pyplot as plt

from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score

# Dataset
X = np.array([
    [1, 2],
    [1, 3],
    [2, 2],
    [2, 3],
    [3, 2],
    
    [8, 8],
    [9, 8],
    [8, 9],
    [9, 9],
    [10, 8],
    
    [20, 20],
    [21, 20],
    [20, 21],
    [21, 21],
    [22, 20]
])

# Number of clusters
k = 3

# Create K-Means model
kmeans = KMeans(
    n_clusters=k,
    random_state=42,
    n_init=10
)

# Train the model
kmeans.fit(X)

# Get cluster labels
labels = kmeans.labels_

# Get cluster centers
centers = kmeans.cluster_centers_

print("===== K-MEANS CLUSTERING =====")

print("\nData Points:")
print(X)

print("\nCluster Labels:")
print(labels)

print("\nCluster Centers:")
print(centers)

# Cluster Validation using Silhouette Score
score = silhouette_score(X, labels)

print("\n===== CLUSTER VALIDATION =====")
print("Silhouette Score:", score)

# Plot clusters
plt.scatter(
    X[:, 0],
    X[:, 1],
    c=labels,
    s=100
)

# Plot cluster centers
plt.scatter(
    centers[:, 0],
    centers[:, 1],
    marker='X',
    s=200
)

plt.title("K-Means Clustering")
plt.xlabel("X")
plt.ylabel("Y")

plt.show()