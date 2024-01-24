'''
    Also known as the Hare & tortoise algoritm uses two pointers which move through the data structure at different speeds.

    Lets take one example problem:
    Given a non-empty, singly linked list with head node head we have to return the middle node. if there are two middle nodes, we have to return the second middle node.

    To solve this problem in a single traversal we can use the harse and tortoise approach.

    There are two pointers used in this methods, slow and fast.
    1. First with the fast pointer we move forward by two steps in each iteration
    2. With the slow pointer we move forward by only one step in each iteration.

    Whwn the fast pointer reaches the end of the linked list, the slow pointer will have reached the middle of the linked list.

    Pseudocode for this approach
    slowPointer = head
    fastPointer = head
    while fasPointer is not null and fastpointer.next is not null:
        slowpointer = slowpointer.next
        fastpointer = fastpointer.next.next
    middleElement = slowPointer.value

'''

def faS(singlyLinkedList):
    slowPointer = singlyLinkedList.head
    fastPointer = singlyLinkedList.head

    while slowPointer and fastPointer:
        slowPointer = slowPointer.next
        fastPointer = fastPointer.next.next

    return slowPointer.value
