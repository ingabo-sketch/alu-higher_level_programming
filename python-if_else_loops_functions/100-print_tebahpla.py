#!/usr/bin/python3
for letter in range(122, 96, -1):
    print("{}".format(chr(letter if letter % 2 == 0 else letter - 32)), end="")
