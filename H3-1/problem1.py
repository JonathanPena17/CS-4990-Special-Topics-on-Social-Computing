import networkx as nx
import matplotlib.pyplot as plt
import numpy as np


# Load the dataset into a directed graph
G_directed = nx.read_edgelist('H3-1/twitter_combined.txt', create_using=nx.DiGraph())

# Convert the directed graph to an undirected graph
G_undirected = G_directed.to_undirected()

# Extract the largest component for centrality analysis (to ensure connectivity)
largest_cc = max(nx.connected_components(G_undirected), key=len)
G_largest = G_undirected.subgraph(largest_cc).copy()

# Check basic information about the undirected largest component
(num_nodes, num_edges) = (G_largest.number_of_nodes(), G_largest.number_of_edges())
num_nodes, num_edges

# Calculate centrality measures
degree_centrality = nx.degree_centrality(G_largest)
closeness_centrality = nx.closeness_centrality(G_largest)
betweenness_centrality = nx.betweenness_centrality(G_largest, normalized=True)

# Degree Centrality Histogram
plt.figure(figsize=(10, 7))
plt.hist(degree_centrality.values(), bins=50)
plt.title('Degree Centrality Histogram')
plt.xlabel('Degree Centrality')
plt.ylabel('Count')
plt.show()

# Closeness Centrality Histogram
plt.figure(figsize=(10, 7))
plt.hist(closeness_centrality.values(), bins=50)
plt.title('Closeness Centrality Histogram')
plt.xlabel('Closeness Centrality')
plt.ylabel('Count')
plt.show()

# Betweenness Centrality Histogram
plt.figure(figsize=(10, 7))
plt.hist(betweenness_centrality.values(), bins=50)
plt.title('Betweenness Centrality Histogram')
plt.xlabel('Betweenness Centrality')
plt.ylabel('Count')
plt.show()

# Sort nodes by degree centrality and pick the top 200
top_200_nodes = sorted(degree_centrality, key=degree_centrality.get, reverse=True)[:200]

# Extract their closeness and betweenness centrality values
top_200_closeness = [closeness_centrality[node] for node in top_200_nodes]
top_200_betweenness = [betweenness_centrality[node] for node in top_200_nodes]

# Calculate mean, median, and standard deviation for closeness and betweenness
mean_closeness = np.mean(top_200_closeness)
median_closeness = np.median(top_200_closeness)
std_dev_closeness = np.std(top_200_closeness)

mean_betweenness = np.mean(top_200_betweenness)
median_betweenness = np.median(top_200_betweenness)
std_dev_betweenness = np.std(top_200_betweenness)

(mean_closeness, median_closeness, std_dev_closeness), (mean_betweenness, median_betweenness, std_dev_betweenness)