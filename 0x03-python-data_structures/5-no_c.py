#!/usr/bin/python3
def no_c(my_string):
    new = ""
    for k in my_string:
        if k is not 'c' and k is not 'C':
            new += k
    return new
