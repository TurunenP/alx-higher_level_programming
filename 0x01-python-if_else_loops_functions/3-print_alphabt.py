#!/usr/bin/python3
# Print lowercase alphabet letters from 'a' to 'z' excluding 'e' and 'q'
for char_code in range(ord('a'), ord('z') + 1):
    if chr(char_code) != 'e' and chr(char_code) != 'q':
        print('{:c}'.format(char_code), end='')
