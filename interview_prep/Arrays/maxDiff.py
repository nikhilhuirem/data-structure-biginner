from typing import List

def getMaximumDifference(arr: List[int], size: int)-> int:
    minElementSofar = arr[0]
    maxDiffSoFar = arr[1] - arr[0]
    currentdiff = arr[1] - arr[0]
    
    for index in range(1,size):
        if arr[index] < minElementSofar:
            minElementSofar = arr[index]
        else:
            currentdiff = arr[index] - minElementSofar
            if(currentdiff > maxDiffSoFar):
                maxDiffSoFar = currentdiff
    return maxDiffSoFar

arr = [4,3,10,2,9,1,6]
size = len(arr)
print(f"Max Differece in the given array is", getMaximumDifference(arr, size))