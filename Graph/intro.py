class Graph:
    def __init__(self):
        self.adj_list = {}
    
    def printGraph(self):
        for vertex in self.adj_list:
            print("Vertex", ":", self.adj_list[vertex])
    