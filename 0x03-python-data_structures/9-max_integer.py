#!/usr/bin/python3
def max_intege(my_list=[]):
    if my_list == []:
        return None
    max_int = 0
    for i in range(len(my_list)):
        if my_list[i] > max_int:
            max_int = my_list[i]
    return max_int
