#In this code we are going to talk all about in place algorithm

def square_list_in_place(int_list):
    for index, element in enumerate(int_list):
        int_list[index] *= element

def square_list_out_place(int_list):
    square_list = [None] * len(int_list)

    for i, element in enumerate(int_list):
        square_list[i] = element ** 2
    return square_list

list = [1, 2, 3, 4, 5]

print(square_list_out_place(list))
square_list_in_place(list)

print(list)

