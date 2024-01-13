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

    def print(self):
        temp = self.head
        for _ in range(self.length):
            print(temp.value)
            temp = temp.next
    
    def append(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
        self.length += 1
        return True
    
    def pop(self):
        if self.lenght == 0:
            return None
        temp = self.head
        if self.length == 0:
            self.head = None
            self.tail = None
        else:
            temp = self.tail
            self.tail = self.tail.prev
            temp.prev = None
        self.length -= 1
        return temp