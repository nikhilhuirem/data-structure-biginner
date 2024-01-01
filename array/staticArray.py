
def insertEnd(arr, n, length, capacity):
    if length < capacity:
        arr[length] = n

def removeEnd(arr, length):
    if length > 0:
        arr[length - 1] = 0

