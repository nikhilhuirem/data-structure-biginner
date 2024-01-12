class Node:
    def __init__(self, value) -> None:
        self.value = value
        self.next = None
        self.prev = None

class CircularLL:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        length = 1
