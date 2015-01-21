'''
	Graf na ktorym besdziemy operowac
	@author PM
'''

'''
	void TSP(int v)
{
  int u;

  Sh[shptr++] = v;                // zapamiętujemy na stosie bieżący wierzchołek

  if(shptr < n)                   // jeśli brak ścieżki Hamiltona, to jej szukamy
  {
    visited[v] = true;            // Oznaczamy bieżący wierzchołek jako odwiedzony
    for(u = 0; u < n; u++)        // Przeglądamy sąsiadów wierzchołka v
      if(A[v][u] && !visited[u])  // Szukamy nieodwiedzonego jeszcze sąsiada
      {
        dh += W[v][u];            // Dodajemy wagę krawędzi v-u do sumy
        TSP(u);                   // Rekurencyjnie wywołujemy szukanie cyklu Hamiltona
        dh -= W[v][u];            // Usuwamy wagę krawędzi z sumy
      }
    visited[v] = false;           // Zwalniamy bieżący wierzchołek
  }
  else if(A[v0][v])               // Jeśli znaleziona ścieżka jest cyklem Hamiltona
  {
    dh += W[v][v0];               // to sprawdzamy, czy ma najmniejszą sumę wag
    if(dh < d)                    // Jeśli tak,
    {
      d = dh;                     // To zapamiętujemy tę sumę
      for(u = 0; u < shptr; u++)  // oraz kopiujemy stos Sh do S
        S[u] = Sh[u];
      sptr = shptr;
    }
    dh -= W[v][v0];               // Usuwamy wagę krawędzi v-v0 z sumy
  }
  shptr--;                        // Usuwamy bieżący wierzchołek ze ścieżki
}
'''

class Graph:
	
	graph = None
	dimen = None
	
	def __init__(self, dim):
		self.dimen = dim
		self.graph = [[0 for x in range(dim)] for x in range(dim)] 
		
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
		
	if "connect" in command:
		params = command.split(' ')
		graph.AddConnection(int(params[1]), int(params[2]), int(params[3]))
		graph.PrintAll()
		
	if "check ore" in command:
		print graph.CheckOre();
		
	print command