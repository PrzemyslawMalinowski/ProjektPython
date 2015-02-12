#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
    Graf na ktorym besdziemy operowac
    @author PM
'''

class Graph:

    def __init__(self, dim):
        self.dimen = dim
        self.graph = [[0 for x in range(dim)] for x in range(dim)] 
        self.start = 0
        
    def PrintAll(self):
        for arr in self.graph:
            print arr
            
    def AddConnection(self, node1, node2, value):
        self.graph[node1][node2] = value
        self.graph[node2][node1] = value
        
    def Deg(self, label):
        deg = 0
        for x in range(self.dimen):
            if self.graph[label][x] != 0:
                deg = deg + 1
                
        return deg
        
    def CheckOre(self):
        degs = []
        
        for x in range(self.dimen):
            degs.append(self.Deg(x))
            
        i = 0
        while i < self.dimen:
            j = i + 1
            
            while j < self.dimen:
                if degs[i] + degs[j] < self.dimen:
                    return False;
                j += 1
                
            i += 1
            
        return True
    
    def GetEdges(self):
        return range(self.dimen)
    
    def SetStartPoint(self, start):
        self.start = start
        
    def GetWeight(self, a, b):
        return self.graph[a][b]
