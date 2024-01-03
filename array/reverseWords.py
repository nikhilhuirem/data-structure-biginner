'''
    Problem Statement: You're working on a secret team solving coded transmissions.
'''

def reverseWords(listofChar):
    reverse_character(listofChar, 0, len(listofChar) - 1)
    print(listofChar)
    current_word_start_index = 0
    for i in  range(len(listofChar) + 1):
        if (i == len(listofChar)) or (listofChar[i] == ' '):
            reverse_character(listofChar, current_word_start_index, i - 1)
            current_word_start_index = i + 1

def reverse_character(listofChar, left_index, right_index):
    while left_index < right_index:
        listofChar[left_index], listofChar[right_index] = listofChar[right_index], listofChar[left_index]
        left_index += 1
        right_index -= 1

message = [ 'c', 'a', 'k', 'e', ' ',
            'p', 'o', 'u', 'n', 'd', ' ',
            's', 't', 'e', 'a', 'l' ]
reverseWords(message)
print(''.join(message))