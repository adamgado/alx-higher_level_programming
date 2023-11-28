#!/usr/bin/python3
def uppercase(str):
    for a in str:
        character = a
        if ord(character) > 96 and ord(character) < 123:
            character = chr(ord(a) - 32)
            print("{}".format(character), end='')
    print()
