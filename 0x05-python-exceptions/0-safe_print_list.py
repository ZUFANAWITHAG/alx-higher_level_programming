#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    k = 0
    printed = 0
    for k in range(0, x):
        try:
            print("{}".format(my_list[i]), end="")
            printed += 1
        except IndexError:
            continue
    print()
    return printed
