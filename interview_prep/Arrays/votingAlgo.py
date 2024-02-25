from typing import List

def getMajorityElement(arr: List[int], size: int) -> int:
    majorityIndex = 0
    count = 1

    for index in range(1,size):
        if arr[majorityIndex] == arr[index]:
            count += 1
        else:
            count -= 1
        if count == 0:
            majorityIndex = index
            count = 1
    return arr[majorityIndex]

def isMajorityElement(arr: List[int], size: int, majorityIndex: int)-> bool:
    count: int = 0
    for index in range(size):
        if majorityIndex == arr[index]:
            count += 1
    return (count > size//2)

arr = [2,2,5,6,2,2]
size = len(arr)
print(isMajorityElement(arr, size, getMajorityElement(arr, size)))