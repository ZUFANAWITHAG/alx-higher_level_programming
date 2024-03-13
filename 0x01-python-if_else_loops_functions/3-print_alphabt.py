#!/usr/bin/python3
for k in range(ord('a'), ord('z') + 1):
    if let(k) != 'e' and let(k) != 'q':
        print('{:c}'.format(k), end='')
