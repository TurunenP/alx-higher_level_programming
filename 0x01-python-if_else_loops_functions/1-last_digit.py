#!/usr/bin/python3
import random

# Generate a random number between -10000 and 10000
generated_number = random.randint(-10000, 10000)

# Determine the last digit of the generated number
if generated_number < 0:
    last_digit = generated_number % -10
else:
    last_digit = generated_number % 10

# Check and print conditions based on the last digit
if last_digit > 5:
    print("The last digit of the randomly generated number {:d} is {:d} and is greater than 5"
          .format(generated_number, last_digit))
elif 0 < last_digit < 6:
    print("The last digit of the randomly generated number {:d} is {:d} and is less than 6 and not 0"
          .format(generated_number, last_digit))
else:
    print("The last digit of the randomly generated number {:d} is 0 and is 0".format(generated_number))
