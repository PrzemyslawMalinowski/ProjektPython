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
		graph = Graph(int(params[1]))
		graph.PrintAll()
		
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
			print "Nie można dodać połączenia"
		finally:
			graph.PrintAll()
		
	if "check ore" in command:
		print graph.CheckOre();
		
	if "tsp" in command:
		processor = TSProcessor(graph)
		
		if "greedy" in command:
			processor.SetAlgorithm(TSPGreedy())
		
		res = processor.Calculate()
		print res