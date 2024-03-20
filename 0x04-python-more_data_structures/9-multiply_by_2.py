#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    diction = a_dictionary.copy()
    my_keys = list(diction.keys())

    for y in my_keys:
        diction[y] *= 2

    return (diction)
