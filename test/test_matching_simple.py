#!/usr/bin/env python

"""
Simple unit tests for maximum matching function.

This module implements a series of unit tests for max_cardinality_matching.
The tests provided here are simple in the sense that the number of nodes
for each graph tested does not exceed 20. This is the first series of unit 
tests for the function that tests linear graphs, as well as small bloom
configurations.

:filename test_matching_simple.py
"""

# Necessary imports
import matching as mv
import test_driver as td

import networkx as nx
import unittest

class MatchingSimpleTests( unittest.TestCase ):
    """
    Simple unit tests for the maximum matching function.
    """
    
    def setUp(self):
        pass
        
    def tearDown(self):
        pass
    
    def test010_empty(self):
        """ Empty input graph. """
        g = nx.Graph()
        self.assertEqual(mv.max_cardinality_matching( g ), { })
        
    def test020_singleedge(self):
        """ Single edge. """
        g = nx.Graph()
        g.add_edge(0,1)
        mate1 = mv.max_cardinality_matching( g )
        mate2 = nx.max_weight_matching( g, True )
        self.assertEqual( len(mate1), len(mate2) )
        
    def test030_twoedges(self):
        """ Two edges. """
        g = nx.Graph()
        g.add_edges_from([(0,1),(1,2)])
        mate1 = mv.max_cardinality_matching( g )
        mate2 = nx.max_weight_matching( g, True )
        self.assertEqual( len(mate1), len(mate2) )
        
    def test040_threeedges(self):
        """ Three edges, linear. """
        g = nx.Graph()
        g.add_edges_from([(0,1),(1,2),(2,3)])
        mate1 = mv.max_cardinality_matching( g )
        mate2 = nx.max_weight_matching( g, True )
        self.assertEqual( len(mate1), len(mate2) )
        
    def test050_linear(self):
        """ Multiple edges, linear. """
        g = nx.Graph()
        g.add_edges_from([(0,1),(1,2),(2,3),(3,4),(4,5),(5,6)])
        mate1 = mv.max_cardinality_matching( g )
        mate2 = nx.max_weight_matching( g, True )
        self.assertEqual( len(mate1), len(mate2) )
        
    def test060_circle(self):
        """ Multiple edges, circle of odd length. """
        g = nx.Graph()
        g.add_edges_from([(0,1),(1,2),(2,3),(3,4),(4,5),(5,6),(6,0)])
        mate1 = mv.max_cardinality_matching( g )
        mate2 = nx.max_weight_matching( g, True )
        self.assertEqual( len(mate1), len(mate2) )
        
    def test070_circle(self):
        """ Multiple edges, circle of even length. """
        g = nx.Graph()
        g.add_edges_from([(0,1),(1,2),(2,3),(3,4),(4,5),(5,0)])
        mate1 = mv.max_cardinality_matching( g )
        mate2 = nx.max_weight_matching( g, True )
        self.assertEqual( len(mate1), len(mate2) )
        
    def test080_singlebloom(self):
        """ Single bloom, one edge extension. """
        g = nx.Graph()
        g.add_edges_from([(0,1),(1,2),(2,3),(3,4),(4,5),(5,1)])
        mate1 = mv.max_cardinality_matching( g )
        mate2 = nx.max_weight_matching( g, True )
        td.showGraph(g, mate1, "test080_singlebloom")
        self.assertEqual( len(mate1), len(mate2) )
        
    def test090_singlebloom(self):
        """ Single bloom, two edge extensions, case 1. """
        g = nx.Graph()
        g.add_edges_from([(0,1),(1,2),(2,3),(3,4),(4,5),(5,1),(3,6)])
        mate1 = mv.max_cardinality_matching( g )
        mate2 = nx.max_weight_matching( g, True )
        self.assertEqual( len(mate1), len(mate2) )
        
    def test100_singlebloom(self):
        """ Single bloom, two edge extensions, case 2. """
        g = nx.Graph()
        g.add_edges_from([(0,1),(1,2),(2,3),(3,4),(4,5),(5,1),(4,6)])
        mate1 = mv.max_cardinality_matching( g )
        mate2 = nx.max_weight_matching( g, True )
        self.assertEqual( len(mate1), len(mate2) )
        
    def test110_singlebloom(self):
        """ Single bloom, two extensions. """
        g = nx.Graph()
        g.add_edges_from([(0,1),(1,2),(2,3),(3,4),(4,5),(5,1),(4,6),(6,7)])
        mate1 = mv.max_cardinality_matching( g )
        mate2 = nx.max_weight_matching( g, True )
        td.showGraph(g, mate1, "test110_singlebloom")
        self.assertEqual( len(mate1), len(mate2) )
        
    def test120_singlebloom(self):
        """ Single bloom, three connected components. """
        g = nx.Graph()
        g.add_edges_from([(0,1),(1,2),(2,3),(3,4),(4,5),(5,0),(3,1),(3,5)])
        mate1 = mv.max_cardinality_matching( g )
        mate2 = nx.max_weight_matching( g, True )
        td.showGraph(g, mate1, "test120_singlebloom")
        self.assertEqual( len(mate1), len(mate2) )
        
    def test130_singlebloom(self):
        """ Single bloom, one long extension. """
        g = nx.Graph()
        g.add_edges_from([(0,1),(0,2),(0,7),(0,3),(1,2),(1,3),(2,4),(3,5),(4,6),(5,6),(7,8)\
                         ,(8,9)])
        mate1 = mv.max_cardinality_matching( g )
        mate2 = nx.max_weight_matching( g, True )
        td.showGraph(g, mate1, "test130_singlebloom")
        self.assertEqual( len(mate1), len(mate2) )
        
    def test140_doublebloom(self):
        """ Two blooms, connected together by three edges. """
        g = nx.Graph()
        g.add_edges_from([(0,1),(1,2),(2,3),(3,4),(4,0),(3,11),(11,5),(5,6),(6,7),(7,8),(8,9)\
                         ,(9,10),(10,6)])
        mate1 = mv.max_cardinality_matching( g )
        mate2 = nx.max_weight_matching( g, True )
        td.showGraph(g, mate1, "test140_doublebloom")
        self.assertEqual( len(mate1), len(mate2) )
        
    def test141_doublebloom(self):
        """ Two blooms, connected together by two edges. """
        g = nx.Graph()
        g.add_edges_from([(0,1),(1,2),(2,3),(3,4),(4,0),(3,5),(5,6),(6,7),(7,8),(8,9),(9,10)\
                         ,(10,6)])
        mate1 = mv.max_cardinality_matching( g )
        mate2 = nx.max_weight_matching( g, True )
        td.showGraph(g, mate1, "test141_doublebloom")
        self.assertEqual( len(mate1), len(mate2) )
        
    def test142_doublebloom(self):
        """ Two blooms, connected together by one edge. """
        g = nx.Graph()
        g.add_edges_from([(0,1),(1,2),(2,3),(3,4),(4,0),(3,6),(6,7),(7,8),(8,9),(9,10),(10,6)])
        mate1 = mv.max_cardinality_matching( g )
        mate2 = nx.max_weight_matching( g, True )
        td.showGraph(g, mate1, "test142_doublebloom")
        self.assertEqual( len(mate1), len(mate2) )
        
    def test143_doublebloom(self):
        """ Two blooms, with three connected components each, connected by one edge. """
        g = nx.Graph()
        g.add_edges_from([(0,1),(1,2),(2,3),(2,4),(1,4),(3,4),(4,0),(3,6),(6,7),(7,8),(7,9)\
                         ,(7,10),(8,9),(9,10),(10,6)])
        mate1 = mv.max_cardinality_matching( g )
        mate2 = nx.max_weight_matching( g, True )
        td.showGraph(g, mate1, "test143_doublebloom")
        self.assertEqual( len(mate1), len(mate2) )
        
    def test144_doublebloom(self):
        """ Two blooms, connected at their centers. """
        g = nx.Graph()
        g.add_edges_from([(0,1),(1,2),(2,3),(3,4),(4,0),(3,7),(7,8),(8,9),(9,10),(10,3)])
        mate1 = mv.max_cardinality_matching( g )
        mate2 = nx.max_weight_matching( g, True )
        td.showGraph(g, mate1, "test144_doublebloom")
        self.assertEqual( len(mate1), len(mate2) )
        
    def test145_doublebloom(self):
        """ Two blooms, with three vertices, connected by one edge. """
        g = nx.Graph()
        g.add_edges_from([(0,1),(1,2),(2,0),(2,3),(3,4),(4,5),(5,3),(4,6),(6,7),(7,8),(8,6)])
        mate1 = mv.max_cardinality_matching( g )
        mate2 = nx.max_weight_matching( g, True )
        td.showGraph(g, mate1, "test145_doublebloom")
        self.assertEqual( len(mate1), len(mate2) )
    
    def test146_doublebloom(self):
        """ Two blooms, one embedded inside the other, last example in paper. """
        g = nx.Graph()
        g.add_edges_from([(0,2),(2,1),(2,5),(1,4),(1,3),(3,4),(4,5),(3,6),(6,7),(7,8),(7,10)\
                         ,(5,10),(8,9),(10,11),(9,11),(11,12),(12,13)])
        mate1 = mv.max_cardinality_matching( g )
        mate2 = nx.max_weight_matching( g, True )
        td.showGraph(g, mate1, "test146_doublebloom")
        self.assertEqual( len(mate1), len(mate2) )
    
    def test147_doublebloom(self):
        """ Two blooms, one embedded, connected at their centers. """
        g = nx.Graph()
        g.add_edges_from([(0,1),(1,2),(2,3),(3,0),(3,4),(4,0),(3,7),(7,8),(8,9),(9,10),(10,3)])
        mate1 = mv.max_cardinality_matching( g )
        mate2 = nx.max_weight_matching( g, True )
        td.showGraph(g, mate1, "test147_doublebloom")
        self.assertEqual( len(mate1), len(mate2) )
    
    def test148_doublebloom(self):
        """ Two blooms, one embedded, connected at their centers. """
        g = nx.Graph()
        g.add_edges_from([(0,1),(1,2),(2,3),(4,1),(3,4),(4,0),(3,7),(7,8),(8,9),(9,10),(10,3)])
        mate1 = mv.max_cardinality_matching( g )
        mate2 = nx.max_weight_matching( g, True )
        td.showGraph(g, mate1, "test148_doublebloom")
        self.assertEqual( len(mate1), len(mate2) )
    
    def test149_doublebloom(self):
        """ Two blooms, one embedded, connected at their centers. """
        g = nx.Graph()
        g.add_edges_from([(0,1),(1,2),(2,3),(4,6),(4,1),(3,4),(4,0),(3,7),(7,8),(8,9),(9,10),(10,3)])
        mate1 = mv.max_cardinality_matching( g )
        mate2 = nx.max_weight_matching( g, True )
        td.showGraph(g, mate1, "test149_doublebloom")
        self.assertEqual( len(mate1), len(mate2) )
    
    def test150_triplebloom(self):
        """ Three blooms, connected together. """
        g = nx.Graph()
        g.add_edges_from([(0,1),(1,2),(2,3),(3,4),(4,0),(3,5),(5,6),(5,11),(11,12),(12,13)\
                         ,(13,14),(14,5),(6,7),(7,8),(8,9),(9,10),(10,6)])
        mate1 = mv.max_cardinality_matching( g )
        mate2 = nx.max_weight_matching( g, True )
        td.showGraph(g, mate1, "test150_triplebloom")
        self.assertEqual( len(mate1), len(mate2) )
    
    def test151_triplebloom(self):
        """ Three blooms, connected together with three bridges. """
        g = nx.Graph()
        g.add_edges_from([(0,1),(1,2),(2,3),(3,4),(4,0),(3,5),(5,6),(15,11),(11,12),(12,13)\
                         ,(13,14),(14,15),(6,7),(7,8),(8,9),(9,10),(10,6),(5,15)])
        mate1 = mv.max_cardinality_matching( g )
        mate2 = nx.max_weight_matching( g, True )
        td.showGraph(g, mate1, "test151_triplebloom")
        self.assertEqual( len(mate1), len(mate2) )
    
    def test152_triplebloom(self):
        """ Three hexagons, connected together with three bridges. """
        g = nx.Graph()
        g.add_edges_from([(0,1),(1,16),(16,2),(2,3),(3,4),(4,0),(3,5),(5,6),(15,17),(15,11)\
                         ,(11,12),(12,13),(13,14),(14,17),(6,7),(7,8),(8,9),(18,10),(10,6)\
                         ,(5,15),(9,18)])
        mate1 = mv.max_cardinality_matching( g )
        mate2 = nx.max_weight_matching( g, True )
        td.showGraph(g, mate1, "test152_triplebloom")
        self.assertEqual( len(mate1), len(mate2) )
        
    def test153_triplebloom(self):
        """ Three seven-blooms, connected together with three bridges. """
        g = nx.Graph()
        g.add_edges_from([(0,1),(1,16),(16,19),(19,2),(2,3),(3,4),(4,0),(3,5),(5,6),(15,20)\
                         ,(15,11),(11,12),(12,13),(13,14),(14,17),(17,20),(6,7),(7,8),(8,9)\
                         ,(21,10),(10,6),(5,15),(9,18),(18,21)])
        mate1 = mv.max_cardinality_matching( g )
        mate2 = nx.max_weight_matching( g, True )
        td.showGraph(g, mate1, "test153_triplebloom")
        self.assertEqual( len(mate1), len(mate2) )
        
    def test160_petersengraph(self):
        """ Petersen graph. """
        g = nx.petersen_graph()
        mate1 = mv.max_cardinality_matching( g )
        mate2 = nx.max_weight_matching( g, True )
        td.showGraph(g, mate1, "test160_petersengraph")
        self.assertEqual( len(mate1), len(mate2) )
        
    def test170_bullgraph(self):
        """ Bull graph. """
        g = nx.bull_graph()
        mate1 = mv.max_cardinality_matching( g )
        mate2 = nx.max_weight_matching( g, True )
        #td.showGraph(g, mate1, "test170_bullgraph")
        self.assertEqual( len(mate1), len(mate2) )
        
    def test180_dodecahedralgraph(self):
        """ Dodecahedral graph. """
        g = nx.dodecahedral_graph()
        mate1 = mv.max_cardinality_matching( g )
        mate2 = nx.max_weight_matching( g, True )
        td.showGraph(g, mate1, "test180_dodecahedralgraph")
        self.assertEqual( len(mate1), len(mate2) )
        
    def test190_octahedralgraph(self):
        """ Octahedral graph. """
        g = nx.octahedral_graph()
        mate1 = mv.max_cardinality_matching( g )
        mate2 = nx.max_weight_matching( g, True )
        td.showGraph(g, mate1, "test190_octahedralgraph")
        self.assertEqual( len(mate1), len(mate2) )
        
    def test200_icosahedralgraph(self):
        """ Icosahedral graph. """
        g = nx.icosahedral_graph()
        mate1 = mv.max_cardinality_matching( g )
        mate2 = nx.max_weight_matching( g, True )
        #td.showGraph(g, mate1, "test200_icosahedralgraph")
        self.assertEqual( len(mate1), len(mate2) )

    def test210_cubicgraph(self):
        """ Cubic graph with three connected blooms that admits no perfect matching. """
        g = nx.Graph()
        g.add_edges_from([(0,1),(0,2),(0,3),(1,2),(2,3),(1,4),(3,4),(4,5),(5,6),(5,7),(6,8)\
                         ,(6,9),(8,10),(9,10),(10,11),(11,8),(11,9),(7,12),(7,14),(12,13)\
                         ,(13,14),(15,13),(15,12),(15,14)])
        mate2 = nx.max_weight_matching( g, True )
        td.showGraph(g, mate2, "test210_cubicgraph_edmonds")
        mate1 = mv.max_cardinality_matching( g )
        td.showGraph(g, mate1, "test210_cubicgraph")
        self.assertEqual( len(mate1), len(mate2) )
    
    def test211_cubicgraph(self):
        """ Cubic graph with three connected blooms that is slightly different. """
        g = nx.Graph()
        g.add_edges_from([(0,1),(0,2),(0,3),(1,2),(2,3),(1,4),(3,4),(4,5),(5,6),(5,7),(6,8)\
                         ,(6,9),(8,10),(9,10),(10,11),(11,8),(11,9),(7,12),(7,14),(12,13)\
                         ,(13,14),(15,13),(15,12),(15,14),(12,14),(1,3),(8,9)])
        mate1 = mv.max_cardinality_matching( g )
        mate2 = nx.max_weight_matching( g, True )
        td.showGraph(g, mate1, "test211_cubicgraph")
        td.showGraph(g, mate2, "test211_cubicgraph_edmonds")
        self.assertEqual( len(mate1), len(mate2) )
        
    def test220_fruchtgraph(self):
        """ Frucht graph, smallest cubical graph. """
        g = nx.frucht_graph()
        mate1 = mv.max_cardinality_matching( g )
        mate2 = nx.max_weight_matching( g, True )
        td.showGraph(g, mate1, "test220_fruchtgraph")
        td.showGraph(g, mate2, "test220_fruchtgraph_edmonds")
        self.assertEqual( len(mate1), len(mate2) )
        
    def test230_flowersnarkgraph(self):
        """ Flower snark J5, a flower snark with 20 vertices and 30 edges. """
        g = nx.Graph()
        g.add_edges_from([(0,1),(1,2),(2,3),(3,4),(4,5),(5,6),(6,7),(7,8),(8,9),(9,10)\
                         ,(10,11),(11,12),(12,13),(13,14),(14,0),(15,16),(16,17),(17,18)\
                         ,(18,19),(19,15),(0,15),(1,11),(2,7),(3,16),(4,14),(5,10),(6,17)\
                         ,(8,13),(9,18),(12,19)])
        mate1 = mv.max_cardinality_matching( g )
        mate2 = nx.max_weight_matching( g, True )
        td.showGraph(g, mate1, "test230_flowersnarkgraph")
        td.showGraph(g, mate2, "test230_flowersnarkgraph_edmonds")
        self.assertEqual( len(mate1), len(mate2) )
    
    def test240_disconnected_blooms(self):
        """ Two blooms, connected together by two edges with another disconnected bloom graph. """
        g = nx.Graph()
        g.add_edges_from([(0,1),(1,2),(2,3),(3,4),(4,0),(3,5),(5,6),(6,7),(7,8),(8,9),(9,10)\
                         ,(10,6),(11,12),(12,13),(14,15),(15,11),(12,14),(13,14)])
        mate1 = mv.max_cardinality_matching( g )
        mate2 = nx.max_weight_matching( g, True )
        td.showGraph(g, mate1, "test240_disconnected_blooms")
        self.assertEqual( len(mate1), len(mate2) )
    
    def test250_double_blooms(self):
        """ Two blooms, connected together. """
        g = nx.Graph()
        g.add_edges_from([(1,2),(2,3),(3,4),(4,5),(3,5),(5,6),(6,7),(7,8),(8,9),(7,9),(9,10)\
                          ,(10,11)])
        mate1 = mv.max_cardinality_matching( g )
        mate2 = nx.max_weight_matching( g, True )
        td.showGraph(g, mate1, "test250_double_blooms")
        self.assertEqual( len(mate1), len(mate2) )
        
    def test260_inter_blooms(self):
        """ Two blooms, connected together. """
        g = nx.Graph()
        g.add_edges_from([(1,2),(2,3),(3,4),(4,5),(5,1),(5,6),(6,7),(4,6)])
                          
        mate1 = mv.max_cardinality_matching( g )
        mate2 = nx.max_weight_matching( g, True )
        td.showGraph(g, mate1, "test260_inter_blooms")
        self.assertEqual( len(mate1), len(mate2) )
    
    def test270_grid_graph(self):
        """ Two blooms, connected together. """
        g = nx.Graph()
        g.add_edges_from([(1,2),(2,3),(3,4),(5,6),(6,7),(7,8), (9,10),(10,11),(11,12),(13,14),(14,15),(15,16),
                          (1,5),(5,9),(9,13),(2,6),(6,10),(10,14),(3,7),(7,11),(11,15),(4,8),(8,12),(12,16)])
                          
        mate1 = mv.max_cardinality_matching( g )
        mate2 = nx.max_weight_matching( g, True )
        td.showGraph(g, mate1, "test270_Grid_Graphs")
        self.assertEqual( len(mate1), len(mate2) )
    
    def test271_grid_graph(self):
        """ Two blooms, connected together. """
        g = nx.Graph()
        g.add_edges_from([(1,2),(2,3),(3,4),(5,6),(6,7),(7,8), (9,10),(10,11),(11,12),(13,14),(14,15),(15,16),
                          (1,5),(5,9),(9,13),(2,6),(6,10),(10,14),(3,7),(7,11),(11,15),(4,8),(8,12),(12,16),(16,17),(13,18)])
                          
        mate1 = mv.max_cardinality_matching( g )
        mate2 = nx.max_weight_matching( g, True )
        td.showGraph(g, mate1, "test271_Grid_Graphs")
        self.assertEqual( len(mate1), len(mate2) )
    
    def test280_pentagon_graph(self):
        """ Two blooms, connected together. """
        g = nx.Graph()
        g.add_edges_from([(1,2),(2,3),(1,3),(3,4),(3,5),(4,5),(5,6),(6,7),(5,7),(7,8),(8,9),(7,9),
                          (9,10),(10,2),(2,9)])
                          
        mate1 = mv.max_cardinality_matching( g )
        mate2 = nx.max_weight_matching( g, True )
        td.showGraph(g, mate1, "test280_pentagon_graph")
        self.assertEqual( len(mate1), len(mate2) )
        
def suiteCase():
    """
    Creates a suite of the selected set of unit tests from MatchingSimpleTests.
    """
    
    tests = ['test280_pentagon_graph','test270_grid_graph']
    return unittest.TestSuite( map(MatchingSimpleTests, tests) )

def suiteFull():
    """
    Creates a suite of the full set of unit tests from MatchingSimpleTests.
    """
        
    return unittest.TestLoader().loadTestsFromTestCase( MatchingSimpleTests )

#end