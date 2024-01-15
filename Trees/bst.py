class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class Binary_Search_Tree:
    def __init__(self):
        self.root = None
    
    def insert(self, value):
        new_node = Node(value)
        