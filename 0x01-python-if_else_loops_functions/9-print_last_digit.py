#!/usr/bin/python3

def print_last_digit(number):
    if number < 0:
        last_digit = number % -(10)
        print(abs(last_digit), end='')
    else:
        last_digit = number % 10
        print(last_digit, end='')
    return abs(last_digit)

# Call the function with a sample number
result = print_last_digit(-123)
print(" - Absolute value of the last digit:", result)
