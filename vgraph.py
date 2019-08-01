#!/usr/bin/env python

import os, sys, pylab as plt
from networkx import *

# Project root
os.getcwd()

pathToData = './data/00.dat'

if len(sys.argv) > 1:
    pathToData = sys.argv[1]

# Test sets of nodes for graph visualization.
g = read_edgelist(pathToData)
# Positions for all nodes
pos = nx.spring_layout(g)

# Node number.
nx.draw_networkx_labels(g, pos, font_size=10, font_color='w')
# Create a visualization of the graph and save.
nx.draw(g, pos)
plt.savefig('graph.png')

# Display the resulting graph.
plt.show()

# Close the shape window.
plt.close()
