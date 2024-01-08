def partition(arr, high, low):
    pivot = arr[high]

    i = low - 1
    for j in range(low, high):
        if arr[j] < pivot:
            i = i + 1
            arr[i], arr[j] = arr[j], arr[i]
        arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1

def quickSort(arr, high, low):
    if low < high:
        pi = partition(arr, high, low)

        quickSort(arr, pi -1, low)
        quickSort(arr, high, pi + 1)

arr = [30,20,40,50,10]
length = len(arr) - 1
quickSort(arr, length, 0)
print(arr)