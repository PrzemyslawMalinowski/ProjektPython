#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
    Algorytm implementujący zachłanny algorytm obliczania
    problemu komiwojażera
'''

class TSPGreedy:
    
    def __init__(self):
        self.path = []
        self.cost = 0
        
    def __str__(self):
        return "Zachłanny algorytm"
    
    def SetGraph(self, graph):
        self.graph = graph
        
    def GetMinimumNeighberhood(self, edge, rest):
        min = 9999999999999999
        ed = -1
        
        for e in rest:
            weightTemp = self.graph.GetWeight(edge, e) 
            if min > weightTemp:
                min = weightTemp
                ed = e
        
        return { "edge" : ed, "min" : min }
    
    def CalculatePath(self, currEdge, edges):
        if edges:
            res = self.GetMinimumNeighberhood(currEdge, edges)

            self.cost += res["min"]
            self.path.append(res["edge"])

            if res["edge"] in edges:
                edges.remove(res["edge"])
                
            self.CalculatePath(res["edge"], edges)
            
        
    def Calculate(self):
        if self.graph is not None:
            if self.graph.CheckOre():
                
                print "TSP Greedy alghoritm"
                print "Let us begin:"
                
                start = self.graph.start 
                kek = self.graph.GetEdges()
                kek.remove(start)
                self.CalculatePath(start, kek)
                self.path.insert(0, start)
                self.cost += self.graph.GetWeight(self.path[0], self.path[-1])
                
                print "Founded TSP aprox: " + " -> ".join(map(str, self.path))
                print "Path costs: {0}".format(self.cost)
                
            else:
                
                print "Ore's theorem is not working on this graph"
