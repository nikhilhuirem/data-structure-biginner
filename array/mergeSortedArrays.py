''''
    Problem: In order to win the prize for most cookies sold, my friend Alice and I are going to merge our Girl Scout Cookies orders and enter as one unit.


'''

def merge_lists(my_list, alices_list):
    merged_list_size = len(my_list) + len(alices_list)
    merged_lists = [None] * merged_list_size

    current_index_alices = 0
    current_index_mine = 0
    current_index_merged = 0
    while current_index_merged < merged_list_size:
        if current_index_mine >= len(my_list):
            merged_lists[current_index_merged] = alices_list[current_index_alices]
            current_index_alices += 1
        elif current_index_alices >= len(alices_list):
            merged_lists[current_index_merged] = my_list[current_index_mine]
            current_index_mine += 1
        elif my_list[current_index_mine] < alices_list[current_index_alices]:
            merged_lists[current_index_merged] = my_list[current_index_mine]
            current_index_mine += 1
        else:
            merged_lists[current_index_merged] = alices_list[current_index_alices]
            current_index_alices += 1
        current_index_merged += 1

    return merged_lists
my_list = [3, 4, 6, 10, 11, 15]
alices_list = [1, 5, 8, 12, 14, 19]
print(merge_lists(my_list, alices_list))