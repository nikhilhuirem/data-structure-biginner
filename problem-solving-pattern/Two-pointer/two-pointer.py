'''
    1. Two pointer traverse the data structure togrther until a specific condition is met.
    2. Handy for finding pairs in sorted array or linked list, such as comparing elements to each other in an array.
    3. Can be different types- both pointers starting from same end, or one pointer at each end.


    Lets take an example problem

    Given an array of integers nums and an intefer target, return indices of the two numbers such that they add up to target.

    The brute force approach would take two loops for forming pairs and comparing their sum to target. O(n^2)

    Two pointer Solution:
    1. Sort the given array
    2. Start two pointers. First pointer at the beginging of the array snd second at end.
    3. Get current sum of pointer A and B, if current sum is greater than target move pointer B back, else move pointer A forward.
'''

def twoPointer(nums, target):
    nums.sort()
    print(nums)

    i = 0
    j = len(nums) - 1

    while i < j:
        if nums[i] + nums[j] == target:
            return [i,j]
        elif nums[i] + nums[j] < target:
            i += 1
        else:
            j -= 1
    return 0

arr = [1,9,3,6,4]
print(twoPointer(arr,12))
