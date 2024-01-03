'''
    Problem Statement: Write a function that reverses a string. The input string is given as an array of characters s.
    
'''

def reverseString(listofChar):
    left_index = 0
    right_index = len(listofChar) - 1

    while left_index < right_index:
        listofChar[left_index], listofChar[right_index] = listofChar[right_index], listofChar[left_index]
        left_index += 1
        right_index -= 1

listofChar = ["h","e","l","l","o"]
reverseString(listofChar)
print(listofChar)