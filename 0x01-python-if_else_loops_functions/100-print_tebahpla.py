#!/usr/bin/python3

for i in range(ord('z'), ord('A') - 1, -1):
    print('{}'.format(chr(i - 32) if i % 2 == 0 else chr(i)), end='')
