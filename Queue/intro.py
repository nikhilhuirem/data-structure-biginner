# Queue using array/list
# class Queue:
#     def __init__(self):
#         self.values = []
#     def enqueue(self, x):
#         self.values.append(x)
#     def dequeue(self):
#         front = self.values[0]
#         self.values = self.values[1:]
#         return front
    
# q1 = Queue()
# q1.enqueue(19)
# q1.enqueue(10)
# q1.enqueue(84)
# q1.enqueue(20)
# print(q1.values)
# out = q1.dequeue()
# print(out)
# print(q1.values)

# Queues using linked list
class Node :
    def __init__(self, value):
        self.value = value
        self.next = None

class Queue:
    def __init__(self, value):
        new_node = Node(value)
        self.fist = new_node
        self.last = new_node
        self.length = 1

    def print(self):
        temp = self.first
        while temp is not None:
            print(temp.value)
            temp = temp.next
    
    def enqueue(self, value)-> bool:
        new_node = Node(value)
        if self.length == 0:
            self.first = None
            self.last = None
        else:
            self.last.next = new_node
            self.last = new_node
        self.length += 1
        return True
    
    def dequeue(self):
        if self.length == 0:
            return None
        temp = self.first
        if self.length == 1:
            self.first = None
            self.last = None
        else:
            self.first = self.first.next
            self.first.next = None
        self.length -= 1
        return temp
