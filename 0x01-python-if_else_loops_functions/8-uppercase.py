#!/usr/bin/python3
# Convert a string to uppercase
def uppercase(s):
    result = ""
    for char in s:
        if ord('a') <= ord(char) <= ord('z'):
            char = chr(ord(char) - 32)
        result += char
    print(result)

# Example usage
uppercase("Hello, World!")
