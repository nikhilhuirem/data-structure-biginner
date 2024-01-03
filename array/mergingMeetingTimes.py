'''
    Problem Statement: Your company built an in-house calendar tool called HiCal. You want to add a feature to see the times in a day when everyone is available.

    To do this, you’ll need to know when any team is having a meeting. In HiCal, a meeting is stored as a tuple of integers (start_time, end_time). These integers represent the number of 30-minute blocks past 9:00am.
'''

def mergingMeeting(arr):
    arr.sort()
    merged = [arr[0]]
    for current_start, current_end in arr[1:]:
        last_start, last_end = merged[-1]

        if current_start <= last_end:
            merged[-1] = (last_start, max(last_end, current_end))
        else:
            merged.append((current_start, current_end))
    return merged

print(mergingMeeting([(0, 1), (3, 5), (4, 8), (10, 12), (9, 10)]))