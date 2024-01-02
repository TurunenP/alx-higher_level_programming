#!/usr/bin/python3

def is_lower_case(c):
    """Check if a character is lowercase."""
    return 97 <= ord(c) <= 122

# Example usage:
char_to_check = 'a'
result = is_lower_case(char_to_check)

print(f"Is '{char_to_check}' a lowercase character? {result}")
