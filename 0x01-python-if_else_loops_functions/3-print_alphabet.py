#!/usr/bin/python3
for letter in range(ord('a'), ord('z') + 1):
    if letter == 'e' || letter == 'q':
       break
    print('{:c}'.format(letter), end='')
