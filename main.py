#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
    Graf na ktorym besdziemy operowac
    @author PM
'''

from graph import Graph
from tsprocessor import TSProcessor
from tspgreedy import TSPGreedy

command = ""
graph = None

'''
    Najwazniejsza czesc programu
'''
while command != "exit":
    command = raw_input("Command: ")
    
    if "create" in command:
        params = command.split(' ')
        
        try:
            graph = Graph(int(params[1]))
            graph.PrintAll()
        except Exception:
            print "Cannot create new graph {probably is not defined matrix size}"
        
    if "custom" in command:
        graph = Graph(4)
        
        graph.AddConnection(0, 1, 1)
        graph.AddConnection(0, 2, 1)
        graph.AddConnection(0, 3, 5)
        graph.AddConnection(1, 2, 3)
        graph.AddConnection(1, 3, 4)
        graph.AddConnection(2, 3, 2)
        
        graph.SetStartPoint(1)
        
        graph.PrintAll()
        
    if "connect" in command:
        params = command.split(' ')
        
        try:
            graph.AddConnection(int(params[1]), int(params[2]), int(params[3]))
        except Exception:
            print "Cannot add new connection (probably bad number of params)"
        finally:
            graph.PrintAll()
        
    if "check ore" in command:
        if graph is None:
            print "Create graph first"
        else:     
            print graph.CheckOre();
        
    if "tsp" in command:
        if graph is None:
            print "Create graph first"
        else:
            processor = TSProcessor(graph)
            
            if "greedy" in command:
                processor.SetAlgorithm(TSPGreedy())
            
            processor.Calculate()
        
    if "help" in command:
        print "Commands in program:"
        print ""
        print "create <<size>> - creates new graph"
        print ""
        print "When graph exists:"
        print "connect <<vertex-a>> <<vertex-b>> <<weight>> - add new connection between vertex A and vertex B"
        print "check ore - check Ore Theorem works on graph"
        print "tsp greedy- run TSP algorithm"
