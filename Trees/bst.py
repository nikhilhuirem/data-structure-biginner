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
        if self.root is None:
            self.root = new_node
            return True
        temp = self.root
        if new_node.value < temp.value:
            if temp.left is None:
                temp.left = new_node
                return True
            temp = self.left
        else:
            if temp.right is None:
                temp.right = new_node
                return True
            temp = self.right

            