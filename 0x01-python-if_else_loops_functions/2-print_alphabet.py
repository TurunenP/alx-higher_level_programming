#!/usr/bin/python3
# Print lowercase alphabet letters from 'a' to 'z'
for char_code in range(ord('a'), ord('z') + 1):
    print('{:c}'.format(char_code), end='')
