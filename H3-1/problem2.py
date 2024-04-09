import networkx as nx


G_directed = nx.read_edgelist('H3-1/twitter_combined.txt', create_using=nx.DiGraph())

# Conduct the triadic census
triad_census = nx.algorithms.triads.triadic_census(G_directed)

# Print the results
print("Triadic Census Results:")
for triad_type, count in triad_census.items():
    print(f"{triad_type}: {count}")
