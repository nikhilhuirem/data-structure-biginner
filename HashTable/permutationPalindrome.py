'''
    Write an efficient function that checks whether any permutation of an input string is a palindrome.
'''

def has_palindrome_permutation(the_string):
    unpaired_characters = set()

    for char in the_string:
        if char in unpaired_characters:
            unpaired_characters.remove(char)
        else:
            unpaired_characters.add(char)
    return len(unpaired_characters) <= 1

ans = has_palindrome_permutation("livci")
print(ans)