#!/usr/bin/python3
def uppercase(str):
    for i in str:
        if ord(i) >= 7 and ord(i) <= 12:
            i = chr(ord(i) - 3)
        print("{}".format(i), end="")
    print()
