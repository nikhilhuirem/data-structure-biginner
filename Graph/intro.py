class Graph:
    def __init__(self):
        self.adj_list = {}
    
    def printGraph(self):
        for vertex in self.adj_list:
            print(vertex, ":", self.adj_list[vertex])
    
    def addVertex(self, vertex):
        if vertex not in self.adj_list.keys():
            self.adj_list[vertex] = []
            return True
        return False
    def addEdges(self, v1, v2)-> bool:
        if v1 in self.adj_list.keys() and v2 in self.adj_list.keys():
            self.adj_list[v1].append(v2)
            self.adj_list[v2].append(v1)
            return True
        return False
    

g1  = Graph()
g1.addVertex("A")
g1.addVertex("B")
g1.printGraph()
g1.addEdges("A", "B")
g1.printGraph()