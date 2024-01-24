'''
    Sliding window

    Used to perform a required operation on a specific window size of a given array or linked list

    Useful for problem dealing with subarrays or sublists

    Example problem:
    Given a array of positive numbers and a positive numbers K, find the maximum sum of an any contiguous subarray of size K.

    We can improve this approach by using the sliding window technique to move the window over the array from index K to the end of the array

    1. In each iteration,thw window-sum is updated by removing the element at the left side of the window(index i-K) and adding the element at the right side of the window (index i)

    2. Check if the window-sum is greater than the current max-sum and if so, update max-sum to keep track of the maximum sum found so far.
'''

def slidingWindow(arr, k):
    if k > len(arr) or k <= 0:
        return "Invalid Input"
    maxSum = 0
    currentSum = 0

    for i in range(k):
        print(i)
        currentSum = currentSum + arr[i]
    maxSum = currentSum
    for i in range(k, len(arr)):
        #print(currentSum)
        #print(i)
        currentSum = currentSum - arr[i - k] + arr[i]
        if currentSum > maxSum:
            maxSum = currentSum
    return maxSum

arr = [ 1, 4, 2, 10, 2, 3, 1, 0, 20 ]
k = 4
print(slidingWindow(arr,k))