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
    
    def removeEdge(self, v1, v2)-> bool:
        if v1 in self.adj_list.keys() and v2 in self.adj_list.keys():
            try:
                self.adj_list[v1].remove(v2)
                self.adj_list[v2].remove(v1)
            except ValueError:
                pass
            return True
        return False

my_graph = Graph()
my_graph.addVertex('A')
my_graph.addVertex('B')
my_graph.addVertex('C')
my_graph.addVertex('D')
my_graph.addEdges('A','B')
my_graph.addEdges('B','C')
my_graph.addEdges('C','A')
my_graph.addEdges('A','D')
my_graph.printGraph()
my_graph.removeEdge('A','D')
my_graph.printGraph()