#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    end_list = []
    for a in range(len(my_list)):
        if my_list[a] % 2 == 0:
            end_list.append(True)
        else:
            end_list.append(False)
    return end_list
