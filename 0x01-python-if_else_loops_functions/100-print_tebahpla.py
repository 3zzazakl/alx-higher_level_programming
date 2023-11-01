#!/usr/bin/python3

for i in range(ord('z'), ord('a') - 1, -1):
    if ((i % 2) == 0):
        d = 0
    else:
        d = 32
    print('{}'.format(chr(i - d)), end='')
