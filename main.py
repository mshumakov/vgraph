#!/usr/bin/env python
"""
vGraph graph visualization tool for given sets of studied nodes.
"""
__author__ = """Maksim Shumakov (ms.profile.dev@gmail.com)"""

import os

import pylab as plt
from networkx import *

# Project root
os.getcwd()

# Test sets of nodes for graph visualization.
g = read_edgelist('data/00.dat')
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
