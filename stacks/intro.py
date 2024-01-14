# Stack using arrays/list
# class Stack:
#     def __init__(self):
#         self.values = []
#     def push(self, x):
#         self.values = [x] + self.values
#     def pop(self):
#         return self.values.pop(0)
    
# s1 = Stack()
# s1.push(10)
# s1.push(20)
# s1.push(30)
# s1.push(40)
# s1.push(50)
# print(s1.values)
# print(s1.pop())
# print(s1.values)


# Stack using linked list

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
class Stack:
    def __init__(self, value):
        new_node = Node(value)
        self.top = new_node
        self.height = 1
    
    def push(self, value):
        new_node = Node(value)
        if self.height == 0:
            self.top = new_node
        else:
            new_node.next = self.top
            self.top = new_node
        self.height += 1
    