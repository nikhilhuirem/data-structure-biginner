from typing import List
def prefixAverage1(arr: List[int])-> List[int]:
    A = []
    for i in range(len(arr)):
        a = 0
        for j in range(i):
            a = a + arr[j]
        A.append(a/(i+1))
    return A

def prefixAverage2(arr: List[int])-> List[int]:
    sum = 0
    A = []
    for i in range(len(arr)):
        sum = sum + arr[i]
        A.append(sum/(i+1))
    return A

arr = [1,2,3,4,5]
ans = prefixAverage1(arr)
print(ans)