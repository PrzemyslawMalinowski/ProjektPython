class Node:

	label = ""
	nodes = []
	
	def __init__(self, labelka):
		self.label = labelka
		
	def addNode(self, node):
		self.nodes.append(node)
		
	def printAll():
		print "Wezel: " + self.label
		for node in self.nodes:
			print "* Sasiad: " + self.label