#!/usr/bin/env python

"""
Driver module for all unit testing.

This module generates the suites for all of the test classes and runs
the entire set of tests in the /test directory.

:filename test_driver.py
"""

# Necessary imports
import test_matching_simple
import test_matching_compound
import test_matching_random

import matplotlib.pyplot as plt
import networkx as nx
import unittest

def showGraph(G, mate, label=""):
    """ Print the graph given, showing the matched edges.
    
    :param G - the NetworkX graph given
    :param mate - the dictionary of matched edges
    :param label - the title of the figure (default "")
    :return Nothing
    """
    
    # Set the positions for all nodes and the figure size
    plt.close('all')
    plt.figure( figsize=(10, 10) )
    pos = nx.graphviz_layout(G, prog='sfdp', args='')
    
    # Draw the graph with node labels and a title
    plt.title(label)
    nx.draw(G, pos, node_size=400, with_labels=True)
    
    # Draw the matched edges
    nx.draw_networkx_edges(G, pos, edgelist=mate.items(),
                           width=5, alpha=0.4, edge_color='b')
    
    plt.axis('off')
    plt.show()

# Main function
if __name__ == "__main__":
    
    # Run the unit tests from all testing modules and display their name information  
    try:
        matchingSimpleSuite = test_matching_simple.suiteFull()
        matchingCompoundSuite = test_matching_compound.suiteFull()
        matchingRandomSuite = test_matching_random.suiteCase()
        fullSuite = unittest.TestSuite( [matchingRandomSuite] )
        unittest.TextTestRunner( verbosity=2 ).run( fullSuite )
        
    # Without this, an error occurs for the unit tests
    except SystemExit as inst:
        if inst.args[0] is True:
            raise
        
#end
"""
TODO:
1.) verifyOptimum?
2.) baseStar path compression or not?
3.) IPython Notebook
"""