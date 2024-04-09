import networkx as nx
import matplotlib.pyplot as plt
import numpy as np

# Assuming the dataset has been downloaded and is available locally as "twitter_combined.txt.gz"
# Load the dataset into a directed graph
G_directed = nx.read_edgelist('/mnt/data/twitter_combined.txt.gz', create_using=nx.DiGraph())

# Convert the directed graph to an undirected graph
G_undirected = G_directed.to_undirected()

# Extract the largest component for centrality analysis (to ensure connectivity)
largest_cc = max(nx.connected_components(G_undirected), key=len)
G_largest = G_undirected.subgraph(largest_cc).copy()

# Check basic information about the undirected largest component
(num_nodes, num_edges) = (G_largest.number_of_nodes(), G_largest.number_of_edges())
num_nodes, num_edges
