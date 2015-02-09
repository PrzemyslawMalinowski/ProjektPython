#!/usr/bin/env python
# -*- coding: utf-8 -*-

from graph import Graph

'''
    Klasa odpowiadająca za obliczanie TSP
'''

class TSProcessor(object):
    
    def __init__(self, graph):
        self.graph = graph
        
    def SetAlgorithm(self, alg):
        self.alg = alg
        
        if self.graph is not None:
            self.alg.SetGraph(self.graph)
        
    def Calculate(self):
        self.alg.SetGraph(self.graph)
        self.alg.Calculate()
        return [self.alg.path, self.alg.cost]