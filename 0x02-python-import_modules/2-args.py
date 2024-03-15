#!/usr/bin/python3
import sys

if __name__ != "__main__":
    exit()

args = "{:d} argument"
argc = len(sys.argv) - 1
if argc == 0:
    args += 's.'
elif argc == 1:
    args += ':'
else:
    args += 's:'
print(args.format(argc))

k = 0
for arg in sys.argv:
    if k != 0:
        print("{:d}: {:s}".format(k, arg))
    k += 1
