#!/usr/bin/env python

"""
Compound unit tests for maximum matching function.

This module implements a series of unit tests for max_cardinality_matching.
The tests provided here are compound because the graphs used are iteratively
generated from simpler graphs. NetworkX provides a variety of graph generators
for several classic graphs, many of which are used here. Note that running
the full suite could take some time.

:filename test_matching_compound.py
"""

# Necessary imports
import matching as mv
import test_driver as td

import networkx as nx
import unittest

class MatchingCompoundTests( unittest.TestCase ):
    """
    Compound unit tests for the maximum matching function.
    """
    
    def setUp(self):
        pass
        
    def tearDown(self):
        pass
    
    def test010_ladder_graph(self):
        """ Large ladder graph. """
        g = nx.ladder_graph(1000)
        mate1 = mv.max_cardinality_matching( g )
        mate2 = nx.max_weight_matching( g, True )
        self.assertEqual( len(mate1), len(mate2) )
        
    def test020_barbell_graph(self):
        """ Large barbell graph. """
        g = nx.barbell_graph(500, 20)
        mate2 = nx.max_weight_matching( g, True )
        mate1 = mv.max_cardinality_matching( g )
        self.assertEqual( len(mate1), len(mate2) )
        
    def test021_barbell_graph(self):
        """ Large barbell graph. """
        g = nx.barbell_graph(50, 21)
        mate1 = mv.max_cardinality_matching( g )
        mate2 = nx.max_weight_matching( g, True )
        self.assertEqual( len(mate1), len(mate2) )
        
    def test022_barbell_graph(self):
        """ Large barbell graph. """
        g = nx.barbell_graph(49, 21)
        mate1 = mv.max_cardinality_matching( g )
        mate2 = nx.max_weight_matching( g, True )
        self.assertEqual( len(mate1), len(mate2) )
        
    def test023_barbell_graph(self):
        """ Large barbell graph. """
        g = nx.barbell_graph(49, 20)
        mate1 = mv.max_cardinality_matching( g )
        mate2 = nx.max_weight_matching( g, True )
        self.assertEqual( len(mate1), len(mate2) )
        
    def test024_barbell_graph(self):
        """ Small barbell graph. """
        g = nx.barbell_graph(29, 2)
        mate1 = mv.max_cardinality_matching( g )
        mate2 = nx.max_weight_matching( g, True )
        self.assertEqual( len(mate1), len(mate2) )
    
    def test025_barbell_graph(self):
        """ Very small barbell graph. """
        g = nx.barbell_graph(9, 2)
        mate2 = nx.max_weight_matching( g, True )
        td.showGraph(g, mate2, "test025_barbell_graph_edmonds")
        mate1 = mv.max_cardinality_matching( g )
        self.assertEqual( len(mate1), len(mate2) )
    
    def test026_barbell_graph(self):
        """ Large barbell graph. """
        g = nx.barbell_graph(51, 51)
        mate2 = nx.max_weight_matching( g, True )
        mate1 = mv.max_cardinality_matching( g )
        self.assertEqual( len(mate1), len(mate2) )
    
    def test030_balanced_tree(self):
        """ Large balanced tree. """
        g = nx.balanced_tree(3, 5)
        mate1 = mv.max_cardinality_matching( g )
        mate2 = nx.max_weight_matching( g, True )
        self.assertEqual( len(mate1), len(mate2) )
        
    def test031_balanced_tree(self):
        """ Large balanced tree. """
        g = nx.balanced_tree(4, 5)
        mate1 = mv.max_cardinality_matching( g )
        mate2 = nx.max_weight_matching( g, True )
        self.assertEqual( len(mate1), len(mate2) )
    
    def test032_balanced_tree(self):
        """ Large balanced tree. """
        g = nx.balanced_tree(4, 6)
        mate1 = mv.max_cardinality_matching( g )
        mate2 = nx.max_weight_matching( g, True )
        self.assertEqual( len(mate1), len(mate2) )
        
    def test040_complete_graph(self):
        """ Large complete graph. """
        g = nx.complete_graph(100)
        mate1 = mv.max_cardinality_matching( g )
        mate2 = nx.max_weight_matching( g, True )
        self.assertEqual( len(mate1), len(mate2) )
        
    def test041_complete_graph(self):
        """ Larger complete graph. """
        g = nx.complete_graph(1000)
        mate1 = mv.max_cardinality_matching( g )
        mate2 = nx.max_weight_matching( g, True )
        self.assertEqual( len(mate1), len(mate2) )
    
    def test042_complete_graph(self):
        """ Large complete graph. """
        g = nx.complete_graph(51)
        mate1 = mv.max_cardinality_matching( g )
        mate2 = nx.max_weight_matching( g, True )
        self.assertEqual( len(mate1), len(mate2) )
    
    def test050_complete_bipartite_graph(self):
        """ Large complete bipartite graph. """
        g = nx.complete_bipartite_graph(100, 100)
        mate1 = mv.max_cardinality_matching( g )
        mate2 = nx.max_weight_matching( g, True )
        self.assertEqual( len(mate1), len(mate2) )
    
    def test051_complete_bipartite_graph(self):
        """ Large complete bipartite graph. """
        g = nx.complete_bipartite_graph(100, 200)
        mate1 = mv.max_cardinality_matching( g )
        mate2 = nx.max_weight_matching( g, True )
        self.assertEqual( len(mate1), len(mate2) )
    
    def test060_cycle_graph(self):
        """ Large cycle graph. """
        g = nx.cycle_graph(500)
        mate1 = mv.max_cardinality_matching( g )
        mate2 = nx.max_weight_matching( g, True )
        self.assertEqual( len(mate1), len(mate2) )
    
    def test061_cycle_graph(self):
        """ Large cycle graph. """
        g = nx.cycle_graph(501)
        mate1 = mv.max_cardinality_matching( g )
        mate2 = nx.max_weight_matching( g, True )
        self.assertEqual( len(mate1), len(mate2) )
    
    def test070_dorogovtsev_goltsev_mendes_graph(self):
        """ Large dorogovtsev goltsev mendes graph. """
        g = nx.dorogovtsev_goltsev_mendes_graph(9)
        mate1 = mv.max_cardinality_matching( g )
        mate2 = nx.max_weight_matching( g, True )
        self.assertEqual( len(mate1), len(mate2) )
    
    def test080_grid_2d_graph(self):
        """ Large grid 2d graph. """
        g = nx.grid_2d_graph(10, 10)
        mate1 = mv.max_cardinality_matching( g )
        mate2 = nx.max_weight_matching( g, True )
        self.assertEqual( len(mate1), len(mate2) )
    
    def test081_grid_2d_graph(self):
        """ Large grid 2d graph. """
        g = nx.grid_2d_graph(20, 10)
        mate1 = mv.max_cardinality_matching( g )
        mate2 = nx.max_weight_matching( g, True )
        self.assertEqual( len(mate1), len(mate2) )
    
    def test082_grid_2d_graph(self):
        """ Large grid 2d graph. """
        g = nx.grid_2d_graph(21, 11)
        mate1 = mv.max_cardinality_matching( g )
        mate2 = nx.max_weight_matching( g, True )
        self.assertEqual( len(mate1), len(mate2) )
    
    def test090_hypercube_graph(self):
        """ Large hypercube graph. """
        g = nx.hypercube_graph(5)
        mate1 = mv.max_cardinality_matching( g )
        mate2 = nx.max_weight_matching( g, True )
        self.assertEqual( len(mate1), len(mate2) )
    
    def test091_hypercube_graph(self):
        """ Large hypercube graph. """
        g = nx.hypercube_graph(10)
        mate1 = mv.max_cardinality_matching( g )
        mate2 = nx.max_weight_matching( g, True )
        self.assertEqual( len(mate1), len(mate2) )
    
    def test092_hypercube_graph(self):
        """ Larger hypercube graph. """
        g = nx.hypercube_graph(13)
        mate1 = mv.max_cardinality_matching( g )
        mate2 = nx.max_weight_matching( g, True )
        self.assertEqual( len(mate1), len(mate2) )
        
    def test100_lollipop_graph(self):
        """ Large lollipop graph. """
        g = nx.lollipop_graph(50, 50)
        mate1 = mv.max_cardinality_matching( g )
        mate2 = nx.max_weight_matching( g, True )
        self.assertEqual( len(mate1), len(mate2) )
    
    def test101_lollipop_graph(self):
        """ Large lollipop graph. """
        g = nx.lollipop_graph(50, 51)
        mate1 = mv.max_cardinality_matching( g )
        mate2 = nx.max_weight_matching( g, True )
        self.assertEqual( len(mate1), len(mate2) )
        
    def test102_lollipop_graph(self):
        """ Large lollipop graph. """
        g = nx.lollipop_graph(51, 50)
        mate1 = mv.max_cardinality_matching( g )
        mate2 = nx.max_weight_matching( g, True )
        self.assertEqual( len(mate1), len(mate2) )
    
    def test103_lollipop_graph(self):
        """ Large lollipop graph. """
        g = nx.lollipop_graph(17, 11)
        mate1 = mv.max_cardinality_matching( g )
        mate2 = nx.max_weight_matching( g, True )
        td.showGraph(g, mate1, "test103_lollipop_graph")
        self.assertEqual( len(mate1), len(mate2) )
    
    def test104_lollipop_graph(self):
        """ Small lollipop graph. """
        g = nx.lollipop_graph(13, 13)
        mate1 = mv.max_cardinality_matching( g )
        mate2 = nx.max_weight_matching( g, True )
        self.assertEqual( len(mate1), len(mate2) )
    
    def test105_lollipop_graph(self):
        """ Large lollipop graph. """
        g = nx.lollipop_graph(51, 51)
        mate1 = mv.max_cardinality_matching( g )
        mate2 = nx.max_weight_matching( g, True )
        self.assertEqual( len(mate1), len(mate2) )
    
    def test110_path_graph(self):
        """ Large path graph. """
        g = nx.path_graph(50)
        mate1 = mv.max_cardinality_matching( g )
        mate2 = nx.max_weight_matching( g, True )
        self.assertEqual( len(mate1), len(mate2) )
    
    def test111_path_graph(self):
        """ Large path graph. """
        g = nx.path_graph(51)
        mate1 = mv.max_cardinality_matching( g )
        mate2 = nx.max_weight_matching( g, True )
        self.assertEqual( len(mate1), len(mate2) )
    
    def test120_star_graph(self):
        """ Large star graph. """
        g = nx.star_graph(100)
        mate1 = mv.max_cardinality_matching( g )
        mate2 = nx.max_weight_matching( g, True )
        self.assertEqual( len(mate1), len(mate2) )
    
    def test130_wheel_graph(self):
        """ Large wheel graph. """
        g = nx.wheel_graph(100)
        mate1 = mv.max_cardinality_matching( g )
        mate2 = nx.max_weight_matching( g, True )
        self.assertEqual( len(mate1), len(mate2) )
    
    def test131_wheel_graph(self):
        """ Large wheel graph. """
        g = nx.wheel_graph(101)
        mate1 = mv.max_cardinality_matching( g )
        mate2 = nx.max_weight_matching( g, True )
        self.assertEqual( len(mate1), len(mate2) )
        
    def test140_utility_graph(self):
        """ Utility graph from LCF notation. """
        g = nx.LCF_graph(6, [3, -3], 3)
        mate1 = mv.max_cardinality_matching( g )
        mate2 = nx.max_weight_matching( g, True )
        self.assertEqual( len(mate1), len(mate2) )
        
    def test141_utility_graph(self):
        """ Large utility graph from LCF notation. """
        g = nx.LCF_graph(20, [3, -3], 3)
        mate1 = mv.max_cardinality_matching( g )
        mate2 = nx.max_weight_matching( g, True )
        self.assertEqual( len(mate1), len(mate2) )
    
    def test142_utility_graph(self):
        """ Larger utility graph from LCF notation. """
        g = nx.LCF_graph(60, [3, -3], 3)
        mate1 = mv.max_cardinality_matching( g )
        mate2 = nx.max_weight_matching( g, True )
        td.showGraph(g, mate1, "test142_utility_graph")
        self.assertEqual( len(mate1), len(mate2) )
    
    def test150_generalized_petersen_graph(self):
        """ Generalized petersen graph. """
        g = nx.LCF_graph(20, [-10, -7, 5, -5, 7, -6, -10, -5, 5, 6], 2)
        mate1 = mv.max_cardinality_matching( g )
        mate2 = nx.max_weight_matching( g, True )
        self.assertEqual( len(mate1), len(mate2) )
    
    def test160_prism_graph(self):
        """ 10-prism graph. """
        g = nx.LCF_graph(20, [-3, 3], 10)
        mate1 = mv.max_cardinality_matching( g )
        mate2 = nx.max_weight_matching( g, True )
        self.assertEqual( len(mate1), len(mate2) )
    
    def test170_desargues_graph(self):
        """ Desargues graph. """
        g = nx.LCF_graph(20, [5, -5, 9, -9], 5)
        mate1 = mv.max_cardinality_matching( g )
        mate2 = nx.max_weight_matching( g, True )
        self.assertEqual( len(mate1), len(mate2) )
    
    def test180_tutte_cage_graph(self):
        """ Tutte 12-cage graph. """
        g = nx.LCF_graph(126, [17, 27, -13, -59, -35, 35, -11, 13, -53\
                               , 53, -27, 21, 57, 11, -21, -57, 59, -17], 7)
        mate1 = mv.max_cardinality_matching( g )
        mate2 = nx.max_weight_matching( g, True )
        self.assertEqual( len(mate1), len(mate2) )
        
def suiteCase():
    """
    Creates a suite of the selected set of unit tests from MatchingCompoundTests.
    """
    
    tests = ['test105_lollipop_graph']
    return unittest.TestSuite( map(MatchingCompoundTests, tests) )

def suiteFull():
    """
    Creates a suite of the full set of unit tests from MatchingCompoundTests.
    """
    
    return unittest.TestLoader().loadTestsFromTestCase( MatchingCompoundTests )

#end