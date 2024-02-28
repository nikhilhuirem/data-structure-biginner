def insertionSort(arr: list[int]):
    for j in range(1,len(arr)):
        key = arr[j]
        i = j - 1
        while i >= 0 and arr[i] > key:
            arr[i + 1] = arr[i]
            i -= 1
        arr[i + 1] = key

arr = [3,4,6,8,9,7,2,5,1]
ans = insertionSort(arr)
print(arr)