#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    c = 0
    for a in range(0, x):
        try:
            print("{:d}".format(my_list[a]), end="")
            c = c + 1
        except (TypeError, ValueError):
            pass
        a = a + 1
    print()
    return c
