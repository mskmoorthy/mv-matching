#!/usr/bin/env python

"""
Random unit tests for maximum matching function.

This module implements a series of unit tests for max_cardinality_matching.
The tests provided here create random graphs using the graph generators
provided by NetworkX.

:filename test_matching_random.py
"""

# Necessary imports
import matching as mv
import test_driver as td

import networkx as nx
import unittest

class MatchingRandomTests( unittest.TestCase ):
    """
    Random unit tests for the maximum matching function.
    """
    
    def setUp(self):
        pass
        
    def tearDown(self):
        pass
    
    def test010_fast_gnp_random_graph(self):
        """ Small random Erdos-Renyi graph. """
        g = nx.fast_gnp_random_graph(10, 0.2)
        mate1 = mv.max_cardinality_matching( g )
        mate2 = nx.max_weight_matching( g, True )
        self.assertEqual( len(mate1), len(mate2) )
        
    def test011_fast_gnp_random_graph(self):
        """ Large random Erdos-Renyi graph. """
        g = nx.fast_gnp_random_graph(50, 0.2)
        mate1 = mv.max_cardinality_matching( g )
        mate2 = nx.max_weight_matching( g, True )
        self.assertEqual( len(mate1), len(mate2) )
        
    def test012_fast_gnp_random_graph(self):
        """ Large random Erdos-Renyi graph. """
        g = nx.fast_gnp_random_graph(50, 0.8)
        mate1 = mv.max_cardinality_matching( g )
        mate2 = nx.max_weight_matching( g, True )
        self.assertEqual( len(mate1), len(mate2) )

    def test013_fast_gnp_random_graph(self):
        """ Large random Erdos-Renyi graph. """
        g = nx.fast_gnp_random_graph(100, 0.4)
        mate1 = mv.max_cardinality_matching( g )
        mate2 = nx.max_weight_matching( g, True )
        self.assertEqual( len(mate1), len(mate2) )
        
    def test014_fast_gnp_random_graph(self):
        """ Larger random Erdos-Renyi graph. """
        g = nx.fast_gnp_random_graph(200, 0.4)
        mate1 = mv.max_cardinality_matching( g )
        mate2 = nx.max_weight_matching( g, True )
        self.assertEqual( len(mate1), len(mate2) )
        
    def test020_gnp_random_graph(self):
        """ Small random Erdos-Renyi graph. """
        g = nx.gnp_random_graph(10, 0.2)
        mate1 = mv.max_cardinality_matching( g )
        mate2 = nx.max_weight_matching( g, True )
        self.assertEqual( len(mate1), len(mate2) )
        
    def test021_gnp_random_graph(self):
        """ Large random Erdos-Renyi graph. """
        g = nx.gnp_random_graph(50, 0.2)
        mate1 = mv.max_cardinality_matching( g )
        mate2 = nx.max_weight_matching( g, True )
        self.assertEqual( len(mate1), len(mate2) )
        
    def test022_gnp_random_graph(self):
        """ Large random Erdos-Renyi graph. """
        g = nx.gnp_random_graph(50, 0.8)
        mate1 = mv.max_cardinality_matching( g )
        mate2 = nx.max_weight_matching( g, True )
        self.assertEqual( len(mate1), len(mate2) )

    def test023_gnp_random_graph(self):
        """ Large random Erdos-Renyi graph. """
        g = nx.gnp_random_graph(100, 0.4)
        mate1 = mv.max_cardinality_matching( g )
        mate2 = nx.max_weight_matching( g, True )
        self.assertEqual( len(mate1), len(mate2) )
        
    def test024_gnp_random_graph(self):
        """ Larger random Erdos-Renyi graph. """
        g = nx.gnp_random_graph(200, 0.4)
        mate1 = mv.max_cardinality_matching( g )
        mate2 = nx.max_weight_matching( g, True )
        self.assertEqual( len(mate1), len(mate2) )
    
    def test025_gnp_random_graph(self):
        """ Larger random Erdos-Renyi graph. """
        g = nx.gnp_random_graph(200, 0.9)
        mate1 = mv.max_cardinality_matching( g )
        mate2 = nx.max_weight_matching( g, True )
        self.assertEqual( len(mate1), len(mate2) )
    
    def test026_gnp_random_graph(self):
        """ Huge random Erdos-Renyi graph. """
        g = nx.gnp_random_graph(500, 0.6)
        mate1 = mv.max_cardinality_matching( g )
        mate2 = nx.max_weight_matching( g, True )
        self.assertEqual( len(mate1), len(mate2) )
    
    def test030_dense_gnm_random_graph(self):
        """ Small random graph picked from set of all graphs 
        with n nodes and m edges. """
        g = nx.dense_gnm_random_graph(20, 20)
        mate1 = mv.max_cardinality_matching( g )
        mate2 = nx.max_weight_matching( g, True )
        self.assertEqual( len(mate1), len(mate2) )
    
    def test031_dense_gnm_random_graph(self):
        """ Larger random graph picked from set of all graphs 
        with n nodes and m edges. """
        g = nx.dense_gnm_random_graph(100, 1000)
        mate1 = mv.max_cardinality_matching( g )
        mate2 = nx.max_weight_matching( g, True )
        self.assertEqual( len(mate1), len(mate2) )
    
    def test032_dense_gnm_random_graph(self):
        """ Larger random graph picked from set of all graphs 
        with n nodes and m edges. """
        g = nx.dense_gnm_random_graph(100, 3000)
        mate1 = mv.max_cardinality_matching( g )
        mate2 = nx.max_weight_matching( g, True )
        self.assertEqual( len(mate1), len(mate2) )
    
    def test033_dense_gnm_random_graph(self):
        """ Larger random graph picked from set of all graphs 
        with n nodes and m edges. """
        g = nx.dense_gnm_random_graph(300, 5000)
        mate1 = mv.max_cardinality_matching( g )
        mate2 = nx.max_weight_matching( g, True )
        self.assertEqual( len(mate1), len(mate2) )
    
    def test034_dense_gnm_random_graph(self):
        """ Larger random graph picked from set of all graphs 
        with n nodes and m edges. """
        g = nx.dense_gnm_random_graph(300, 30000)
        mate1 = mv.max_cardinality_matching( g )
        mate2 = nx.max_weight_matching( g, True )
        self.assertEqual( len(mate1), len(mate2) )
    
    def test035_dense_gnm_random_graph(self):
        """ Larger random graph picked from set of all graphs 
        with n nodes and m edges. """
        g = nx.dense_gnm_random_graph(300, 10000)
        mate1 = mv.max_cardinality_matching( g )
        mate2 = nx.max_weight_matching( g, True )
        self.assertEqual( len(mate1), len(mate2) )
        
    def test040_erdos_renyi_graph(self):
        """ Small random Erdos-Renyi graph. """
        g = nx.erdos_renyi_graph(10, 0.2)
        mate1 = mv.max_cardinality_matching( g )
        mate2 = nx.max_weight_matching( g, True )
        self.assertEqual( len(mate1), len(mate2) )
        
    def test041_erdos_renyi_graph(self):
        """ Large random Erdos-Renyi graph. """
        g = nx.erdos_renyi_graph(50, 0.2)
        mate1 = mv.max_cardinality_matching( g )
        mate2 = nx.max_weight_matching( g, True )
        self.assertEqual( len(mate1), len(mate2) )
        
    def test042_erdos_renyi_graph(self):
        """ Large random Erdos-Renyi graph. """
        g = nx.erdos_renyi_graph(50, 0.8)
        mate1 = mv.max_cardinality_matching( g )
        mate2 = nx.max_weight_matching( g, True )
        self.assertEqual( len(mate1), len(mate2) )

    def test043_erdos_renyi_graph(self):
        """ Large random Erdos-Renyi graph. """
        g = nx.erdos_renyi_graph(100, 0.4)
        mate1 = mv.max_cardinality_matching( g )
        mate2 = nx.max_weight_matching( g, True )
        self.assertEqual( len(mate1), len(mate2) )
        
    def test044_erdos_renyi_graph(self):
        """ Larger random Erdos-Renyi graph. """
        g = nx.erdos_renyi_graph(200, 0.4)
        mate1 = mv.max_cardinality_matching( g )
        mate2 = nx.max_weight_matching( g, True )
        self.assertEqual( len(mate1), len(mate2) )
    
    def test045_erdos_renyi_graph(self):
        """ Larger random Erdos-Renyi graph. """
        g = nx.erdos_renyi_graph(200, 0.9)
        mate1 = mv.max_cardinality_matching( g )
        mate2 = nx.max_weight_matching( g, True )
        self.assertEqual( len(mate1), len(mate2) )
    
    def test046_erdos_renyi_graph(self):
        """ Huge random Erdos-Renyi graph. """
        g = nx.erdos_renyi_graph(500, 0.6)
        mate1 = mv.max_cardinality_matching( g )
        mate2 = nx.max_weight_matching( g, True )
        self.assertEqual( len(mate1), len(mate2) )
    
    def test050_newman_watts_strogatz_graph(self):
        """ Newman-Watts-Strogatz small world graph. """
        g = nx.newman_watts_strogatz_graph(200, 3, 0.4)
        mate1 = mv.max_cardinality_matching( g )
        mate2 = nx.max_weight_matching( g, True )
        self.assertEqual( len(mate1), len(mate2) )
    
    def test051_newman_watts_strogatz_graph(self):
        """ Newman-Watts-Strogatz small world graph. """
        g = nx.newman_watts_strogatz_graph(200, 10, 0.4)
        mate1 = mv.max_cardinality_matching( g )
        mate2 = nx.max_weight_matching( g, True )
        self.assertEqual( len(mate1), len(mate2) )
    
    def test052_newman_watts_strogatz_graph(self):
        """ Newman-Watts-Strogatz small world graph. """
        g = nx.newman_watts_strogatz_graph(200, 100, 0.4)
        mate1 = mv.max_cardinality_matching( g )
        mate2 = nx.max_weight_matching( g, True )
        self.assertEqual( len(mate1), len(mate2) )
    
    def test053_newman_watts_strogatz_graph(self):
        """ Newman-Watts-Strogatz small world graph. """
        g = nx.newman_watts_strogatz_graph(200, 100, 0.8)
        mate1 = mv.max_cardinality_matching( g )
        mate2 = nx.max_weight_matching( g, True )
        self.assertEqual( len(mate1), len(mate2) )
    
    def test054_newman_watts_strogatz_graph(self):
        """ Newman-Watts-Strogatz small world graph. """
        g = nx.newman_watts_strogatz_graph(200, 50, 0.8)
        mate1 = mv.max_cardinality_matching( g )
        mate2 = nx.max_weight_matching( g, True )
        self.assertEqual( len(mate1), len(mate2) )
    
    def test055_newman_watts_strogatz_graph(self):
        """ Newman-Watts-Strogatz small world graph. """
        g = nx.newman_watts_strogatz_graph(200, 10, 0.8)
        mate1 = mv.max_cardinality_matching( g )
        mate2 = nx.max_weight_matching( g, True )
        self.assertEqual( len(mate1), len(mate2) )
        
    def test056_newman_watts_strogatz_graph(self):
        """ Newman-Watts-Strogatz small world graph. """
        g = nx.newman_watts_strogatz_graph(200, 100, 0.1)
        mate1 = mv.max_cardinality_matching( g )
        mate2 = nx.max_weight_matching( g, True )
        self.assertEqual( len(mate1), len(mate2) )
        
    def test060_watts_strogatz_graph(self):
        """ Watts-Strogatz small world graph. """
        g = nx.watts_strogatz_graph(200, 3, 0.4)
        mate1 = mv.max_cardinality_matching( g )
        mate2 = nx.max_weight_matching( g, True )
        self.assertEqual( len(mate1), len(mate2) )
    
    def test061_watts_strogatz_graph(self):
        """ Watts-Strogatz small world graph. """
        g = nx.watts_strogatz_graph(200, 10, 0.4)
        mate1 = mv.max_cardinality_matching( g )
        mate2 = nx.max_weight_matching( g, True )
        self.assertEqual( len(mate1), len(mate2) )
    
    def test062_watts_strogatz_graph(self):
        """ Watts-Strogatz small world graph. """
        g = nx.watts_strogatz_graph(200, 100, 0.4)
        mate1 = mv.max_cardinality_matching( g )
        mate2 = nx.max_weight_matching( g, True )
        self.assertEqual( len(mate1), len(mate2) )
    
    def test063_watts_strogatz_graph(self):
        """ Watts-Strogatz small world graph. """
        g = nx.watts_strogatz_graph(200, 100, 0.8)
        mate1 = mv.max_cardinality_matching( g )
        mate2 = nx.max_weight_matching( g, True )
        self.assertEqual( len(mate1), len(mate2) )
    
    def test064_watts_strogatz_graph(self):
        """ Watts-Strogatz small world graph. """
        g = nx.watts_strogatz_graph(200, 50, 0.8)
        mate1 = mv.max_cardinality_matching( g )
        mate2 = nx.max_weight_matching( g, True )
        self.assertEqual( len(mate1), len(mate2) )
    
    def test065_watts_strogatz_graph(self):
        """ Watts-Strogatz small world graph. """
        g = nx.watts_strogatz_graph(200, 10, 0.8)
        mate1 = mv.max_cardinality_matching( g )
        mate2 = nx.max_weight_matching( g, True )
        self.assertEqual( len(mate1), len(mate2) )
        
    def test066_watts_strogatz_graph(self):
        """ Watts-Strogatz small world graph. """
        g = nx.watts_strogatz_graph(200, 100, 0.1)
        mate1 = mv.max_cardinality_matching( g )
        mate2 = nx.max_weight_matching( g, True )
        self.assertEqual( len(mate1), len(mate2) )
    
    def test070_random_regular_graph(self):
        """ Random regular graph. """
        g = nx.random_regular_graph(10, 100)
        mate1 = mv.max_cardinality_matching( g )
        mate2 = nx.max_weight_matching( g, True )
        self.assertEqual( len(mate1), len(mate2) )
    
    def test071_random_regular_graph(self):
        """ Random regular graph. """
        g = nx.random_regular_graph(20, 100)
        mate1 = mv.max_cardinality_matching( g )
        mate2 = nx.max_weight_matching( g, True )
        self.assertEqual( len(mate1), len(mate2) )
        
    def test072_random_regular_graph(self):
        """ Random regular graph. """
        g = nx.random_regular_graph(30, 100)
        mate1 = mv.max_cardinality_matching( g )
        mate2 = nx.max_weight_matching( g, True )
        self.assertEqual( len(mate1), len(mate2) )
        
    def test073_random_regular_graph(self):
        """ Random regular graph. """
        g = nx.random_regular_graph(5, 100)
        mate1 = mv.max_cardinality_matching( g )
        mate2 = nx.max_weight_matching( g, True )
        self.assertEqual( len(mate1), len(mate2) )
    
    def test080_barabasi_albert_graph(self):
        """ Random graph using Barabasi-Albert preferential
        attachment model. """
        g = nx.barabasi_albert_graph(100, 50)
        mate1 = mv.max_cardinality_matching( g )
        mate2 = nx.max_weight_matching( g, True )
        self.assertEqual( len(mate1), len(mate2) )
    
    def test081_barabasi_albert_graph(self):
        """ Random graph using Barabasi-Albert preferential
        attachment model. """
        g = nx.barabasi_albert_graph(100, 10)
        mate1 = mv.max_cardinality_matching( g )
        mate2 = nx.max_weight_matching( g, True )
        self.assertEqual( len(mate1), len(mate2) )
    
    def test082_barabasi_albert_graph(self):
        """ Random graph using Barabasi-Albert preferential
        attachment model. """
        g = nx.barabasi_albert_graph(100, 80)
        mate1 = mv.max_cardinality_matching( g )
        mate2 = nx.max_weight_matching( g, True )
        self.assertEqual( len(mate1), len(mate2) )
    
    def test083_barabasi_albert_graph(self):
        """ Random graph using Barabasi-Albert preferential
        attachment model. """
        g = nx.barabasi_albert_graph(100, 5)
        mate1 = mv.max_cardinality_matching( g )
        mate2 = nx.max_weight_matching( g, True )
        self.assertEqual( len(mate1), len(mate2) )
    
    def test090_powerlaw_cluster_graph(self):
        """ Random graph using Holme and Kim algorithm. """
        g = nx.powerlaw_cluster_graph(100, 30, 0.4)
        mate1 = mv.max_cardinality_matching( g )
        mate2 = nx.max_weight_matching( g, True )
        self.assertEqual( len(mate1), len(mate2) )
    
    def test091_powerlaw_cluster_graph(self):
        """ Random graph using Holme and Kim algorithm. """
        g = nx.powerlaw_cluster_graph(100, 10, 0.4)
        mate1 = mv.max_cardinality_matching( g )
        mate2 = nx.max_weight_matching( g, True )
        self.assertEqual( len(mate1), len(mate2) )
    
    def test092_powerlaw_cluster_graph(self):
        """ Random graph using Holme and Kim algorithm. """
        g = nx.powerlaw_cluster_graph(100, 10, 0.8)
        mate1 = mv.max_cardinality_matching( g )
        mate2 = nx.max_weight_matching( g, True )
        self.assertEqual( len(mate1), len(mate2) )
        
    def test093_powerlaw_cluster_graph(self):
        """ Random graph using Holme and Kim algorithm. """
        g = nx.powerlaw_cluster_graph(100, 50, 0.8)
        mate1 = mv.max_cardinality_matching( g )
        mate2 = nx.max_weight_matching( g, True )
        self.assertEqual( len(mate1), len(mate2) )
    
    def test100_random_lobster(self):
        """ Random lobster graph. """
        g = nx.random_lobster(100, 0.3, 0.3)
        mate1 = mv.max_cardinality_matching( g )
        mate2 = nx.max_weight_matching( g, True )
        self.assertEqual( len(mate1), len(mate2) )
    
    def test101_random_lobster(self):
        """ Random lobster graph. """
        g = nx.random_lobster(100, 0.8, 0.8)
        mate1 = mv.max_cardinality_matching( g )
        mate2 = nx.max_weight_matching( g, True )
        self.assertEqual( len(mate1), len(mate2) )
    
    def test102_random_lobster(self):
        """ Random lobster graph. """
        g = nx.random_lobster(100, 0.8, 0.3)
        mate1 = mv.max_cardinality_matching( g )
        mate2 = nx.max_weight_matching( g, True )
        self.assertEqual( len(mate1), len(mate2) )
    
    def test103_random_lobster(self):
        """ Random lobster graph. """
        g = nx.random_lobster(100, 0.3, 0.8)
        mate1 = mv.max_cardinality_matching( g )
        mate2 = nx.max_weight_matching( g, True )
        self.assertEqual( len(mate1), len(mate2) )
    
    def test104_random_lobster(self):
        """ Random lobster graph. """
        g = nx.random_lobster(101, 0.3, 0.8)
        mate1 = mv.max_cardinality_matching( g )
        mate2 = nx.max_weight_matching( g, True )
        self.assertEqual( len(mate1), len(mate2) )
    
    def test110_random_shell_graph(self):
        """ Random shell graph. """
        g = nx.random_shell_graph([(10,20,0.8),(20,40,0.8)])
        mate1 = mv.max_cardinality_matching( g )
        mate2 = nx.max_weight_matching( g, True )
        self.assertEqual( len(mate1), len(mate2) )
    
    def test111_random_shell_graph(self):
        """ Random shell graph. """
        g = nx.random_shell_graph([(50,100,0.4),(50,100,0.4)])
        mate1 = mv.max_cardinality_matching( g )
        mate2 = nx.max_weight_matching( g, True )
        self.assertEqual( len(mate1), len(mate2) )
    
    def test112_random_shell_graph(self):
        """ Random shell graph. """
        g = nx.random_shell_graph([(50,100,0.1),(50,100,0.1)])
        mate1 = mv.max_cardinality_matching( g )
        mate2 = nx.max_weight_matching( g, True )
        self.assertEqual( len(mate1), len(mate2) )
        
    def test113_random_shell_graph(self):
        """ Random shell graph. """
        g = nx.random_shell_graph([(50,200,0.5),(50,300,0.5)])
        mate2 = nx.max_weight_matching( g, True )
        mate1 = mv.max_cardinality_matching( g )
        self.assertEqual( len(mate1), len(mate2) )
        
    def test114_random_shell_graph(self):
        """ Random shell graph. """
        g = nx.random_shell_graph([(7,15,0.4),(7,15,0.4)])
        mate1 = mv.max_cardinality_matching( g )
        mate2 = nx.max_weight_matching( g, True )
        self.assertEqual( len(mate1), len(mate2) )
    
    def test115_random_shell_graph(self):
        """ Random shell graph that completely fails. """
        g = nx.Graph({0: {8: {}, 1: {}, 2: {}, 5: {}}\
                      , 1: {0: {}, 8: {}, 4: {}, 5: {}}\
                      , 2: {0: {}, 10: {}}, 3: {4: {}, 12: {}, 13: {}, 7: {}}\
                      , 4: {1: {}, 10: {}, 3: {}}, 5: {0: {}, 1: {}, 13: {}, 8: {}}\
                      , 6: {}, 7: {9: {}, 10: {}, 3: {}}, 8: {0: {}, 1: {}, 11: {}, 12: {}, 5: {}}\
                      , 9: {10: {}, 7: {}}, 10: {9: {}, 2: {}, 4: {}, 13: {}, 7: {}}\
                      , 11: {8: {}}, 12: {8: {}, 3: {}}, 13: {10: {}, 3: {}, 5: {}}})
        mate2 = nx.max_weight_matching( g, True )
        #td.showGraph(g, mate2, "test115_random_shell_graph_edmonds")
        mate1 = mv.max_cardinality_matching( g )
        self.assertEqual( len(mate1), len(mate2) )
        
def suiteCase():
    """
    Creates a suite of the selected set of unit tests from MatchingRandomTests.
    """
    
    tests = ['test110_random_shell_graph','test111_random_shell_graph','test112_random_shell_graph','test113_random_shell_graph']
    return unittest.TestSuite( map(MatchingRandomTests, tests) )

def suiteFull():
    """
    Creates a suite of the full set of unit tests from MatchingRandomTests.
    """
    
    return unittest.TestLoader().loadTestsFromTestCase( MatchingRandomTests )

#end