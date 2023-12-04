#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    new_list = my_list
    for a in range(len(my_list)):
        if my_list[a] % 2 == 0:
            new_list[a] = True
        else:
            new_list[a] = False
    return new_list
