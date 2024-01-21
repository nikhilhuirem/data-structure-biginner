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
    
g1  = Graph()
g1.addVertex("A")
g1.printGraph()