'''
    This technique is used to deal with problem that require you to find overlapping intervals.

    Example Proble: 
    Given a list of intervals, merge all the overlapping intervals to produce a list that has only mutaully exclusive intervals.

    The optimised version to solve the problem:
    1. Sort the intervals according to the starting point of each interval.
    2. Push the first interval into the stack.
    3. Iterate over each itervals:
        a. If the current intervals does not overlap with the top of the stack then, push the current interval into the stack.
        b. If the current interval does overlap with the top of the stack then, update the stack top with the ending time of the current interval.
    4. The stack now has the output merged intervals.

    this will take a time complexity of O(nlogn)
'''