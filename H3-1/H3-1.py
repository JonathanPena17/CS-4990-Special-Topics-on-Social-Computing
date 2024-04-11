import networkx as nx
import matplotlib.pyplot as plt
import numpy as np

##### Problem 1.1 #################################################################

# Load the dataset into a directed graph
G_directed = nx.read_edgelist('twitter_combined.txt', create_using=nx.DiGraph())

# Convert the directed graph to an undirected graph
G_undirected = G_directed.to_undirected()

# Extract the largest component for centrality analysis (to ensure connectivity)
largest_cc = max(nx.connected_components(G_undirected), key=len)
G_largest = G_undirected.subgraph(largest_cc).copy()

# Calculate centrality measures
degree_centrality = nx.degree_centrality(G_largest)
closeness_centrality = nx.closeness_centrality(G_largest)
betweenness_centrality = nx.betweenness_centrality(G_largest, normalized=True)

##### Problem 1.2 #################################################################

# Degree Centrality Histogram
plt.figure(figsize=(10, 7))
plt.hist(list(degree_centrality.values()), bins=50, color='blue')
plt.title('Degree Centrality Histogram')
plt.xlabel('Degree Centrality')
plt.ylabel('Count')
plt.savefig('degree_centrality_histogram.png')
plt.close()

# Closeness Centrality Histogram
plt.figure(figsize=(10, 7))
plt.hist(list(closeness_centrality.values()), bins=50, color='green')
plt.title('Closeness Centrality Histogram')
plt.xlabel('Closeness Centrality')
plt.ylabel('Count')
plt.savefig('closeness_centrality_histogram.png')
plt.close()

# Betweenness Centrality Histogram
plt.figure(figsize=(10, 7))
plt.hist(list(betweenness_centrality.values()), bins=50, color='red')
plt.title('Betweenness Centrality Histogram')
plt.xlabel('Betweenness Centrality')
plt.ylabel('Count')
plt.savefig('betweenness_centrality_histogram.png')
plt.close()

##### Problem 1.3 #################################################################

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

print("Closeness Centrality Measures:")
print(f"Mean: {mean_closeness}")
print(f"Median: {median_closeness}")
print(f"Standard Deviation: {std_dev_closeness}\n")

print("Betweenness Centrality Measures:")
print(f"Mean: {mean_betweenness}")
print(f"Median: {median_betweenness}")
print(f"Standard Deviation: {std_dev_betweenness}")

##### Problem 2 #################################################################

triad_census = nx.algorithms.triads.triadic_census(G_directed)

print("Triadic Census Results:")
for triad_type, count in triad_census.items():
    print(f"{triad_type}: {count}")