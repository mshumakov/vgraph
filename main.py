import os
import pylab as plt
from networkx import *

# Project root
os.getcwd()

# Test sets of nodes for graph visualization.
g = read_edgelist('data/00.dat')
g.number_of_nodes() # Number of nodes in the graph.
g.number_of_edges() # Number of links between nodes.

# Create a visualization of the graph and save.
nx.draw(g)
plt.savefig('graph.png')

# Display the resulting graph.
plt.show()

# Close the shape window.
plt.close()
