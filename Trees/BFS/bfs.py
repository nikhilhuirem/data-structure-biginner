# BFS means Bredth First Search


class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self):
        self.root = None
    
    def insert(self, value)-> bool:
        newnode = Node(value)
        if self.root is None:
            self.root = newnode
            return True
        temp = self.root

        while(True):
            if newnode.value == temp.value:
                return False
            if newnode.value < temp.value:
                if temp.left is None:
                    temp.left = newnode
                    return True
                temp = temp.left
            else:
                if temp.right is None:
                    temp.right = newnode
                    return True
                temp = temp.right

    def contains(self, value)-> bool:
        if self.root is None:
            return False
        temp = self.root
        while(True):
            if temp.value > value:
                temp = temp.left
            elif temp.value < value:
                temp = temp.right
            else:
                return True
        return False
    
    def BFS(self):
        current_node = self.root
        queue = []
        results = []
        queue.append(current_node)

        while len(queue) > 0:
            current_node = queue.pop(0)
            results.append(current_node.value)
            if current_node.left is not None:
                queue.append(current_node.left)
            if current_node.right is not None:
                queue.append(current_node.right)
        return results

my_tree = BinarySearchTree()
my_tree.insert(47)
my_tree.insert(21)
my_tree.insert(76)
my_tree.insert(18)
my_tree.insert(27)
my_tree.insert(52)
my_tree.insert(82)
print(my_tree.BFS())