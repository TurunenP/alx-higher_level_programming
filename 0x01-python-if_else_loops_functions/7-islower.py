#!/usr/bin/python3
# Check if a character is lowercase
def islower(c):
    return ord('a') <= ord(c) <= ord('z')

# Example usage
char_to_check = 'a'
if islower(char_to_check):
    print(f"{char_to_check} is lowercase")
else:
    print(f"{char_to_check} is not lowercase")
